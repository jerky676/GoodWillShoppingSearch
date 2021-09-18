from enum import Enum,unique

class GoodWillLocations(Enum):
    """
    Enumeration of the GoodWill locations.
    """
    # The GoodWill locations.
    # The order of the locations is not important.

    Empty = ""
    # Goodwill Easter Seals of the Gulf Coast Inc.
    AL_Mobile = 53
    # Goodwill Industries of Arkansas Inc.
    AR_Little_Rock = 13
    # Goodwill of Central &amp; Northern Arizona
    AZ_Phoenix = 201
    # Goodwill Industries of Southern Arizona
    AZ_Tucson = 148
    # Goodwill South Central California
    CA_Bakersfield = 71
    # Goodwill Industries of the Greater East Bay  Oakland Fairfield CA
    CA_Fairfield = 67
    # Goodwill Serving the People of Southern Los Angeles County
    CA_Long_Beach = 57
    # Goodwill Southern California
    CA_Los_Angeles = 78
    # Goodwill Industries of Ventura and Santa Barbara Counties
    CA_Oxnard = 26
    # Goodwill Industries Sacramento Valley
    CA_Sacramento = 162
    # Goodwill Central Coast 
    CA_Salinas = 75
    # Goodwill Industries of San Diego County 
    CA_San_Diego = 12
    # Goodwill of Silicon Valley 
    CA_San_Jose = 119
    # Goodwill of Orange County 
    CA_Santa_Ana = 2
    # Goodwill Industries of the Redwood Empire 
    CA_Santa_Rosa = 120
    # Goodwill Industries of San Francisco 
    CA_South_San_Francisco = 62
    # Goodwill Industries of San Joaquin Valley Inc. 
    CA_Stockton = 49
    # Discover Goodwill of Southern and Western Colorado 
    CO_Colorado_Springs = 73
    # Goodwill of Western &amp; Northern CT 
    CT_Bridgeport = 343
    # Goodwill Southern New England Inc. 
    CT_Hamden = 174
    # Goodwill Industries of Delaware &amp; Delaware County Inc. 
    DE_Wilmington = 42
    # Goodwill Industries of South Florida
    FL_Fort_Lauderdale = 16
    # Goodwill Industries of SW Florida Inc.
    FL_Fort_Myers = 81
    # Goodwill Industries of North Florida 
    FL_Jacksonville = 47
    # Gulfstream Goodwill Industries 
    FL_West_Palm_Beach = 34
    # Goodwill Industries of Central Florida 
    FL_Orlando = 109
    # Goodwill Industries Big Bend Inc. 
    FL_Tallahassee = 176
    # Goodwill-Suncoast 
    FL_Tampa = 66
    # Goodwill Industries of the Southern Rivers 
    GA_Columbus = 72
    # Goodwill Industries of Middle Georgia 
    GA_Macon = 195
    #  Goodwill of North Georgia 
    GA_Atlanta = 339
    # Goodwill Southeast Georgia 
    GA_Savannah = 98
    # Goodwill Hawaii 
    HI_Honolulu = 115
    # Goodwill of the Heartland 
    IA_Iowa_City = 10
    # Goodwill of Central Iowa 
    IA_Des_Moines = 102
    # Goodwill Industries of Northeast Iowa Inc. 
    IA_Waterloo = 171
    # Goodwill of the Great Plains Sioux City Iowa 
    IA_Sioux_City = 137
    # Boise Metro Goodwill 
    ID_Boise = 159
    # Goodwill Industries of Central Illinois Inc. 
    IL_East_Peoria = 90
    # Goodwill Industries of Northern Illinois 
    IL_Rockford = 135
    # Land of Lincoln Goodwill 
    IL_Springfield = 132
    # Goodwill Industries of Northeast Indiana East Inc.
    IN_Fort_WayneEast = 340
    # Goodwill Industries of Northeast Indiana Inc.
    IN_Fort_Wayne = 105
    # Goodwill of Central &amp; Southern Indiana 
    IN_Indianapolis = 5
    # Goodwill Industries of Michiana Inc. 
    IN_South_Bend = 50
    # Wabash Valley Goodwill 
    IN_Terre_Haute = 4
    # Goodwill Industries of Kansas INC. 
    KS_Wichita = 20
    # Goodwill Industries of Kentucky 
    KY_Louisville = 25
    # Goodwill Industries of Acadiana 
    LA_Lafayette = 202
    # Goodwill of North Louisiana 
    LA_Shreveport = 7
    # Goodwill Industries of the Chesapeake Inc. 
    MD_Baltimore = 11
    # Goodwill of Greater Washington D.C. 
    MD_Forestville = 76
    # Goodwill Monocacy Valley 
    MD_Frederick = 69
    # Horizon Goodwill Industries 
    MD_Hagerstown = 184
    # Goodwill of Northern New England 
    ME_Portland = 111
    # Goodwill Industries of Southeastern MI Inc. 
    MI_Adrian = 55
    # Goodwill Industries of Central Michigans Heartland 
    MI_Charlotte = 68
    # Green Works 
    MI_Detroit = 336
    # Goodwill Industries of Mid Michigan 
    MI_Flint = 114
    # Goodwill of Greater Grand Rapids 
    MI_Grandville = 9
    # Goodwill Industries of Southwestern Michigan 
    MI_Kalamazoo = 77
    # Goodwill Industries of West Michigan Inc. 
    MI_Muskegon = 86
    # Goodwill Industries of St. Clair County (Goodwill SCC) 
    MI_Port_Huron = 85
    # Goodwill Industries of Northern Michigan Inc. 
    MI_Traverse_City = 89
    # Goodwill-Easter Seals MN 
    MN_Brooklyn_Park = 106
    # Goodwill of Western Missouri &amp; Eastern Kansas 
    MO_Blue_Springs = 58
    # MERS/Missouri Goodwill Industries 
    MO_St_Louis = 140
    # Goodwill South Mississippi 
    MS_Gulfport = 129
    # Goodwill Industries of Mississippi 
    MS_Clinton = 178
    # Goodwill Industries of the Southern Piedmont 
    NC_Charlotte = 80
    # Goodwill Industries of Central North Carolina Inc. 
    NC_Greensboro = 46
    # Goodwill Industries of Northwest North Carolina Inc. 
    NC_Statesville = 181
    # Easter Seals Goodwill ND Inc. 
    ND_Bismarck = 154
    # Goodwill Industries of Greater Nebraska Inc. 
    NE_Grand_Island = 182
    # Goodwill Industries Serving Eastern Nebraska &amp; Southwest Iowa 
    NE_Omaha = 118
    # Goodwill Industries of Southern NJ &amp; Philadelphia 
    NJ_Bellmawr = 136
    # Goodwill Industries of Greater New York and Northern New Jersey 
    NY_New_York = 33
    # Goodwill of Southern Nevada 
    NV_Las_Vegas = 147
    # Goodwill Industries of Western New York 
    NY_Buffalo = 127
    # Goodwill of The Finger Lakes 
    NY_Rochester = 17
    # Goodwill Industries of Akron Ohio Inc. 
    OH_Akron = 27
    # Goodwill of Ashtabula Inc. 
    OH_Ashtabula = 97
    # Ohio Valley Goodwill Industries 
    OH_Cincinnati = 130
    # Goodwill Industries of South Central Ohio 
    OH_Chillicothe = 126
    # Goodwill Industries of Greater Cleveland & East Central Ohio 
    OH_Cleveland = 87
    # Goodwill Columbus 
    OH_Columbus = 107
    # Goodwill Easter Seals Miami Valley 
    OH_Dayton = 54
    # Marion Goodwill Industries 
    OH_Delaware = 103
    # Goodwill Industries of Lorain County 
    OH_Elyria = 172
    # Licking/Knox Goodwill Industries Inc. 
    OH_Newark = 32
    # Goodwill Industries of Northwest Ohio 
    OH_Oregon = 28
    # Goodwill Industries of Wayne and Holmes Counties Inc. 
    OH_Wooster = 6
    # Youngstown Area Goodwill Industries Inc. 
    OH_Youngstown = 84
    # Zanesville Welfare Organization and Goodwill Industries Inc. 
    OH_Zanesville = 344
    # Goodwill Industries of Southwest Oklahoma & North Texas 
    OK_Lawton = 188
    # Goodwill Industries Ontario Great Lakes Canada 
    ON_London = 180
    # Goodwill Industries of Lane & South Coast Counties 
    OR_Eugene = 59
    # Goodwill Industries of the Columbia Willamette 
    OR_Hillsboro = 8
    # Southern Oregon Goodwill Industries 
    OR_Medford = 15
    # Goodwill Keystone Area Berwyn 
    PA_Berwyn = 30
    # Goodwill Industries of North Central PA Inc. 
    PA_Falls_Creek = 146
    # Goodwill Industries of North Central PA Inc. 
    PA_DuBois = 345
    # Goodwill Industries NCPA 
    PA_Falls_Creek_NCPA = 341
    # Goodwill Keystone Area Harrisburg 
    PA_Harrisburg = 199
    # Goodwill of Southwestern Pennsylvania 
    PA_North_Versailles = 18
    # Goodwill Keystone Area Reading
    PA_Reading = 60
    # Goodwill Industries of Northeastern Pennsylvania 
    PA_Scranton = 179
    # Goodwill Industries of Upstate/Midlands South Carolina 
    SC_Columbia = 193
    # Goodwill Industries of Upstate/Midlands South Carolina 
    SC_Greenville = 22
    # Palmetto Goodwill 
    SC_North_Charleston = 177
    # Goodwill Industries of Upstate/Midlands South Carolina UNION 
    SC_Union = 342
    # Goodwill of the Great Plains Sioux Falls  South Dakota 
    SD_Sioux_Falls = 163
    # Goodwill Industries-Knoxville Inc. 
    TN_Knoxville = 337
    # Chattanooga Goodwill Industries Inc. 
    TN_Chattanooga = 346
    # Goodwill Industries of Middle Tennessee Inc. 
    TN_Nashville = 117
    # Goodwill West Texas 
    TX_Abilene = 138
    # Goodwill Industries of Central Texas 
    TX_Austin = 43
    # Goodwill Industries of Southeast Texas 
    TX_Beaumont = 23
    # Goodwill Industries of South Texas 
    TX_Corpus_Christi = 133
    # Goodwill Industries of Central East Texas Inc. 
    TX_Lufkin = 74
    # Shopgoodwill of El Paso 
    TX_El_Paso = 100
    # Goodwill Industries of Fort Worth 
    TX_Fort_Worth = 63
    # Goodwill Houston North 
    TX_Houston = 185
    # Goodwill Industries of Northwest Texas 
    TX_Lubbock = 104
    # Goodwill Industries of San Antonio 
    TX_San_Antonio = 164
    # Goodwill Industries of NE Texas 
    TX_Sherman = 338
    # Goodwill Industries of East Texas Inc. 
    TX_Tyler = 101
    # Heart of Texas Goodwill 
    TX_Waco = 144
    # SLC Metro Goodwill 
    UT_Salt_Lake_City = 192
    # Rappahannock Goodwill Industries Inc. 
    VA_Fredericksburg = 145
    # Goodwill of Central & Coastal Virginia
    VA_Hampton = 348
    # Goodwill of Central & Coastal Virginia
    VA_Richmond = 200
    # Goodwill Industries of the Valleys 
    VA_Salem = 191
    # Goodwill Industries of the Columbia Inc. 
    WA_Pasco = 155
    # Seattle Goodwill 
    WA_Seattle = 48
    # Goodwill Industries of the Inland Northwest Curve Apparel 
    WA_Spokane_Curve = 198
    # Goodwill Industries of the Inland Northwest 
    WA_Spokane = 19
    # Goodwill of the Olympics and Rainier Region 
    WA_Tacoma = 122
    # Goodwill of North Central Wisconsin 
    WI_Appleton = 134
    # Goodwill Industries of South Central Wisconsin Inc. 
    WI_Madison = 108
    # Goodwill Retail Services Inc. 
    WI_Racine = 29
    # Goodwill Industries of Kanawha Valley Inc. 
    WV_Charleston = 56
    # Goodwill Industries of KYOWVA Area Inc. 
    WV_Huntington = 31
    # Goodwill Industries of Wyoming Inc. 
    WY_Cheyenne = 150