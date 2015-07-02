import time
import json
import requests

"""===============================================================================

Some api pages
https://www.huobi.com/help/index.php?a=market_help&lang=en
https://bitpay.com/bitcoin-payment-gateway-api
https://blockchain.info/api
https://localbitcoins.com/api-docs/public/
https://www.bitstamp.net/api/
https://coinbase.com/docs/api/overview
https://coinbase.com/api/doc/1.0/prices/buy.html
https://coinbase.com/api/v1/prices/spot_rate
https://www.kraken.com/help/api
https://www.bitfinex.com/pages/api
http://bitcoincharts.com/about/markets-api/
https://www.bitfinex.com/pages/api
OKCOIN
Market Depth - https://www.okcoin.com/api/depth.do?ok=1
Futures Price Ticker - https://www.okcoin.com/api/future_ticker.do

http://btcchina.org/api-market-data-documentation-en

https://api.quadrigacx.com/v2/ticker?book=btc_cad
https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week


https://www.bitvc.com/help/api_futures_market?lang=en
http://market.bitvc.com/futures/ticker_btc_week.js


Tricks
\t* indents things


================================================================================="""
"""class exchanges():
    bitStampTick
    bitFinexTick
    krakenTick"""



    
def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last'] # replace last with timestamp etc
	
def bitfinex(): 
    bitFinexTick = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    return bitFinexTick.json()['last_price']	

def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker',data=json.dumps({"pair":"XXBTZUSD"}),
        headers={"content-type":"application/json"})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]


def coinbase():
    coinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy') # replace buy with spot_rate, sell etc
    return coinBaseTick.json()['amount'] # replace amount with currency etc

def coinsetUSD():
    coinsetter = requests.get('https://api.coinsetter.com/v1/marketdata/ticker') # replace buy with spot_rate, sell etc
    return coinsetter.json()['last'] ['price'] # replace amount with currency etc


def btceBU():
    btceBtcTick = requests.get('https://btc-e.com/api/2/btc_usd/ticker')
    return btceBtcTick.json()['ticker']['last'] # replace last with updated etc

	
def okcoinUSD(): 
    okcoinTick = requests.get("https://www.okcoin.com/api/ticker.do?ok=1")
    return okcoinTick.json()['ticker'] ['last'] # replace last with updated etc
#Chinese CNY Spot	
	
def okcoinCNY(): 
    okcoincn = requests.get("https://www.okcoin.cn/api/ticker.do")
    return okcoincn.json()['ticker'] ['last'] # replace last with updated etc

#def btcchinaCNY(): 
    btcchina = requests.get("https://data.btcchina.com/data/ticker?market=btccny")
    return btcchina.json() ['ticker'] ['high'] # replace last with updated etc


#Canadian Exchanges


def quadrigaUSD(): 
    quadrigausd = requests.get("https://api.quadrigacx.com/v2/ticker?book=btc_usd")
    return quadrigausd.json()['last'] # replace last with updated etc	


def quadrigaCAD(): 
    quadrigacad = requests.get("https://api.quadrigacx.com/v2/ticker?book=btc_cad")
    return quadrigacad.json()['last'] # replace last with updated etc	



#OKCOIN USD Futures 


def okcUSDFUTWEEK(): 
    okcweek = requests.get("https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week")
    return okcweek.json()['ticker'] ['last'] # replace last with updated etc


def okcUSDFUTBIWEEK(): 
    okcbiweek = requests.get("https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=next_week")
    return okcbiweek.json()['ticker'] ['last'] # replace last with updated etc


def okcUSDFUTQUARTER(): 
    okcquarter = requests.get("https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=quarter")
    return okcquarter.json()['ticker'] ['last'] # replace last with updated etc


#BITVC CNY Futures

def bitVCFUTWEEK(): 
    bitvcweek = requests.get("http://market.bitvc.com/futures/ticker_btc_week.js")
    return bitvcweek.json()['last'] # replace last with updated etc

def bitVCFUTBIWEEK(): 
    bitvcbiweek = requests.get("http://market.bitvc.com/futures/ticker_btc_next_week.js")
    return bitvcbiweek.json()['last'] # replace last with updated etc

