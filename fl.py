from flask import Flask, render_template, request,flash
app = Flask(__name__)

import datetime
import mysql.connector

login_needed=1
try:
    conn = mysql.connector.connect(database="cricket", user="project",host="127.0.0.1",password="Cricket.1")
except:
    conn = mysql.connector.connect(database="python_mysql", user="root",host="127.0.0.1",password="vivbhav97")
cursor = conn.cursor(buffered=True)
cursor1 = conn.cursor(buffered=True)
#Even if previous user didn't logout, user_id will reset.
if login_needed:
    user_id = 0
else:
    user_id = 1

@app.route('/')
@app.route('/login.html')
def login_page(name=None):
    return render_template('login.html', name=name)

@app.route('/statistics.html')
def stats(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    return render_template('statistics.html', name=name)

@app.route('/groupleaderboard.html', methods=['POST', 'GET'])
def grleader(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    a = []
    if request.method == 'POST':
        grpname = request.form['groupname']
        if not grpname:
            return render_template('groupleaderboard.html', name=name, a = a, error="enter group name")
        cursor.execute(("select group_id from groups where groupname = '{}';".format(grpname)))
        a = cursor.fetchone()
        gid = a[0]
        cursor.execute(("select username, points from users where user_id in (select user_id from user_group where group_id = {}) order by points desc;".format(gid)))
        a = [i for i in cursor]
    return render_template('groupleaderboard.html', name=name, a = a)    
         

@app.route('/playervsplayer.html', methods=['POST', 'GET'])
def pvsp(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    if request.method == 'POST':
        player1 = request.form['player1']
        player2 = request.form['player2']
        if not player1 or not player2:
            return render_template('playervsplayer.html', name=name, row = [['-'] * 17]*2, error = "Enter names of both players")
        cursor.execute(("select * from player where name in ('{}', '{}');".format(player1, player2)))
        rows = [i for i in cursor]
    else:
        rows = [['-'] * 17]*2           
    return render_template('playervsplayer.html', name=name, row = rows)

#just add a logout button and add link /logout.html
@app.route('/logout.html')
def logout(name=None):
    global user_id 
    user_id = 0 #redirect to login page 
    return render_template('login.html', name=name)

@app.route('/topplayers.html')
def topplay(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    cursor.execute(("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by runs desc limit 20"))
    rows = [i for i in cursor]
    cursor1.execute(("select name, wickets, eco, fourhaul, fivehaul from player order by wickets desc limit 20"))
    rows1 = [i for i in cursor1]
    return render_template('topplayers.html', name=name, rows = rows, rows1 = rows1)

@app.route('/squadselect.html', methods=['POST', 'GET'])
def squad(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    date = "2017-05-05"#datetime.datetime.today().strftime('%Y-%m-%d')
    error = ""
    cursor.execute(("select name, matches, average, strike_rate, wickets,eco,price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}');".format(date,date)))
    cursor1.execute(("select budget from users where user_id = {};".format(user_id)))
    b = cursor1.fetchone()
    budget = b[0]
    p = 0
    if request.method == 'POST':
        try:
            name = request.form['send_button']
        except:
            try:
                name1 = request.form['send_button1']
                name = ""
            except:
                name1 = name = ""
                name2 = request.form['send_button2']
        if name:
            name = name[7:]
            cursor1.execute(("select player_id, price from player where name = '{}';".format(name)))
            a = cursor1.fetchone()
            try:
                if budget - int(a[1]) >= 0:
                    cursor1.execute(("insert into userplayer values ('{}', '{}');".format(user_id, a[0])))
                    budget -= int(a[1])
                    cursor1.execute(("update users set budget={} where user_id = {};".format(str(budget), user_id)))
                else:
                    error = "Budget is insufficient"
            except mysql.connector.Error as err:
                if err[0] == 1062:#error number
                    error = "Player already selected"
                else:#1644
                    error = "You can select at the most 10 players"
        elif name1:
            name = name1[7:]
            cursor1.execute(("select player_id, price from player where name = '{}';".format(name)))
            a = cursor1.fetchone()
            add = int(a[1])
            p_id = a[0]
            cursor1.execute(("select * from userplayer where user_id={} and player_id={};".format(user_id, p_id)))
            if cursor1.fetchone():
                cursor1.execute(("delete from userplayer where user_id={} and player_id={};".format(user_id, p_id)))
                budget += add
                cursor1.execute(("update users set budget={} where user_id = {};".format(str(budget), user_id)))
        else:
            if name2 == "Name":
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by name ASC".format(date,date)))
            elif name2 == 'Matches':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by matches DESC".format(date,date)))
            elif name2 == 'Average':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by average DESC".format(date,date)))
            elif name2 == 'Strike Rate':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by strike_rate DESC".format(date,date)))
            elif name2 == 'Wickets':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by wickets DESC".format(date,date)))
            elif name2 == 'Economy':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by eco ASC".format(date,date)))
            elif name2 == 'Price':
                cursor.execute(("select name, matches, average, strike_rate, wickets, eco, price from player where team_id in (select team1_id from matches where dates = '{}') or team_id in (select team2_id from matches where dates = '{}') order by price DESC".format(date,date)))
        cursor1.execute(("commit;"))
    rows = [i for i in cursor]
    cursor1.execute(("select name, price from player where player_id in (select player_id from userplayer where user_id= '{}');".format(user_id)))
    rows1 = [j for j in cursor1]
    cursor1.execute(("select runs, wickets from player where player_id in(select player_id from userplayer where user_id = {})".format(user_id)))
    for a in cursor1:
        p += (a[0] + a[1]*10)/100
    cursor1.execute("UPDATE users set points = {} where user_id = {}".format(p, user_id))
    return render_template('squadselect.html', name=name, rows = rows, rows1 = rows1, error = error, budget = budget, p = p)

@app.route('/price.html')
def plist(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player")
    rows = [i for i in cursor]
    return render_template('price.html', name=name, rows=rows)

@app.route('/price.html', methods=['POST','GET'])
def batlist(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    if request.form['send_button'] == 'Name':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by name ASC")
    elif request.form['send_button'] == 'Batting Style':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by batstyle DESC")
    elif request.form['send_button'] == 'Matches':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by matches DESC")
    elif request.form['send_button'] == 'Runs':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by runs DESC")
    elif request.form['send_button'] == 'Highest Score':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by highest_score DESC")
    elif request.form['send_button'] == 'Average':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by average DESC")
    elif request.form['send_button'] == 'Strike Rate':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by strike_rate DESC")
    elif request.form['send_button'] == 'Hundreds':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by hundreds DESC")
    elif request.form['send_button'] == 'Fifties':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by fifties DESC")
    elif request.form['send_button'] == 'Fours':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by fours DESC")
    elif request.form['send_button'] == 'Sixes':
        cursor.execute("select name, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player order by sixes DESC")
    else:
        cursor.execute("select name, batstyle, matches, run`s, highest_score, average, strike_rate, hundreds, fifties, fours, sixes from player")
    rows = [i for i in cursor]
    return render_template('price.html', name=name, rows=rows)

@app.route('/bowling.html', methods=['POST', 'GET'])
def bowl(name=None):
    global user_id
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    if request.method == "POST":
        if request.form['send_button'] == 'Name':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by name asc")
        elif request.form['send_button'] == 'Matches':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by matches desc")
        elif request.form['send_button'] == 'Wickets':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by wickets desc")
        elif request.form['send_button'] == 'Economy':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by eco asc")
        elif request.form['send_button'] == '4 Wicket Hauls':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by fourhaul desc")
        elif request.form['send_button'] == '5 Wicket Hauls':
            cursor.execute("select name, matches, wickets, eco, fourhaul,fivehaul from player order by fivehaul desc")
    else:
        cursor.execute("select name, matches, wickets, eco, fourhaul, fivehaul, price from player")
    rows = [i for i in cursor]
    return render_template('bowling.html', name=name, rows=rows)

@app.route('/administrator.html')
def ulist(name=None):
    global user_id 
    if login_needed:
        if user_id != 1:
            return render_template('login.html', name=name)
    cursor.execute("select * from users;")
    rows = [i for i in cursor]
    return render_template('administrator.html', name=name, rows=rows)

@app.route('/schedule.html')
def sched(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    cursor1.execute("""select t1.name, t2.name, matches.dates, ground.name from matches join ground on ground.ground_id = matches.ground_id join team as t1 on matches.team1_id = t1.team_id join team as t2 on matches.team2_id = t2.team_id order by matches.dates;""")
    ans = [i for i in cursor1]
    return render_template('schedule.html', name=name, ans=ans)


@app.route('/home.html')
def matchinfo(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    return render_template('home.html', name=name)

@app.route('/', methods=['POST','GET'])
@app.route('/login.html', methods=['POST','GET'])
def login_page_post(name=None):
    global user_id 
    username, password = request.form['username'],request.form['password']
    cursor.execute(("select password, user_id from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        return render_template('login.html', name=name,error1="Incorrect username",error2="")
    if a[0] == password:
        user_id = int(a[1])
        return render_template('home.html', name=name)
    else:
        return  render_template('login.html', name=name,error2="Incorrect Password",error1="")

@app.route('/registration.html')
def registration_page(name=None):
    return render_template('registration.html', name=name)


@app.route('/registration.html', methods=['POST','GET'])
def registration_page_post(name=None):
    global user_id 
    firstname = request.form['firstname']
    if not firstname:
        return  render_template('registration.html', name=name,error="Enter firstname")
    lastname = request.form['lastname']
    if not lastname:
        return  render_template('registration.html', name=name,error="Enter lastname")
    username = request.form['username']
    if not username:
        return  render_template('registration.html', name=name,error="Enter username")
    email = request.form['emailid']
    if not email:
        return  render_template('registration.html', name=name,error="Enter email-id")
    favteam = request.form['favouriteteam']
    if not favteam:
        return  render_template('registration.html', name=name,error="Enter name of your favourite team")
    password = request.form['password']
    if not password:
        return  render_template('registration.html', name=name,error="Password not entered")
    cpassword = request.form['cpassword']
    if password != cpassword:
        return  render_template('registration.html', name=name,error="Passwords do not match")
    cursor.execute(("select password from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        cursor.execute(("insert into users(username, password,firstname,lastname, email, favteam, budget, points) values('{}', '{}', '{}', '{}', '{}', '{}', 1300000, 0);".format(username, password,firstname,lastname, email, favteam)))
        cursor.execute(("select user_id from users where username ='{}';".format(username)))
        a = cursor.fetchone()
        user_id = int(a[0])
        #cursor.execute(("""delimiter // create trigger t{} before insert on userplayer for each row begin if (select count(player_id) from userplayer where user_id = {} group by user_id) > 9 then signal sqlstate "10000" set message_text = 'no';end if; end // delimiter ;""".format(str(a[0]),str(a[0]))))
        cursor.execute(("commit;"))
        return render_template('home.html', name=name)
    else:
        return  render_template('registration.html', name=name,error="Username is already taken!")

@app.route('/creategroup.html')
def create_group_page(name=None):
    global user_id 
    if not user_id:
        return render_template('login.html', name=name)
    return render_template('creategroup.html', name=name)

@app.route('/creategroup.html', methods=['POST','GET'])
def create_group(name=None):
    global user_id 
    grpname = request.form['grpname']
    if not grpname:
        return render_template('creategroup.html', name=name,error="Enter group name!")
    cursor.execute(("select group_id from groups where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    if a:
        return render_template('creategroup.html', name=name,error="Group name is already taken!")
    cursor.execute(("insert into groups(groupname) values('{}');".format(grpname)))
    cursor.execute(("commit;"))
    cursor.execute(("select group_id from groups where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    group_id = a[0]
    cursor.execute(("insert into user_group(user_id, group_id) values('{}','{}');".format(user_id, group_id)))
    cursor.execute(("commit;"))
    return render_template('addtogroup.html', name=name)

@app.route('/addtogroup.html')
def addto_group_page(name=None):
    global user_id 
    if not user_id:
        return render_template('login.html', name=name)
    return render_template('addtogroup.html', name=name)

@app.route('/addtogroup.html', methods=['POST','GET'])
def addto_group(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    username = request.form['username']
    grpname = request.form['groupname']
    if not username or not grpname:
        return render_template('addtogroup.html', name=name,error="Enter both values")
    cursor.execute(("select user_id from users where username ='{}';".format(username)))
    a = cursor.fetchone()
    if not a:
        return render_template('addtogroup.html', name=name,error="Invalid username")
    else:
        uid = a[0]
    cursor.execute(("select group_id from groups where groupname='{}';".format(grpname)))
    a = cursor.fetchone()
    if not a:
        return render_template('addtogroup.html', name=name,error="Invalid groupname")
    else:
        gid = a[0]
    cursor.execute(("select * from user_group where (user_id='{}' and group_id='{}');".format(uid,gid)))
    a = cursor.fetchone()
    if a:
        return render_template('addtogroup.html', name=name,error="User is already part of group!")
    cursor.execute(("insert into user_group values('{}','{}');".format(uid,gid)))
    cursor.execute(("commit;"))
    return render_template('addtogroup.html', name=name)

@app.route('/teamvsteam.html', methods=['POST','GET'])
def tvst(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    c = 0
    rows = []
    t1 = t2 = ""
    if request.method == 'POST':
        t1 = request.form['t1']
        t2 = request.form['t2']
        if not t1 or not t2:
            return render_template('teamvsteam.html', name=name, rows = rows, count = c, name1 = t1, name2 = t2, error="Enter both names!")
        cursor.execute(("select team_id from team where name='{}'".format(t1)))
        a = cursor.fetchone()
        if not a:
            return render_template('teamvsteam.html', name=name, rows = rows, count = c, name1 = t1, name2 = t2, error="Invalid team1 name")
        else:
            t1i = a[0]
        cursor.execute(("select team_id from team where name='{}'".format(t2)))
        a = cursor.fetchone()
        if not a:
            return render_template('teamvsteam.html', name=name, rows = rows, count = c, name1 = t1, name2 = t2, error="Invalid team2 name")
        else:
            t2i = a[0]
        cursor.execute(("select match_id from matches where ((team1_id={} and team2_id={}) or (team1_id={} and team2_id={}))".format(t1i, t2i, t2i, t1i)))
        cur = cursor.fetchall()
        print(cur)
        for i in cur:
            cursor.execute(("select * from match_team_performance where match_id = {}".format(int(i[0]))))
            row = [j for j in cursor]
            rows.append(row)
            c += 1
    return render_template('teamvsteam.html', name=name, rows = rows, count = c, name1 = t1, name2 = t2)

@app.route('/playerground.html', methods=['POST','GET'])
def playerground(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    name = p1= c1 =""
    bat = bowl = []
    if request.method == 'POST':
        p1 = request.form['p1']
        c1 = request.form['c1']
        if not p1 or not c1:
            return render_template('playerground.html', name=name, bat = bat, bowl = bowl, nam = p1, error="Enter both values")
        cursor.execute(("select ground_id from ground where city='{}'".format(c1)))
        a = cursor.fetchone()
        if not a:
            return render_template('playerground.html', name=name, bat = bat, bowl = bowl, nam = p1, error="Invalid city name")
        else:
            gid = a[0]
        cursor.execute(("select player_id from player where name='{}'".format(p1)))
        a = cursor.fetchone()
        if not a:
            return render_template('playerground.html', name=name, bat = bat, bowl = bowl, nam = p1, error="Invalid city name")
        else:
            pid = a[0]
        cursor.execute(("select * from match_player_bat where player_id={} and match_id in (select match_id from matches where ground_id = {})".format(pid, gid)))
        bat = [i for i in cursor]
        cursor.execute(("select * from match_player_bowl where player_id={} and match_id in (select match_id from matches where ground_id = {})".format(pid, gid)))
        bowl = [i for i in cursor]
    return render_template('playerground.html', name=name, bat = bat, bowl = bowl, nam = p1)

@app.route('/playerteam.html', methods=['POST','GET'])
def playerteam(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    name = p1= t1 =""
    bat = bowl = []
    if request.method == 'POST':
        p1 = request.form['p1']
        t1 = request.form['t1']
        if not p1 or not t1:
            return render_template('playerteam.html', name=name, bat = bat, bowl = bowl, pname = p1, error="Enter both values")
        cursor.execute(("select team_id from team where name='{}'".format(t1)))
        a = cursor.fetchone()
        if not a:
            return render_template('playerteam.html', name=name, bat = bat, bowl = bowl, pname = p1, error="Invalid team name")
        else:
            tid = a[0]
        cursor.execute(("select player_id from player where name='{}'".format(p1)))
        a = cursor.fetchone()
        if not a:
            return render_template('playerteam.html', name=name, bat = bat, bowl = bowl, pname = p1, error="Invalid player name")
        else:
            pid = a[0]
        cursor.execute(("select * from match_player_bat where player_id={} and match_id in (select match_id from matches where team1_id = {} or team2_id = {})".format(pid, tid, tid)))
        bat = [i for i in cursor]
        cursor.execute(("select * from match_player_bowl where player_id={} and match_id in (select match_id from matches where team1_id = {} or team2_id = {})".format(pid, tid, tid)))
        bowl = [i for i in cursor]
    return render_template('playerteam.html', name=name, bat = bat, bowl = bowl, pname = p1)

@app.route('/playerall.html', methods=['POST','GET'])
def playerall(name=None):
    global user_id 
    if login_needed:
        if not user_id:
            return render_template('login.html', name=name)
    name = p1 = ""
    bat = []
    bowl = []
    if request.method == 'POST':
        p1 = request.form['p1']
        if not p1:
            return render_template('playerall.html', name=name, bat = bat, bowl = bowl, pname = p1, error="Enter player name")
        cursor.execute(("select player_id from player where name='{}'".format(p1)))
        a = cursor.fetchone()
        if not a:
            return render_template('playerall.html', name=name, bat = bat, bowl = bowl, pname = p1, error="Invalid player name")
        else:
            pid = a[0]
        cursor.execute(("select team2_id from matches where team1_id=(select team_id from player where player_id = {})".format(pid)))
        tids = [str(i)[1] for i in cursor]
        cursor.execute(("select team1_id from matches where team2_id=(select team_id from player where player_id = {})".format(pid)))
        for i in cursor:
            tids.append(int(str(i)[1]))
        tn = []
        for i in tids:
            cursor.execute(("select name from team where team_id = {}".format(i)))
            a = cursor.fetchone()
            tn.append(str(a[0]))
        cursor.execute(("select * from match_player_bat where player_id={}".format(pid)))
        j = 0
        for i in cursor:
            i = i + (tn[j],)
            j += 1
            bat.append(i)
        cursor1.execute(("select * from match_player_bowl where player_id={}".format(pid)))
        j = 0
        for i in cursor1:
            i = i + (tn[j],)
            j += 1
            bowl.append(i)
    return render_template('playerall.html', name=name, bat = bat, bowl = bowl, pname = p1)

@app.route('/groups.html', methods=['POST','GET'])
def groups(name=None):
    global user_id 
    cursor.execute(("select groupname from groups where group_id in (select group_id from user_group where user_id = {})".format(user_id)))
    groups = [str(i)[3:-3] for i in cursor]
    return render_template('groups.html', name=name, groups = groups)

@app.route('/faq.html')
def faq(name=None):
    return render_template('faq.html', name=name)
