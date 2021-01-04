$st="dell" #keyword searc
$sg="" # menu searhc gallery new today ending today 
$c="" #categories
$s="43" #location 43 austin
$lp="0" # low price
$hp="999999" # hig price
$sbn="false" # Show Buy It Now Items Only 
$spo="false" # Show Pickup Only Items Only 
$snpo="false" # Hide Pickup Only Items 
$socs="false" # Show 1¢ Shipping Items Only 
$sd="false" # search descripyion
$sca="false" # search closed auctions
$caed="10/5/2020" # ClosedAuctionEndingDate
$cadb="7" # days back
$scs="false" # search canada
$sis="false" # search international
$col="1" # the field order
$p="1" # page number
$ps="40" # page size
$desc="false" # sort desc
$ss="0" #saved search id
$UseBuyerPrefs="true"



$url="https://www.shopgoodwill.com/Listings?"
$url+="st=$st&"
$url+="sg=$sg&"
$url+="c=$c&"
$url+="s=$s&"
$url+="lp=$lp&"
$url+="hp=$hp&"
$url+="sbn=$sbn&"
$url+="spo=$spo&"
$url+="snpo=$snpo&"
$url+="socs=$socs&"
$url+="sd=$sd&"
$url+="sca=$sca&"
$url+="caed=$caed&"
$url+="cadb=$cadb&"
$url+="scs=$scs&"
$url+="sis=$sis&"
$url+="col=$col&"
$url+="p=$p&"
$url+="ps=$ps&"
$url+="desc=$desc&"
$url+="ss=$ss&"
$url+="UseBuyerPrefs=$UseBuyerPrefs"


# Install the module on demand
If (-not (Get-Module -ErrorAction Ignore -ListAvailable PowerHTML)) {
    Write-Verbose "Installing PowerHTML module for the current user..."
    Install-Module PowerHTML -ErrorAction Stop
  }
  Import-Module -ErrorAction Stop PowerHTML


$searchClass = "data-container"
$productData = "product-data"
$searchnode="//span[@class=""$searchClass""]"

$htmlDom = ConvertFrom-Html -URI $url

$nodes = $($htmlDom.SelectNodes($searchnode))



foreach ($desc in $nodes){
    # $desc | Get-Member

    $desc.ParentNode | Get-Member
    exit
    # $desc.innerhtml
    # $productdata=$($desc.SelectSingleNode("//div[@class=""$productData""]"))

    # $productData.innerhtml
    # $productData.SelectSingleNode("//div[@class=""$productData""]")
}


# private static IEnumerable<HtmlNode> GetElementsWithClass(HtmlDocument doc, String className) {

#     Regex regex = new Regex( "\\b" + Regex.Escape( className ) + "\\b", RegexOptions.Compiled );

#     return doc
#         .Descendants()
#         .Where( n => n.NodeType == NodeType.Element )
#         .Where( e => e.Name == "div" && regex.IsMatch( e.GetAttributeValue("class", "") ) );
# }



# foreach($node in $nodes){
#     $node.HasClass($searchClass)
#     # $node.innerhtml 
# }


# .getElementsByClassName($searchClass) | %{Write-Host $_.innerhtml}

#for extra credit we can parse all the links
#$req.ParsedHtml.getElementsByTagName('a') | %{Write-Host $_.href} #outputs all the links


#$req



# $WebResponseObj # | Where-Object $_.class -eq "data-container"

# $HTML = New-Object -Com "HTMLFile"

# $HTML.IHTMLDocument2_write($WebResponseObj.Content)

# $HTML.ParsedHtml # .getElementsByTagName('span') 




#| Where-Object $_.class -eq "data-container"

# products = soup.find_all('span', {'class' : 'data-container'})