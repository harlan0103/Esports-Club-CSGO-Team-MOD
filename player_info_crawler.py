import requests
import urllib.request
import re
import os
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import countryParser

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def getTeamList():
	# This url is hltv.org top 50 teams list
	team_url = 'https://www.hltv.org/stats/teams?rankingFilter=Top50'
	soup = requests.get(team_url, headers = headers)
	data = BeautifulSoup(soup.text, 'lxml')

	# Parse the team page
	page = data.select('body > div[class=bgPadding] > div > div[class=colCon] > div[class=contentCol] > div > table > tbody > tr > td > a')

	for t in page:
		# We get team name and team page href
		team_name = t.get_text()
		team_url = 'https://www.hltv.org' + t['href']

		# Call playerPic() to get all player picture
		playerInfo(team_name, team_url)



def playerInfo(teamname, teamurl):	
	# We use header to pretend as explore
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

	soup = requests.get(teamurl, headers = headers)
	data = BeautifulSoup(soup.text, 'lxml')

	# page contains player name and img src, we need to parse them now
	page = data.select('body > div[class=bgPadding] > div > div[class=colCon] > div[class=contentCol] > div > div[class=grid] > div > img[class=container-width]')
	
	for p in page:
		# Example: Andreas 'Xyp9x' Højsleth
		player_name = p['title']
		# Parse player name to the nick name
		nick_name = player_name.split()[1].replace('\'','')
		print(nick_name)

		# Image src
		src = p['src']

		# Set nick name as the name of img
		name = teamname + '_' + nick_name + '.png'
		path = 'img/' + name
		# Get picture content as bytes and save into .jpg
		piccontent = requests.get(src, headers = headers)

		f = open(path, 'ab')
		f.write(piccontent.content)
		f.close()

		# Save player pic to local file
		save_info = 'saved ' + name + ' !'
		print(save_info)


		# Now get player profile from liquidpedia/counter-strike
		liquidpedia_url = 'https://liquipedia.net/counterstrike/' + nick_name

		# Get request to the url and parse the data
		player_page = requests.get(liquidpedia_url, headers = headers)
		player_page_data = BeautifulSoup(player_page.text, 'lxml')

		# Get player birthday and country information
		player_info = player_page_data.select('body > div[id=wrap] > div > div[class=row] > div > div > div[id=bodyContent] > div[id=mw-content-text] > div[class=mw-parser-output] > div > div > div > div[class=infobox-cell-2] > span > span[class=bday]')
		player_nation = player_page_data.select('body > div[id=wrap] > div > div[class=row] > div > div > div[id=bodyContent] > div[id=mw-content-text] > div[class=mw-parser-output] > div > div > div > div[class=infobox-cell-2] > a')

		try:
			bd = player_info[0].get_text().split('-')
		except (IndexError):
			birth = "1990.01.01"
		else:
			birth = bd[0] + '.' + bd[1] + '.' + bd[2]
		
		# Get 3-digit country code
		try:
			country_name = player_nation[0]['title']
		except (IndexError):
			country_code = "None"
		else:
			country_code = countryParser.parseCountryCode(country_name)
		print(country_code)
		# Now save player information as the .lua.txt format
		firstName = player_name.split()[0]
		lastName = player_name.split()[2]

		player_detail = '{ firstName = "' + firstName + '", lastName = "' + lastName + '", nickName = "' + nick_name + '", birth = "' + birth + '", nation = "' + country_code + '", region = "", customfigure = "' + name + '",  },\n'

		# Write player info detail to the .txt file
		player_file = open('playerData.txt', mode='a')
		player_file.write(player_detail)
		player_file.close()

if __name__ == '__main__':
	getTeamList()


