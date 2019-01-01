from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 

mumurl = ['http://www.iplt20.com/teams/mumbai-indians/squad/107/Rohit-Sharma/', 'http://www.iplt20.com/teams/mumbai-indians/squad/1124/Jasprit-Bumrah/', 'http://www.iplt20.com/teams/mumbai-indians/squad/509/Jos-Buttler/', 'http://www.iplt20.com/teams/mumbai-indians/squad/103/Harbhajan-Singh/', 'http://www.iplt20.com/teams/mumbai-indians/squad/213/Mitchell-Johnson/', 'http://www.iplt20.com/teams/mumbai-indians/squad/730/Mitchell-McClenaghan/', 'http://www.iplt20.com/teams/mumbai-indians/squad/211/Lasith-Malinga/', 'http://www.iplt20.com/teams/mumbai-indians/squad/2740/Hardik-Pandya/', 'http://www.iplt20.com/teams/mumbai-indians/squad/3183/Krunal-Pandya/', 'http://www.iplt20.com/teams/mumbai-indians/squad/44/Parthiv-Patel/', 'http://www.iplt20.com/teams/mumbai-indians/squad/210/Kieron-Pollard/', 'http://www.iplt20.com/teams/mumbai-indians/squad/2738/Nitish-Rana/', 'http://www.iplt20.com/teams/mumbai-indians/squad/100/Ambati-Rayudu/', 'http://www.iplt20.com/teams/mumbai-indians/squad/1118/Karn-Sharma/', 'http://www.iplt20.com/teams/mumbai-indians/squad/595/Lendl-Simmons/', 'http://www.iplt20.com/teams/mumbai-indians/squad/307/Tim-Southee/', 'http://www.iplt20.com/teams/mumbai-indians/squad/163/Saurabh-Tiwaary/', 'http://www.iplt20.com/teams/mumbai-indians/squad/166/Vinay-Kumar/']
punurl = ['http://www.iplt20.com/teams/rising-pune-supergiant/squad/271/Steve-Smith/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/158/Mayank-Agarwal/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/32/Ankit-Sharma/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/92/Rajat-Bhatia/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/140/Deepak-Chahar/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/3763/Rahul-Chahar/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/181/Dan-Christian/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/1/MS-Dhoni/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/48/Ashok-Dinda/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/24/Faf-du-Plessis/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/3729/Lockie-Ferguson/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/898/Imran-Tahir/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/135/Ajinkya-Rahane/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/1154/Ben-Stokes/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/2973/Washington-Sundar/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/89/Manoj-Tiwary/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/958/Adam-Zampa/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/86/Jaydev-Unadkat/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/3838/Rahul-Tripathi/', 'http://www.iplt20.com/teams/rising-pune-supergiant/squad/1745/Shardul-Thakur/']
rcburl = ['http://www.iplt20.com/teams/royal-challengers-bangalore/squad/164/Virat-Kohli/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/162/Sreenath-Arvind/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/1561/Avesh-Khan/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/590/Samuel-Badree/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/148/Stuart-Binny/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/111/Yuzvendra-Chahal/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/1111/Aniket-Choudhary/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/233/AB-de-Villiers/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/236/Chris-Gayle/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/1020/Travis-Head/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/85/Iqbal-Abdulla/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/297/Kedar-Jadhav/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/72/Mandeep-Singh/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/3319/Tymal-Mills/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/434/Adam-Milne/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/53/Pawan-Negi/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/157/Harshal-Patel/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/1115/Sachin-Baby/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/1521/Billy-Stanlake/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/4305/Vishnu-Vinod/', 'http://www.iplt20.com/teams/royal-challengers-bangalore/squad/227/Shane-Watson/']
kkrurl = ['http://www.iplt20.com/teams/kolkata-knight-riders/squad/84/Gautam-Gambhir/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/969/Trent-Boult/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/184/Darren-Bravo/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/76/Piyush-Chawla/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/840/Nathan-Coulter-Nile/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/820/Colin-de-Grandhomme/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/1116/Sheldon-Jackson/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/37/Ishank-Jaggi/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/261/Kuldeep-Yadav/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/179/Chris-Lynn/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/203/Sunil-Narine/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/123/Manish-Pandey/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/96/Yusuf-Pathan/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/1106/Ankit-Rajpoot/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/201/Shakib-Al-Hasan/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/127/Robin-Uthappa/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/967/Chris-Woakes/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/108/Suryakumar-Yadav/', 'http://www.iplt20.com/teams/kolkata-knight-riders/squad/59/Umesh-Yadav/']
k11purl = ['http://www.iplt20.com/teams/kings-xi-punjab/squad/282/Glenn-Maxwell/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/61/Varun-Aaron/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/456/Hashim-Amla/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/412/Anureet-Singh/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/2743/KC-Cariappa/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/431/Martin-Guptill/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/253/Gurkeerat-Mann-Singh/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1505/Matt-Henry/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/191/Shaun-Marsh/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/187/David-Miller/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/197/Eoin-Morgan/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/3831/T-Natarajan/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1113/Axar-Patel/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/16/Wriddhiman-Saha/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/38/Ishant-Sharma/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1112/Sandeep-Sharma/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1107/Mohit-Sharma/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/3830/Rinku-Singh/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/964/Marcus-Stoinis/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/3180/Swapnil-Singh/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1749/Rahul-Tewatia/', 'http://www.iplt20.com/teams/kings-xi-punjab/squad/1085/Manan-Vohra/']
srhurl = ['http://www.iplt20.com/teams/sunrisers-hyderabad/squad/170/David-Warner/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/69/Bipul-Sharma/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/913/Ben-Cutting/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/41/Shikhar-Dhawan/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/388/Moises-Henriques/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/1556/Deepak-Hooda/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/1299/Chris-Jordan/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/3840/Mohammed-Siraj/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/618/Mohammad-Nabi/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/116/Bhuvneshwar-Kumar/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/1086/Siddarth-Kaul/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/113/Yuvraj-Singh/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/440/Kane-Williamson/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/2746/Barinder-Sran/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/1083/Vijay-Shankar/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/2885/Rashid-Khan/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/52/Naman-Ojha/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/115/Ashish-Nehra/', 'http://www.iplt20.com/teams/sunrisers-hyderabad/squad/1594/Mustafizur-Rahman/']
glurl = ['http://www.iplt20.com/teams/gujarat-lions/squad/14/Suresh-Raina/', 'http://www.iplt20.com/teams/gujarat-lions/squad/3177/Akshdeep-Nath/', 'http://www.iplt20.com/teams/gujarat-lions/squad/3826/Shubham-Agarwal/', 'http://www.iplt20.com/teams/gujarat-lions/squad/3825/Basil-Thampi/', 'http://www.iplt20.com/teams/gujarat-lions/squad/193/James-Faulkner/', 'http://www.iplt20.com/teams/gujarat-lions/squad/167/Aaron-Finch/', 'http://www.iplt20.com/teams/gujarat-lions/squad/40/Manpreet-Gony/', 'http://www.iplt20.com/teams/gujarat-lions/squad/2975/Ishan-Kishan/', 'http://www.iplt20.com/teams/gujarat-lions/squad/9/Ravindra-Jadeja/', 'http://www.iplt20.com/teams/gujarat-lions/squad/10/Shadab-Jakati/', 'http://www.iplt20.com/teams/gujarat-lions/squad/102/Dinesh-Karthik/', 'http://www.iplt20.com/teams/gujarat-lions/squad/101/Dhawal-Kulkarni/', 'http://www.iplt20.com/teams/gujarat-lions/squad/77/Praveen-Kumar/', 'http://www.iplt20.com/teams/gujarat-lions/squad/202/Brendon-McCullum/', 'http://www.iplt20.com/teams/gujarat-lions/squad/104/Munaf-Patel/', 'http://www.iplt20.com/teams/gujarat-lions/squad/49/Irfan-Pathan/', 'http://www.iplt20.com/teams/gujarat-lions/squad/1906/Jason-Roy/', 'http://www.iplt20.com/teams/gujarat-lions/squad/91/Pradeep-Sangwan/', 'http://www.iplt20.com/teams/gujarat-lions/squad/4320/Ankit-Soni/', 'http://www.iplt20.com/teams/gujarat-lions/squad/3186/Nathu-Singh/', 'http://www.iplt20.com/teams/gujarat-lions/squad/413/Dwayne-Smith/', 'http://www.iplt20.com/teams/gujarat-lions/squad/3827/Tejas-Baroka/', 'http://www.iplt20.com/teams/gujarat-lions/squad/1480/Andrew-Tye/']
ddurl = ['http://www.iplt20.com/teams/delhi-daredevils/squad/165/Zaheer-Khan/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/3823/Ankit-Bawne/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/968/Corey-Anderson/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/2756/Sam-Billings/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/2722/Carlos-Brathwaite/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/488/Pat-Cummins/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/1563/Shreyas-Iyer/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/217/Angelo-Mathews/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/30/Amit-Mishra/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/94/Mohammed-Shami/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/836/Chris-Morris/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/57/Shahbaz-Nadeem/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/276/Karun-Nair/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/2972/Rishabh-Pant/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/1664/Kagiso-Rabada/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/258/Sanju-Samson/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/99/Aditya-Tare/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/1740/Jayant-Yadav/', 'http://www.iplt20.com/teams/delhi-daredevils/squad/272/Marlon-Samuels/']
urls = [ddurl, glurl, k11purl, kkrurl, mumurl, punurl, rcburl, srhurl]


