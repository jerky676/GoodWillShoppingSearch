using DealScanner.Repostitory.Entities.GoodWill;
using DealScanner.Repostitory.Repositories;
using DealScanner.Repostitory.Enums.GoodWill;
using Xunit;

namespace DealScanner.Tests
{
    public class GoodWillRepositoryTests
    {

        public GoodWillRepostiory GetRepository()
        {
            return new GoodWillRepostiory("https://www.shopgoodwill.com/");
        }


        [Fact]
        public void Test1()
        {
            var repository = GetRepository();

            var search = new GoodWillSearch();

            search.Categories = GoodWillCategories.Computers;
            search.Location = GoodWillLocation.TX_Austin;
            search.KeywordSearch = "xeon";

            var items = repository.SearchAuctions(search);
        }
    }
}
