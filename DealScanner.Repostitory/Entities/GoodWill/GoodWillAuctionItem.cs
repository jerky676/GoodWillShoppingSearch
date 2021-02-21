using System;
using System.Collections.Generic;
using System.Text;

namespace DealScanner.Repostitory.Entities.GoodWill
{
    public class GoodWillAuctionItem
    {
        public decimal Price { get; set; }

        public string ProductId { get; set; }

        public DateTime EndDate { get; set; }

        public double Duration { 
            get {
                return EndDate.Subtract(DateTime.Now).TotalMinutes;
            } }
    }
}
