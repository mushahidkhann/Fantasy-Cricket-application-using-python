from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 


urls0 = ['http://www.espncricinfo.com/series/8048/scorecard/1082591/Sunrisers-Hyderabad-vs-Royal-Challengers-Bangalore-1st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082592/Rising-Pune-Supergiant-vs-Mumbai-Indians-2nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082593/Gujarat-Lions-vs-Kolkata-Knight-Riders-3rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082594/Kings-XI-Punjab-vs-Rising-Pune-Supergiant-4th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082595/Royal-Challengers-Bangalore-vs-Delhi-Daredevils-5th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082596/Sunrisers-Hyderabad-vs-Gujarat-Lions-6th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082597/Mumbai-Indians-vs-Kolkata-Knight-Riders-7th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082598/Kings-XI-Punjab-vs-Royal-Challengers-Bangalore-8th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082599/Rising-Pune-Supergiant-vs-Delhi-Daredevils-9th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082600/Mumbai-Indians-vs-Sunrisers-Hyderabad-10th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082601/Kolkata-Knight-Riders-vs-Kings-XI-Punjab-11th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082602/Royal-Challengers-Bangalore-vs-Mumbai-Indians-12th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082603/Gujarat-Lions-vs-Rising-Pune-Supergiant-13th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082604/Kolkata-Knight-Riders-vs-Sunrisers-Hyderabad-14th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082605/Delhi-Daredevils-vs-Kings-XI-Punjab-15th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082606/Mumbai-Indians-vs-Gujarat-Lions-16th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082607/Royal-Challengers-Bangalore-vs-Rising-Pune-Supergiant-17th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082608/Delhi-Daredevils-vs-Kolkata-Knight-Riders-18th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082609/Sunrisers-Hyderabad-vs-Kings-XI-Punjab-19th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082610/Gujarat-Lions-vs-Royal-Challengers-Bangalore-20th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082611/Sunrisers-Hyderabad-vs-Delhi-Daredevils-21st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082612/Kings-XI-Punjab-vs-Mumbai-Indians-22nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082613/Kolkata-Knight-Riders-vs-Gujarat-Lions-23rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082615/Rising-Pune-Supergiant-vs-Sunrisers-Hyderabad-24th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082614/Mumbai-Indians-vs-Delhi-Daredevils-25th-match/']
urls1 = [ 'http://www.espncricinfo.com/series/8048/scorecard/1082616/Gujarat-Lions-vs-Kings-XI-Punjab-26th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082617/Kolkata-Knight-Riders-vs-Royal-Challengers-Bangalore-27th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082618/Mumbai-Indians-vs-Rising-Pune-Supergiant-28th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082620/Rising-Pune-Supergiant-vs-Kolkata-Knight-Riders-30th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082621/Royal-Challengers-Bangalore-vs-Gujarat-Lions-31st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082622/Kolkata-Knight-Riders-vs-Delhi-Daredevils-32nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082623/Kings-XI-Punjab-vs-Sunrisers-Hyderabad-33rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082624/Rising-Pune-Supergiant-vs-Royal-Challengers-Bangalore-34th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082625/Gujarat-Lions-vs-Mumbai-Indians-35th-match/','http://www.espncricinfo.com/series/8048/scorecard/1082626/Kings-XI-Punjab-vs-Delhi-Daredevils-36th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082627/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-37th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082628/Mumbai-Indians-vs-Royal-Challengers-Bangalore-38th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082629/Rising-Pune-Supergiant-vs-Gujarat-Lions-39th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082630/Delhi-Daredevils-vs-Sunrisers-Hyderabad-40th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082631/Kolkata-Knight-Riders-vs-Rising-Pune-Supergiant-41st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082632/Delhi-Daredevils-vs-Gujarat-Lions-42nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082633/Royal-Challengers-Bangalore-vs-Kings-XI-Punjab-43rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082634/Sunrisers-Hyderabad-vs-Rising-Pune-Supergiant-44th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082635/Delhi-Daredevils-vs-Mumbai-Indians-45th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082636/Royal-Challengers-Bangalore-vs-Kolkata-Knight-Riders-46th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082637/Kings-XI-Punjab-vs-Gujarat-Lions-47th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082638/Sunrisers-Hyderabad-vs-Mumbai-Indians-48th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082639/Kings-XI-Punjab-vs-Kolkata-Knight-Riders-49th-match/']
urls2 = ['http://www.espncricinfo.com/series/8048/scorecard/1082640/Gujarat-Lions-vs-Delhi-Daredevils-50th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082641/Mumbai-Indians-vs-Kings-XI-Punjab-51st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082642/Delhi-Daredevils-vs-Rising-Pune-Supergiant-52nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082643/Gujarat-Lions-vs-Sunrisers-Hyderabad-53rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082644/Kolkata-Knight-Riders-vs-Mumbai-Indians-54th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082645/Rising-Pune-Supergiant-vs-Kings-XI-Punjab-55th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082646/Delhi-Daredevils-vs-Royal-Challengers-Bangalore-56th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082647/Mumbai-Indians-vs-Rising-Pune-Supergiant-Qualifier-1/', 'http://www.espncricinfo.com/series/8048/scorecard/1082648/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-Eliminator/', 'http://www.espncricinfo.com/series/8048/scorecard/1082649/Mumbai-Indians-vs-Kolkata-Knight-Riders-Qualifier-2/', 'http://www.espncricinfo.com/series/8048/scorecard/1082650/Mumbai-Indians-vs-Rising-Pune-Supergiant-Final/']
urls = [urls0, urls1, urls2]





