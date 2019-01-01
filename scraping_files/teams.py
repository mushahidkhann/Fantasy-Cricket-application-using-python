from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 

urls = ['http://www.iplt20.com/teams/delhi-daredevils', 'http://www.iplt20.com/teams/gujarat-lions', 'http://www.iplt20.com/teams/kings-xi-punjab', 'http://www.iplt20.com/teams/kolkata-knight-riders', 'http://www.iplt20.com/teams/mumbai-indians', 'http://www.iplt20.com/teams/rising-pune-supergiant', 'http://www.iplt20.com/teams/royal-challengers-bangalore', 'http://www.iplt20.com/teams/sunrisers-hyderabad']   


def Team(url):
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')
	
	team_info = []
	
	team = soup.find('div', {'class' : 'team-info'})
	team_info.append(str(team.find('h1').text).strip())

	try : 
		winners = team.find('p', {'class' : 'winner'}).text
		win = winners.split(',')
		years = []
		for year in win:
			years.append(str(year.strip()))
		team_info.append(years)
	except:
		team_info.append("-")

	items = team.find('ul')
	for item in items.find_all('li') :
		if 'Owner' in item.text:
			team_info.append(str(item.text.split('Owner ')[1]))
		if 'Coach' in item.text:
			team_info.append(str(item.text.split('Coach ')[1]))
		if 'Venue' in item.text:
			team_info.append(str(item.text.split('Venue ')[1]))
		if 'Captain' in item.text:
			team_info.append(str(item.text.split('Captain ')[1]))

	name = str(team_info[0])
	win = str(team_info[1])
	owner = str(team_info[2])
	coach = str(team_info[3])
	venue = str(team_info[4])
	captain = str(team_info[5])
	print(team_info)
	return name, win, owner, coach, venue, captain

def connect() :
	#db = python_mysql_dbconfig.read_db_config()
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()
	i = 1
	for url in urls:
		data = Team(url)
		cursor.execute("INSERT INTO team(team_id, name, win_year, owner, coach, venue, captain) VALUES (%s, %s, %s, %s, %s, %s, %s)", (i, data[0], data[1], data[2], data[3], data[4], data[5]))
		i += 1
	conn.commit()
        cursor.close()
        conn.close()

connect()
