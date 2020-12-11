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

start-process $url