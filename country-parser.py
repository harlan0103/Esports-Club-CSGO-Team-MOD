import pycountry

name = "Andreas"
ln = "Hojsleth"
num = "1"
playerInfo = '[' + num + ']={ firstNmae="' + name + '", lastName="' + ln + '",},'
print(playerInfo)

nation = "Denmark"


country_list = {
	"Denmark" : "DEN"
}

print(country_list.get(nation))