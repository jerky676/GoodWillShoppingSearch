using DealScanner.Repostitory.Attributes;
using DealScanner.Repostitory.Enums.GoodWill;
using DealScanner.Repostitory.Enums.GoodWill;
using System;
using System.Collections.Generic;
using System.Text;

namespace DealScanner.Repostitory.Entities.GoodWill
{
    public class GoodWillSearch
    {
        public GoodWillSearch()
        {
            SearchGallery = GoodWillSearchGallery.None;
            ClosedAuctionEndDate = DateTime.Now.ToString("M/D/YYYY");
        }

        [Querystring("st")]
        public string KeywordSearch { get; set; }

        [Querystring("sg")]
        public GoodWillSearchGallery SearchGallery { get; set; }

        [Querystring("c")]
        public GoodWillCategories Categories { get; set; }

        [Querystring("s")]
        public GoodWillLocation Location { get; set; }

        [Querystring("lp")]
        public int LowPrice { get; set; }
        
        [Querystring("hp")]
        public int HighPrice { get; set; }

        [Querystring("sbn")]
        public bool ShowBuyNowOnly { get; set; }
        
        [Querystring("spo")]
        public bool ShowPickUpOnly { get; set; }

        [Querystring("snpo")]
        public bool HidePickUpOnly { get; set; }

        [Querystring("socs")]
        public bool ShowOneCentShipOnly { get; set; }

        [Querystring("sd")]
        public bool SearchDescription { get; set; }

        [Querystring("sca")]
        public bool ShowClosedAuctions { get; set; }

        [Querystring("caed")]
        public string ClosedAuctionEndDate { get; set; }

        [Querystring("cadb")]
        public int DayBack { get; set; }

        [Querystring("scs")]
        public bool SearchCanada { get; set; }

        [Querystring("sis")]
        public bool SearchInternational { get; set; }

        [Querystring("col")]
        public int FieldOrder { get; set; }

        [Querystring("p")]
        public int PageNumber { get; set; }

        [Querystring("ps")]
        public int PgaeSize { get; set; }

        [Querystring("desc")]
        public bool ShortDescription { get; set; }

        [Querystring("ss")]
        public int SavedSearchId { get; set; }

        [Querystring("UseBuyerPrefs")]
        public bool UseBuyerPrefrences { get; set; }
    }
}
