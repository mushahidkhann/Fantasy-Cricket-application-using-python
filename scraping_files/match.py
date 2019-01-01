from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 


urls0 = ['http://www.espncricinfo.com/series/8048/scorecard/1082591/Sunrisers-Hyderabad-vs-Royal-Challengers-Bangalore-1st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082592/Rising-Pune-Supergiant-vs-Mumbai-Indians-2nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082593/Gujarat-Lions-vs-Kolkata-Knight-Riders-3rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082594/Kings-XI-Punjab-vs-Rising-Pune-Supergiant-4th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082595/Royal-Challengers-Bangalore-vs-Delhi-Daredevils-5th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082596/Sunrisers-Hyderabad-vs-Gujarat-Lions-6th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082597/Mumbai-Indians-vs-Kolkata-Knight-Riders-7th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082598/Kings-XI-Punjab-vs-Royal-Challengers-Bangalore-8th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082599/Rising-Pune-Supergiant-vs-Delhi-Daredevils-9th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082600/Mumbai-Indians-vs-Sunrisers-Hyderabad-10th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082601/Kolkata-Knight-Riders-vs-Kings-XI-Punjab-11th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082602/Royal-Challengers-Bangalore-vs-Mumbai-Indians-12th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082603/Gujarat-Lions-vs-Rising-Pune-Supergiant-13th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082604/Kolkata-Knight-Riders-vs-Sunrisers-Hyderabad-14th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082605/Delhi-Daredevils-vs-Kings-XI-Punjab-15th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082606/Mumbai-Indians-vs-Gujarat-Lions-16th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082607/Royal-Challengers-Bangalore-vs-Rising-Pune-Supergiant-17th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082608/Delhi-Daredevils-vs-Kolkata-Knight-Riders-18th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082609/Sunrisers-Hyderabad-vs-Kings-XI-Punjab-19th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082610/Gujarat-Lions-vs-Royal-Challengers-Bangalore-20th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082611/Sunrisers-Hyderabad-vs-Delhi-Daredevils-21st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082612/Kings-XI-Punjab-vs-Mumbai-Indians-22nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082613/Kolkata-Knight-Riders-vs-Gujarat-Lions-23rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082615/Rising-Pune-Supergiant-vs-Sunrisers-Hyderabad-24th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082614/Mumbai-Indians-vs-Delhi-Daredevils-25th-match/']
urls1 = [ 'http://www.espncricinfo.com/series/8048/scorecard/1082616/Gujarat-Lions-vs-Kings-XI-Punjab-26th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082617/Kolkata-Knight-Riders-vs-Royal-Challengers-Bangalore-27th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082618/Mumbai-Indians-vs-Rising-Pune-Supergiant-28th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082620/Rising-Pune-Supergiant-vs-Kolkata-Knight-Riders-30th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082621/Royal-Challengers-Bangalore-vs-Gujarat-Lions-31st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082622/Kolkata-Knight-Riders-vs-Delhi-Daredevils-32nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082623/Kings-XI-Punjab-vs-Sunrisers-Hyderabad-33rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082624/Rising-Pune-Supergiant-vs-Royal-Challengers-Bangalore-34th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082625/Gujarat-Lions-vs-Mumbai-Indians-35th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082626/Kings-XI-Punjab-vs-Delhi-Daredevils-36th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082627/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-37th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082628/Mumbai-Indians-vs-Royal-Challengers-Bangalore-38th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082629/Rising-Pune-Supergiant-vs-Gujarat-Lions-39th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082630/Delhi-Daredevils-vs-Sunrisers-Hyderabad-40th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082631/Kolkata-Knight-Riders-vs-Rising-Pune-Supergiant-41st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082632/Delhi-Daredevils-vs-Gujarat-Lions-42nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082633/Royal-Challengers-Bangalore-vs-Kings-XI-Punjab-43rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082634/Sunrisers-Hyderabad-vs-Rising-Pune-Supergiant-44th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082635/Delhi-Daredevils-vs-Mumbai-Indians-45th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082636/Royal-Challengers-Bangalore-vs-Kolkata-Knight-Riders-46th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082637/Kings-XI-Punjab-vs-Gujarat-Lions-47th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082638/Sunrisers-Hyderabad-vs-Mumbai-Indians-48th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082639/Kings-XI-Punjab-vs-Kolkata-Knight-Riders-49th-match/']
urls2 = ['http://www.espncricinfo.com/series/8048/scorecard/1082640/Gujarat-Lions-vs-Delhi-Daredevils-50th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082641/Mumbai-Indians-vs-Kings-XI-Punjab-51st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082642/Delhi-Daredevils-vs-Rising-Pune-Supergiant-52nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082643/Gujarat-Lions-vs-Sunrisers-Hyderabad-53rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082644/Kolkata-Knight-Riders-vs-Mumbai-Indians-54th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082645/Rising-Pune-Supergiant-vs-Kings-XI-Punjab-55th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082646/Delhi-Daredevils-vs-Royal-Challengers-Bangalore-56th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082647/Mumbai-Indians-vs-Rising-Pune-Supergiant-Qualifier-1/', 'http://www.espncricinfo.com/series/8048/scorecard/1082648/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-Eliminator/', 'http://www.espncricinfo.com/series/8048/scorecard/1082649/Mumbai-Indians-vs-Kolkata-Knight-Riders-Qualifier-2/', 'http://www.espncricinfo.com/series/8048/scorecard/1082650/Mumbai-Indians-vs-Rising-Pune-Supergiant-Final/']
urls = [urls0, urls1, urls2]

