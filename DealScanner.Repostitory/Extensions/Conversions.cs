using DealScanner.Repostitory.Attributes;
using DealScanner.Repostitory.Entities.GoodWill;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DealScanner.Repostitory.Extensions
{
    public static class Conversions
    {
        public static string ToQueryString<EntityType>(this EntityType dataEntity)
        {
            var properties = dataEntity.GetType().GetProperties();
            var queryString = "?";

            foreach (var property in properties)
            {
                var name = ((Querystring)property.GetCustomAttributes(typeof(Querystring), false).First()).Name;
                string value;

                if (property.PropertyType.BaseType == typeof(Enum))
                {
                    value = ((int)property.GetValue(dataEntity)).ToString();
                } else
                {
                    value = (string)property.GetValue(dataEntity).ToString();
                }               

                queryString += $"{name}=\"{value}\"&";
            }

            return queryString.TrimEnd('&');
        }

        public static string ToQueryString(this GoodWillSearch search)
        {
            return search.ToQueryString<GoodWillSearch>();
        }

    }
}
