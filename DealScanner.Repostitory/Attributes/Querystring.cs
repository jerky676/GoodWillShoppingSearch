using System;
using System.Collections.Generic;
using System.Text;

namespace DealScanner.Repostitory.Attributes
{
    public class Querystring : Attribute
    {
        public Querystring(string name)
        {
            Name = name;
        }

        public string Name { get; set; }
    }
}