def Matches(url, cursor):
	team_list = []	

	
	#Soup Object
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')

	#FIND NAMES OF TEAMS
	team_list = []
	for name in soup.find_all('a', {'class' : 'app_partial'}):
		print(name)
                for teams in name.find_all('span', {'class' : 'long-name'}):
                        print(teams)
			for team in teams:
				team_list.append(str(team.string))
	#FIND ID OF TEAM
	cursor.execute("select team_id from team where name = '" + team_list[0] + "'")
	team1_id = cursor.fetchone()[0]
	cursor.execute("select team_id from team where name = '" + team_list[1] + "'")
	team2_id = cursor.fetchone()[0]
	
	#FIND GROUND
	name = ((soup.find('div', {'class':'stadium-details'})).find('a')).find('span').string.split(',')[0]
	cursor.execute("select venue from team where name = '" + team_list[0] + "'")
	team1_ground = cursor.fetchone()[0]
	if name.split()[0] in team1_ground :
		ground_id = team1_id
	else :
		ground_id = team2_id
	
	#FIND DATES
	dates = soup.find_all('div', {'class':'match-detail--left'})
	i = 1
	for date in dates:
		if 'days' in date.find('h4').string:
			break
		i += 1
	j = 1
	for date in soup.find_all('div', {'class':'match-detail--right'}):
		if j == i:
			days = date.find('span').string
			break
		j += 1
	items = days.split()
	months = {"January":'01', "February":'02', "March":'03', "April":'04', "May":'05', "June":'06', "July":'07',"August":'08', "September":'09',"October":'10', "November":'11', "December":'12'}
	date = items[2] + "-" + months[items[1]] + "-" + items[0].split(',')[0] 



	#FIND TOSS and DECISION BAT = 1, FIELD = 0
	tosses = soup.find_all('div', {'class':'match-detail--left'})
	i = 1
	for toss in tosses:
		if toss.find('h4').string == 'Toss':
			break
		i += 1
	tosses = soup.find_all('div', {'class':'match-detail--right'})
	j = 1
	for toss in tosses:
		if j == i:
			s = toss.find('span').string.split(',')
			break
		j += 1
	if s[0].strip() == team_list[0]:
		toss = team1_id
		loss = team2_id
	else:
		toss = team2_id
		loss = team1_id
	
	if 'bat' in s[1]:
		batfirst = toss
	else:
		batfirst = loss

	#FIND WINNING TEAM
	team = soup.find_all('div', {'class' : 'game-status'})[1].string.split()[0]
	d = {'Delhi Daredevils':'DD', 'Gujarat Lions': 'GL', 'Kings XI Punjab':'KXIP', 'Kolkata Knight Riders':'KKR', 'Mumbai Indians':'MI', 'Rising Pune Supergiant':'RPS', 'Royal Challengers Bangalore':'RCB', 'Sunrisers Hyderabad':'SRH'}
	if team in team_list[0] or team in d[team_list[0]]:
		team_won = team1_id
	else:	
		team_won = team2_id


	#FIND MAN OF THE MATCH
	mans = soup.find_all('div', {'class':'match-detail--left'})
	i = 1
	for man in mans:
		if 'Player' in man.find('h4').string:
			break
		i += 1
	j = 1
	for man in soup.find_all('div', {'class':'match-detail--right'}):
		if j == i:
			MoM = man.find('a').string
			break
		j += 1
	
	cursor.execute("select name from player where team_id = '" + str(team_won) + "'")
	players = cursor.fetchall()
	name = MoM.split()
	flag = 0
	for player in players:
		if MoM in player[0]:
			man = player[0]
			flag = 1
			break
	if flag == 0:
		for player in players:
			if name[0] in player[0] or name[1] in player[0]:
				man = player[0]
				break
	cursor.execute("select player_id from player where name = '" + man + "'")
	player_id = cursor.fetchone()[0]
	return (team1_id, team2_id, ground_id, date, toss, batfirst, team_won, player_id)


def connect() :	
	#Connect to Database
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()

	for links in urls:
		for url in links:
			data = Matches(url, cursor)
			print(data)
#			cursor.execute("INSERT INTO matches(team1_id, team2_id, ground_id, dates, toss, batfirst, team_won, MoM) VALUES(%s, %s, %s,DATE %s, %s, %s, %s, %s);",data)
#	conn.commit()
#        cursor.close()
#        conn.close()
connect()