def bitVCFUTQUARTERLY(): 
    bitvcquarterly = requests.get("http://market.bitvc.com/futures/ticker_btc_quarter.js")
    return bitvcquarterly.json()['last'] # replace last with updated etc	
	

		
"""=============================================================================="""


while True:
   #Spot Price
    btstampUSDLive = float(btstamp())
    bfxUSDLive = float(bitfinex())
    krakenUSDLive = float(kraken())
    coinbUSDLive = float(coinbase())
    btceUSDLive = float(btceBU())
    CoinsetterUSD = float(coinsetUSD())
    okcoinUSDSPOT = float(okcoinUSD())
   #Chinese CNY Spot 
    okcoinCNYSPOT = float(okcoinCNY())
    #BTCChinaCNY = float(btcchinaCNY())
   #Canada Spot
    QuadrigaUSD = float(quadrigaUSD())
    QuadrigaCAD = float(quadrigaCAD())
   #OKCOIN USD Futures
    OkcWeekly = float(okcUSDFUTWEEK())
    OkcBiWeekly = float(okcUSDFUTBIWEEK())
    OkcQuarterly = float(okcUSDFUTQUARTER())
   #BITVC CNY FUTURES
    BitVCWeekly = float(bitVCFUTWEEK())
    BitVCBIWeekly = float(bitVCFUTBIWEEK())
    BitVCQUARTERLY = float(bitVCFUTQUARTERLY())



   #Averages
    average1 = bfxUSDLive + btstampUSDLive + coinbUSDLive + krakenUSDLive + btceUSDLive + okcoinUSDSPOT
    average2 = OkcWeekly + OkcBiWeekly + OkcQuarterly
    average3 = BitVCWeekly + BitVCBIWeekly + BitVCQUARTERLY



    #okcoinUSDLive = float(okcoin())


    #okcFutLive = float(okcoinFut())
    print ("#######################################################################")	
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=Spot Prices=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("Bitstamp Price in USD =", btstampUSDLive)
    print ("Bitfinex Price in USD =", bfxUSDLive)
    print ("Kraken Price in USD =", krakenUSDLive)
    print ("Coinbase Price in USD =", coinbUSDLive)
    print ("BTC-e Price in USD =", btceUSDLive)
    print ("Coinsetter Price in USD =", CoinsetterUSD)
    print ("OKCoin.com Price in USD =", okcoinUSDSPOT)
    print ("QuadrigaCX Price in USD =", QuadrigaUSD)
    print ("=-=-=-=-=-=-=-=-=-=-=CNY Spot Prices=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("OKCoin.cn Price in CNY =", okcoinCNYSPOT)
    #print ("BTCCHINA Price in CNY =", btcchinaCNY)
    print ("=-=-=-=-=-=-=-=-=-=-=CAD Spot Prices=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("QuadrigaCX Price in CAD =", QuadrigaCAD)
    print ("Average of Stamp/BFX/Coinbase/Kraken/BTC-e/OKCoin ", average1 / 6)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("Difference betweeen Bitfinex and Bitstamp", bfxUSDLive - btstampUSDLive)
    print ("Difference betweeen Coinbase and Bitstamp", coinbUSDLive - btstampUSDLive)
    print ("Difference betweeen Bitstamp and BTC-e", btstampUSDLive - btceUSDLive)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("#######################################################################")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=OKCOIN FUTURES IN USD=-=-=-=-=-=-=-=-=-=-=-=-=")
    print ("Weekly Futures Last Price =", OkcWeekly)
    print ("Bi-Weekly Futures Last Price =", OkcBiWeekly)
    print ("Quarterly Futures Last Price =", OkcQuarterly)
    print ("Average of all Futures Contract Types ", average2 / 3)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=BITVC FUTURES IN CNY=-=-=-=-=-=-=-=-=-=-=-=-=")
    print ("Weekly Futures Last Price =", BitVCWeekly)
    print ("Bi-Weekly  Futures Last Price =", BitVCBIWeekly)
    print ("Quarterly Futures Last Price =", BitVCQUARTERLY)
    print ("Average of all Futures Contract Types ", average3 / 3)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=")

    time.sleep(15)
    
    
	




	
	
                                   
    
    




