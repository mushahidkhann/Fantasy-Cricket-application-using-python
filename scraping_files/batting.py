from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata


urls0 = ['http://www.espncricinfo.com/series/8048/scorecard/1082591/Sunrisers-Hyderabad-vs-Royal-Challengers-Bangalore-1st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082592/Rising-Pune-Supergiant-vs-Mumbai-Indians-2nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082593/Gujarat-Lions-vs-Kolkata-Knight-Riders-3rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082594/Kings-XI-Punjab-vs-Rising-Pune-Supergiant-4th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082595/Royal-Challengers-Bangalore-vs-Delhi-Daredevils-5th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082596/Sunrisers-Hyderabad-vs-Gujarat-Lions-6th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082597/Mumbai-Indians-vs-Kolkata-Knight-Riders-7th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082598/Kings-XI-Punjab-vs-Royal-Challengers-Bangalore-8th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082599/Rising-Pune-Supergiant-vs-Delhi-Daredevils-9th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082600/Mumbai-Indians-vs-Sunrisers-Hyderabad-10th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082601/Kolkata-Knight-Riders-vs-Kings-XI-Punjab-11th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082602/Royal-Challengers-Bangalore-vs-Mumbai-Indians-12th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082603/Gujarat-Lions-vs-Rising-Pune-Supergiant-13th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082604/Kolkata-Knight-Riders-vs-Sunrisers-Hyderabad-14th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082605/Delhi-Daredevils-vs-Kings-XI-Punjab-15th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082606/Mumbai-Indians-vs-Gujarat-Lions-16th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082607/Royal-Challengers-Bangalore-vs-Rising-Pune-Supergiant-17th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082608/Delhi-Daredevils-vs-Kolkata-Knight-Riders-18th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082609/Sunrisers-Hyderabad-vs-Kings-XI-Punjab-19th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082610/Gujarat-Lions-vs-Royal-Challengers-Bangalore-20th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082611/Sunrisers-Hyderabad-vs-Delhi-Daredevils-21st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082612/Kings-XI-Punjab-vs-Mumbai-Indians-22nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082613/Kolkata-Knight-Riders-vs-Gujarat-Lions-23rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082615/Rising-Pune-Supergiant-vs-Sunrisers-Hyderabad-24th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082614/Mumbai-Indians-vs-Delhi-Daredevils-25th-match/']
urls1 = [ 'http://www.espncricinfo.com/series/8048/scorecard/1082616/Gujarat-Lions-vs-Kings-XI-Punjab-26th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082617/Kolkata-Knight-Riders-vs-Royal-Challengers-Bangalore-27th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082618/Mumbai-Indians-vs-Rising-Pune-Supergiant-28th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082620/Rising-Pune-Supergiant-vs-Kolkata-Knight-Riders-30th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082621/Royal-Challengers-Bangalore-vs-Gujarat-Lions-31st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082622/Kolkata-Knight-Riders-vs-Delhi-Daredevils-32nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082623/Kings-XI-Punjab-vs-Sunrisers-Hyderabad-33rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082624/Rising-Pune-Supergiant-vs-Royal-Challengers-Bangalore-34th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082625/Gujarat-Lions-vs-Mumbai-Indians-35th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082626/Kings-XI-Punjab-vs-Delhi-Daredevils-36th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082627/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-37th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082628/Mumbai-Indians-vs-Royal-Challengers-Bangalore-38th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082629/Rising-Pune-Supergiant-vs-Gujarat-Lions-39th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082630/Delhi-Daredevils-vs-Sunrisers-Hyderabad-40th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082631/Kolkata-Knight-Riders-vs-Rising-Pune-Supergiant-41st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082632/Delhi-Daredevils-vs-Gujarat-Lions-42nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082633/Royal-Challengers-Bangalore-vs-Kings-XI-Punjab-43rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082634/Sunrisers-Hyderabad-vs-Rising-Pune-Supergiant-44th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082635/Delhi-Daredevils-vs-Mumbai-Indians-45th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082636/Royal-Challengers-Bangalore-vs-Kolkata-Knight-Riders-46th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082637/Kings-XI-Punjab-vs-Gujarat-Lions-47th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082638/Sunrisers-Hyderabad-vs-Mumbai-Indians-48th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082639/Kings-XI-Punjab-vs-Kolkata-Knight-Riders-49th-match/']
urls2 = ['http://www.espncricinfo.com/series/8048/scorecard/1082640/Gujarat-Lions-vs-Delhi-Daredevils-50th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082641/Mumbai-Indians-vs-Kings-XI-Punjab-51st-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082642/Delhi-Daredevils-vs-Rising-Pune-Supergiant-52nd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082643/Gujarat-Lions-vs-Sunrisers-Hyderabad-53rd-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082644/Kolkata-Knight-Riders-vs-Mumbai-Indians-54th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082645/Rising-Pune-Supergiant-vs-Kings-XI-Punjab-55th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082646/Delhi-Daredevils-vs-Royal-Challengers-Bangalore-56th-match/', 'http://www.espncricinfo.com/series/8048/scorecard/1082647/Mumbai-Indians-vs-Rising-Pune-Supergiant-Qualifier-1/', 'http://www.espncricinfo.com/series/8048/scorecard/1082648/Sunrisers-Hyderabad-vs-Kolkata-Knight-Riders-Eliminator/', 'http://www.espncricinfo.com/series/8048/scorecard/1082649/Mumbai-Indians-vs-Kolkata-Knight-Riders-Qualifier-2/', 'http://www.espncricinfo.com/series/8048/scorecard/1082650/Mumbai-Indians-vs-Rising-Pune-Supergiant-Final/']
urls = [urls0, urls1, urls2]



