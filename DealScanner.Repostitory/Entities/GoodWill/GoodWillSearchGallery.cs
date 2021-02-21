using System;
using System.Collections.Generic;
using System.Text;

namespace DealScanner.Repostitory.Entities.GoodWill
{
    public class GoodWillSearchGallery
    {
        public static readonly GoodWillSearchGallery NewToday = new GoodWillSearchGallery("New");
        public static readonly GoodWillSearchGallery EndingToday = new GoodWillSearchGallery("Ending");
        public static readonly GoodWillSearchGallery None = new GoodWillSearchGallery("");

        private GoodWillSearchGallery(string value)
        {
            Value = value;
        }

        public string Value { get; private set; }

        public override string ToString()
        {
            return Value;
        }

    }    
}