def matches(url, cursor):
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')
	#FIND NAMES OF TEAMS
	teams_list = []
	for name in soup.find_all('a', {'class' : 'team-name app_partial'}):
		for teams in name.find_all('span', {'class' : 'long-name'}):
			for team in teams:
				teams_list.append(team.string)

	#FIND ID OF TEAM
	cursor.execute("select team_id from team where name = '" + teams_list[0] + "'")
	team1_id = cursor.fetchone()[0]
	cursor.execute("select team_id from team where name = '" + teams_list[1] + "'")
	team2_id = cursor.fetchone()[0]
	

	#Total Score
	total_list = []
	extras = []
	i = 0
	for total in soup.find_all('div', {'class' : 'wrap total'}):
		for cell in total.find_all('div'):
			if cell.string != "TOTAL":
				total = cell.string
				if 'all out' in total :
					wickets = 10
					runs = total.split()[0]
					overs = (total.split()[3])[1:]
					if i == 0:
						total_list.append([team1_id, int(runs), int(wickets), int(float(overs))])
					else : 
						total_list.append([team2_id, int(runs), int(wickets), int(float(overs))])
					i += 1
					continue
				data = total.split('/')
				runs = data[0]
				wickets = data[1].split()[0]
				overs = data[1].split()[1][1:]
				if i == 0:
					total_list.append([team1_id, int(runs), int(wickets), int(float(overs))])
				else : 
					total_list.append([team2_id, int(runs), int(wickets), int(float(overs))])
				i += 1

	#Extras
	i = 0
	for link in soup.findAll('div', {'class' : 'wrap extras'}):
		for cell in link.find_all('div'):
			if i % 2 != 0:
				data = cell.string
				extras = data.split(',')
				lb = nb = b = w = 0
				for extra in extras :
					if 'lb' in extra:
						s = extra.split()[-1]
						lb = s
						if s[-1] == ')':
							lb = s[:-1]
						continue
					if 'w' in extra:
						s = extra.split()[-1]
						w = s
						if s[-1] == ')':
							w = s[:-1]
					if 'nb' in extra:
						s = extra.split()[-1]
						nb = s
						if s[-1] == ')':
							nb = s[:-1]
						continue
					if 'b' in extra:
						s = extra.split()[-1]
						b = s
						if s[-1] == ')':
							b = s[:-1]
				if i == 1:
					total_list[0].extend([int(w),int(nb),int(b),int(lb)])
				else:
					total_list[1].extend([int(w),int(nb),int(b),int(lb)])
					
			i += 1
	return (total_list)

def connect() :	
	#Connect to Database
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()
	cursor.execute("select match_id from matches order by match_id limit 1")
	match_id = cursor.fetchone()[0]

	for links in urls:
		for url in links:
			data = []
			items = matches(url, cursor)
			for i in range(len(items)):
				row = (match_id, items[i][0], items[i][1], items[i][2], items[i][3], items[i][4], items[i][5], items[i][6], items[i][7])
				print(row)
				data.append(row)
			cursor.executemany("INSERT INTO match_team_performance VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",data)
			match_id += 1
	conn.commit()
	cursor.close()
	conn.close()

connect()

