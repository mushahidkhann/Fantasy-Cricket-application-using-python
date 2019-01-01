from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 


urls0 = ['http://www.espncricinfo.com/series/8048/scorecard/1082591/Sunrisers-Hyderabad-vs-Royal-Challengers-Bangalore-1st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082592/Rising-Pune-Supergiant-vs-Mumbai-Indians-2nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082593/Gujarat-Lions-vs-Kolkata-Knight-Riders-3rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082594/Kings-XI-Punjab-vs-Rising-Pune-Supergiant-4th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082595/Royal-Challengers-Bangalore-vs-Delhi-Daredevils-5th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082596/Sunrisers-Hyderabad-vs-Gujarat-Lions-6th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082597/Mumbai-Indians-vs-Kolkata-Knight-Riders-7th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082598/Kings-XI-Punjab-vs-Royal-Challengers-Bangalore-8th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082599/Rising-Pune-Supergiant-vs-Delhi-Daredevils-9th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082600/Mumbai-Indians-vs-Sunrisers-Hyderabad-10th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082601/Kolkata-Knight-Riders-vs-Kings-XI-Punjab-11th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082602/Royal-Challengers-Bangalore-vs-Mumbai-Indians-12th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082603/Gujarat-Lions-vs-Rising-Pune-Supergiant-13th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082604/Kolkata-Knight-Riders-vs-Sunrisers-Hyderabad-14th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082605/Delhi-Daredevils-vs-Kings-XI-Punjab-15th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082606/Mumbai-Indians-vs-Gujarat-Lions-16th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082607/Royal-Challengers-Bangalore-vs-Rising-Pune-Supergiant-17th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082608/Delhi-Daredevils-vs-Kolkata-Knight-Riders-18th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082609/Sunrisers-Hyderabad-vs-Kings-XI-Punjab-19th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082610/Gujarat-Lions-vs-Royal-Challengers-Bangalore-20th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082611/Sunrisers-Hyderabad-vs-Delhi-Daredevils-21st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082612/Kings-XI-Punjab-vs-Mumbai-Indians-22nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082613/Kolkata-Knight-Riders-vs-Gujarat-Lions-23rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082615/Rising-Pune-Supergiant-vs-Sunrisers-Hyderabad-24th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082614/Mumbai-Indians-vs-Delhi-Daredevils-25th-match/']
urls1 = [ 'http://www.espncricinfo.com/series/8048/scorecard/1082616/Gujarat-Lions-vs-Kings-XI-Punjab-26th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082617/Kolkata-Knight-Riders-vs-Royal-Challengers-Bangalore-27th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082618/Mumbai-Indians-vs-Rising-Pune-Supergiant-28th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082620/Rising-Pune-Supergiant-vs-Kolkata-Knight-Riders-30th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082621/Royal-Challengers-Bangalore-vs-Gujarat-Lions-31st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082622/Kolkata-Knight-Riders-vs-Delhi-Daredevils-32nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082623/Kings-XI-Punjab-vs-Sunrisers-Hyderabad-33rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082624/Rising-Pune-Supergiant-vs-Royal-Challengers-Bangalore-34th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082625/Gujarat-Lions-vs-Mumbai-Indians-35th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082626/Kings-XI-Punjab-vs-Delhi-Daredevils-36th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082627/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-37th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082628/Mumbai-Indians-vs-Royal-Challengers-Bangalore-38th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082629/Rising-Pune-Supergiant-vs-Gujarat-Lions-39th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082630/Delhi-Daredevils-vs-Sunrisers-Hyderabad-40th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082631/Kolkata-Knight-Riders-vs-Rising-Pune-Supergiant-41st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082632/Delhi-Daredevils-vs-Gujarat-Lions-42nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082633/Royal-Challengers-Bangalore-vs-Kings-XI-Punjab-43rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082634/Sunrisers-Hyderabad-vs-Rising-Pune-Supergiant-44th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082635/Delhi-Daredevils-vs-Mumbai-Indians-45th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082636/Royal-Challengers-Bangalore-vs-Kolkata-Knight-Riders-46th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082637/Kings-XI-Punjab-vs-Gujarat-Lions-47th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082638/Sunrisers-Hyderabad-vs-Mumbai-Indians-48th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082639/Kings-XI-Punjab-vs-Kolkata-Knight-Riders-49th-match/']
urls2 = ['http://www.espncricinfo.com/series/8048/scorecard/1082640/Gujarat-Lions-vs-Delhi-Daredevils-50th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082641/Mumbai-Indians-vs-Kings-XI-Punjab-51st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082642/Delhi-Daredevils-vs-Rising-Pune-Supergiant-52nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082643/Gujarat-Lions-vs-Sunrisers-Hyderabad-53rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082644/Kolkata-Knight-Riders-vs-Mumbai-Indians-54th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082645/Rising-Pune-Supergiant-vs-Kings-XI-Punjab-55th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082646/Delhi-Daredevils-vs-Royal-Challengers-Bangalore-56th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082647/Mumbai-Indians-vs-Rising-Pune-Supergiant-Qualifier-1/', 'http://www.espncricinfo.com/series/8048/scorecard/1082648/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-Eliminator/', 'http://www.espncricinfo.com/series/8048/scorecard/1082649/Mumbai-Indians-vs-Kolkata-Knight-Riders-Qualifier-2/', 'http://www.espncricinfo.com/series/8048/scorecard/1082650/Mumbai-Indians-vs-Rising-Pune-Supergiant-Final/']
urls = [urls0, urls1, urls2]