def bat(soup) :

	run_list = []
	name_list = []
	out_list = []
	l = []
	#Batsmen Name	
	for link in soup.findAll('div',{'class' : 'cell batsmen'}):
		name_list.append(link.string)

	#Batsmen Runs
	i = 0
	links = soup.find('div', {'class' : 'wrap header'})
	for link in links.find_all('div', {'class' : 'cell runs'}):
		if link.string == 'M':
			break;
		i += 1
	j = 0
	for run in soup.find_all('div', {'class' : 'cell runs'}):
		if j != i:
			runs = run.string
			if runs == '-':
				runs = 0
			run_list.append(runs)
		j += 1
		j %= 6

	#	Not out = 0,  c/b = 1,  Run out = 2,  lbw = 3,  Bowled = 4,  Stumping = 5	
	out = []
	for link in soup.findAll('div', {'class' : "cell commentary"}):
		if link.string:
			out_list.append(link.string)
			continue
		if not link.string :
			out_list.append("a")
			continue
		else :	
			for a in link.find_all('a'):
				out_list.append(a.string)
	for item in out_list:
		items = item.split()
		if 'a' in items:
			out.append('a')
			continue
		if 'not' in items or 'retired' in items:
			out.append([0, 0, 0, 0])
			continue
		isout = 1
		bowler = ''
		dismissal_assist = ''
		if items[0] == 'c':
			dismissal_id = 1
			if items[1] == '&' and items[2] == 'b':
				for i in range(3, len(items)):
					bowler += items[i] + " "
				dismissal_assist = 0 
			else:
				i = 2
				dismissal_assist = items[1]
				while items[i] != 'b':
					dismissal_assist += " " + items[i]
					i += 1
				bowler = items[i + 1]
				for j in range(i + 2, len(items)):
					bowler += " " + items[j]
			out.append([dismissal_id, dismissal_assist, bowler, isout])
			continue
		if items[0] == 'run' and items[1] == 'out':
			dismissal_assist = items[2]
			for i in range(3, len(items)):
				dismissal_assist += " " + items[i]
			dismissal_assist = dismissal_assist[1:-1]
			out.append([2, dismissal_assist, 0, 1])
			continue
		if items[0] == 'lbw' :
			bowler = items[2]
			for i in range(3, len(items)):
				bowler += " " + items[i]
			out.append([3, 0, bowler, 1])
			continue
		if items[0] == 'hit':
			bowler = items[3] + " " + items[4]
			out.append([4, 0, bowler, 1])
		if items[0] == 'b':
			bowler = items[1]
			for i in range(2, len(items)):
				bowler += " " + items[i]
			out.append([4, 0, bowler, 1])
		if items[0] == 'st':
			i = 2
			dismissal_assist = items[1]
			while items[i] != 'b':
				dismissal_assist += " " + items[i]
				i += 1
			bowler = items[i + 1]
			for j in range(i + 2, len(items)):
				bowler += " " + items[j]
			out.append([5, dismissal_assist, bowler, isout])



	for i in range(len(name_list)):
		if name_list[i] == "BATSMEN":
			continue
		player = []
		player.append(name_list[i])
		for j in range(5):
			player.append(run_list[i*5 + j])
		player.extend(out[i])
		l.append(player)
	return l