def Player(url):
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')
	player = []	
	i = 0
	#Player Name	
	try :
		name = soup.find('h1', {'class' : 'player-hero__name  player-hero__name--captain'})
		player.append(str(name.text))
	except :
		name = soup.find('h1' , {'class' : 'player-hero__name'})
		player.append(str(name.text))

	#Player Team
	player.append(str(soup.find('div', {'class' : 'team-info'}).find('h1').text))
	
	#Player Batting Style
	try:
		if str(soup.find('table', {'class':'player-details'}).find_all('td', {'class' : 'player-details__value'})[1].text)[:5] == 'Right':
			player.append("RIGHT")
		else:
			player.append("LEFT")
	except : 
		player.append("RIGHT")

	#Player Batting
	table1 = soup.find('table', {'class' : 'table table--scroll-on-phablet player-stats-table'})
	index = [1,3,4,5,7,8,9,10,11]
	row = table1.find('tr', {'class' : 'player-stats-table__highlight'})
	i = 0
	for stat in row.find_all('td'):
		if i in index:
			if '*' in stat.text:
				player.append(str(stat.text[:-1]))
				i += 1
				continue
			if stat.text == '-':
				player.append("0.0")
				i += 1
				continue
			player.append(str(stat.text))
		i += 1
	
	#Player Bowling
	table2 = soup.find_all('table', {'class':'table table--scroll-on-phablet player-stats-table'})[1]
	index = [4, 7, 9, 10]
	row = table2.find('tr', {'class' : 'player-stats-table__highlight'})
	i = 0
	for stat in row.find_all('td'):
		if i in index:
			if stat.text == '-':
				player.append("0.0")
				i += 1
				continue
			player.append(str(stat.text))
		i += 1
	return(player)

def connect() :	
	conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor()
	team_id = 1
	for teams in urls:
		for url in teams:
			player = Player(url)
			data = (player[0], team_id, player[2], int(player[3]), int(player[4]), int(player[5]), float(player[6]), float(player[7]), int(player[8]), int(player[9]), int(player[10]), int(player[11]), int(player[12]), float(player[13]), int(player[14]), int(player[15]), 0)
			print(data)
			cursor.execute("INSERT INTO player(name, team_id, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes, wickets, eco, fourhaul, fivehaul, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
		team_id += 1
	conn.commit()
        cursor.close()
        conn.close()


connect()
