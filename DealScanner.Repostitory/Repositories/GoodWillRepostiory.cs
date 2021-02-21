using DealScanner.Repostitory.Entities.GoodWill;
using DealScanner.Repostitory.Extensions;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace DealScanner.Repostitory.Repositories
{
    public class GoodWillRepostiory
    {
        public string Url { get; set; }
        private readonly string route = "Listing";

        public GoodWillRepostiory(string url)
        {
            if (!url.EndsWith("/"))
            {
                url += "/";
            }
            Url = $"{url}";
        }

        public HttpClient CreateClient()
        {
            return new HttpClient { BaseAddress = new System.Uri(Url) };
        }



        public async Task<List<GoodWillAuctionItem>> SearchAuctions(GoodWillSearch search)
        {
            var uri = $"{route}{search.ToQueryString()}";
            var client = CreateClient();


            try
            {
                var response = await client.GetAsync(uri);

                if (response.IsSuccessStatusCode)
                {
                    var test = await response.Content.ReadAsStringAsync();
                }
            }
            catch (Exception ex)
            {
                var test = ex;
            }








            return null;
        }




    }
}