def find_bowlers(soup) :
	ball_list = []
	ball = []
	j = 0
	for table in soup.find_all('table'):
		if j == 2:
			break
		j += 1
		table_rows = table.find_all('tr')
		for tr in table_rows:
			td = tr.find_all('td')
			row = [i.text for i in td]
			ball_list.append(row)
	for i in range(len(ball_list)):
		player = []
		if ball_list[i] == []:
			continue
		if len(ball_list[i]) == 10:
			for j in range(len(ball_list[i])-1):
				if (j != 1):
					player.append(str(ball_list[i][j]))
		else :
			for j in range(len(ball_list[i])-1):
				if (j != 1 and j != 7 and j != 8 and j != 9):
					player.append(str(ball_list[i][j]))
			
		ball.append(player)
	return ball

def Bowler(url, cursor):
	team_list = []
	
	#Soup Object
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')

	#FIND NAMES OF TEAMS
	team_list = []
	for name in soup.find_all('a', {'class' : 'team-name app_partial'}):
		for teams in name.find_all('span', {'class' : 'long-name'}):
			for team in teams:
				team_list.append(str(team.string))


	#FIND ID OF TEAM
	cursor.execute("select team_id from team where name = '" + team_list[0] + "'")
	team1_id = cursor.fetchone()[0]
	cursor.execute("select team_id from team where name = '" + team_list[1] + "'")
	team2_id = cursor.fetchone()[0]
		

	#Find all stats
	bowlers = find_bowlers(soup)
	cursor.execute("select name from player where team_id = '" + str(team1_id) + "' or team_id = '" + str(team2_id) + "'")
	players = cursor.fetchall()
	for bowler in bowlers :
		n = bowler[0].split()
		flag = 0
		if 'HH Pandya' in bowler[0]:
			bowler[0] = 'Hardik Pandya'
		if 'KH Pandya' in bowler[0]:
			bowler[0] = 'Krunal Pandya'
		if 'Aravind' in bowler[0]:
			bowler[0] = 'Sreenath Arvind'
		if 'DR Smith' in bowler[0]:
			bowler[0] = 'Dwayne Smith'
		if 'P Kumar' in bowler[0]:
			bowler[0] = 'Praveen Kumar'
		if 'B Kumar' in bowler[0]:
			bowler[0] = 'Bhuvneshwar Kumar'
		if 'I Sharma' in bowler[0]:
			bowler[0] = 'Ishant Sharma'
		if 'MM Sharma' in bowler[0]:
			bowler[0] = 'Mohit Sharma'
		if 'KV Sharma' in bowler[0]:
			bowler[0] = 'Karn Sharma'
		if 'C de Grandhomme' in bowler[0]:
			bowler[0] = 'Colin de Grandhomme'
		if 'UT Yadav' in bowler[0]:
			bowler[0] = 'Umesh Yadav'
		for player in players:
			if bowler[0] in player[0]:
				name = player[0]
				flag = 1
				break
		if flag == 0:
			for player in players:
				if n[1] in player[0]:
					name = player[0]
					flag = 1
					break
			if flag == 0:
				bowler[0] = 'PAPU'
				continue
		cursor.execute("select player_id from player where name = '" + name + "'")
		player_id = cursor.fetchone()[0]
		bowler[0] = player_id

	final = []
	for bowler in bowlers:
		if not bowler[0] == 'PAPU':
			final.append(bowler)	
	return(final)


def connect() :	
	#Connect to Database
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()
	cursor.execute("select match_id from matches order by match_id limit 1")
	match_id = cursor.fetchone()[0]

	for links in urls:
		for url in links:
			data = []
			items = Bowler(url, cursor)
			for i in range(len(items)):
				row = (items[i][0], match_id, int(float(items[i][1])), int(items[i][2]), int(items[i][3]), int(items[i][4]), float(items[i][5]), int(items[i][6]), int(items[i][7]))
				data.append(row)
			print(data)
			cursor.executemany("INSERT INTO match_player_bowl VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",data)
			match_id += 1
			conn.commit()
	cursor.close()
	conn.close()

connect()