def find_name(batsman, players, cursor):
	n = batsman.split()
	flag = 0

	if 'Z Khan' in batsman:
		batsman = 'Zaheer Khan'
	if 'PA Patel' in batsman:
		batsman = 'Parthiv Patel'
	if 'YK Pathan' in batsman:
		batsman = 'Yusuf Pathan'
	if 'AR Patel' in batsman:
		batsman = 'Axar Patel'
	if 'SPD Smith' in batsman:
		batsman = 'Steve Smith'
	if 'SV Samson' in batsman:
		batsman = 'Sanju Samson'
	if 'SA Yadav' in batsman:
		batsman = 'Suryakumar Yadav'
	if 'HH Pandya' in batsman:
		batsman = 'Hardik Pandya'
	if 'KH Pandya' in batsman:
		batsman = 'Krunal Pandya'
	if 'Aravind' in batsman:
		batsman = 'Sreenath Arvind'
	if 'DR Smith' in batsman:
		batsman = 'Dwayne Smith'
	if 'P Kumar' in batsman:
		batsman = 'Praveen Kumar'
	if 'B Kumar' in batsman:
		batsman = 'Bhuvneshwar Kumar'
	if 'I Sharma' in batsman:
		batsman = 'Ishant Sharma'
	if 'MM Sharma' in batsman:
		batsman = 'Mohit Sharma'
	if 'KV Sharma' in batsman:
		batsman = 'Karn Sharma'
	if 'C de Grandhomme' in batsman:
		batsman = 'Colin de Grandhomme'
	if 'UT Yadav' in batsman:
		batsman = 'Umesh Yadav'
	for player in players:
		if batsman in player[0]:
			name = player[0]
			flag = 1
			break
	if flag == 0:
		for player in players:
			p = player[0].split()
			if (len(p[1]) > 2 and p[1] in batsman) or (len(p[0]) > 2 and p[0] in batsman):
				name = player[0]
				flag = 1
				break
		if flag == 0:
			print(batsman)
			return 'PAPU'
	cursor.execute("select player_id from player where name = '" + name + "'")
	player_id = cursor.fetchone()[0]
	return player_id


def Batting(url, cursor):
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
	batsmen = bat(soup)
	cursor.execute("select name from player where team_id = '" + str(team1_id) + "' or team_id = '" + str(team2_id) + "'")
	players = cursor.fetchall()

	for batsman in batsmen :
		batsman[0] = find_name(batsman[0], players, cursor)
		if not batsman[8] == 0:
			batsman[8] = find_name(batsman[8], players, cursor)
			if batsman[8] == 'PAPU':
				batsman[8] = 0
		if not batsman[7] == 0:
			batsman[7] = find_name(batsman[7], players, cursor)
			if batsman[7] == 'PAPU':
				batsman[7] = 0

	final = []
	for batsman in batsmen:
		if not batsman[0] == 'PAPU':
			final.append(batsman)	
	return(final)


def connect() :	
	#Connect to Database
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()
	cursor.execute("select match_id from matches order by match_id limit 1")
	match_id = cursor.fetchone()[0]

	items = Batting(urls0[4], cursor)
	for links in urls:
		for url in links:
			data = []
			print(match_id - 57)
			items = Batting(url, cursor)
			for i in range(len(items)):
				row = (items[i][0], match_id, int(items[i][1]), int(items[i][2]), int(items[i][3]), int(items[i][4]), float(items[i][5]), int(items[i][6]), int(items[i][7]), int(items[i][8]), int(items[i][9]))
				print(row)
				data.append(row)
			cursor.executemany("INSERT INTO match_player_bat VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",data)
			match_id += 1
			conn.commit()
	cursor.close()
	conn.close()

connect()



