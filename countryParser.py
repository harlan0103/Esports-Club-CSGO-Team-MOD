import pycountry

name = "Andreas"
ln = "Hojsleth"
num = "1"
playerInfo = '[' + num + ']={ firstNmae="' + name + '", lastName="' + ln + '",},'

# List contains country name and abbreviation
country_list = {
	"Afghanistan" : "AFG",
	"Argentina" : "ARG",
	"Australia" : "AUS",
	"Austria" : "AUT",
	"Belgium" : "BEL",
	"Bosnia and Herzegovina" : "BIN",
	"Belarus" : "BLR",
	"Brazil" : "BRA",
	"Canada" : "CAN",
	"Chile" : "CHI",
	"China" : "CHN",                
	"Colombia" : "COL",
	"Croatia" : "CRO",
	"Czech Republic" : "CZE",
	"Egypt" : "EGY",
	"Spain" : "ESP",
	"Finland" : "FIN",
	"France" : "FRA",
	"Germany" : "GER",
	"Greece" : "GRE",
	"Hong Kong" : "HKG",
	"Hungary" : "HUN",
	"Indonesia" : "IDN",
	"India" : "IND",
	"Ireland" : "IRE",
	"Israel" : "ISR",
	"Italy" : "ITA",
	"Jordan" : "JOR",
	"Japan" : "JPN",
	"Kazakhstan" : "KAZ",
	"South Korea" : "KOR",
	"Saudi Arabia" : "KSA",
	"Mexico" : "MEX",
	"Mongolia" : "MGL", 
	"Netherlands" : "NED",
	"Norway" : "NOR",
	"New Zealand" : "NZL",
	"Peru" : "PER",
	"Philippines" : "PHI",
	"Poland" : "POL",
	"Portugal" : "POR",
	"Korea DPR" : "PRK",
	"Romania" : "ROU",
	"South Africa" : "RSA",
	"Russia" : "RUS",
	"Singapore" : "SIN",
	"Switzerland" : "SUI",
	"Slovakia" : "SVK",
	"Sweden" : "SWE",
	"Thailand" : "THA",
	"China Taipei" : "TPE",
	"Tunisia" : "TUN",
	"Turkey" : "TUR",
	"United Arab Emirates" : "UAE",
	"United Kingdom" : "UK",
	"Ukraine" : "UKR",
	"Uruguay" : "URU",
	"United States" : "USA",
	"Vietnam" : "VIE",
	"Denmark" : "DEN"
}


def parseCountryCode(nationName):
	if country_list.get(nationName) is None:
		return(nationName)
	else:
		return(country_list.get(nationName))
