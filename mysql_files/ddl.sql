DROP TABLE match_team_performance;
DROP TABLE match_player_bat;
DROP TABLE match_player_bowl;
DROP TABLE dismissal;
DROP TABLE player;
DROP TABLE user_group;
DROP TABLE matches;
DROP TABLE groups;
DROP TABLE team;
DROP TABLE users;
DROP TABLE ground;
DROP TABLE userplayer;


CREATE TABLE users(                                                 
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(20) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	favteam VARCHAR(20) NOT NULL,                          
	username VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL,
	budget INT NOT NULL,
	points INT NOT NULL
);

CREATE TABLE team(
	team_id INT,
	name VARCHAR(30) NOT NULL,
	win_year VARCHAR(30),
	owner VARCHAR(50),
	coach VARCHAR(30),
	venue VARCHAR(530),
	captain VARCHAR(30),
	PRIMARY KEY(team_id)
);

CREATE TABLE player(
	player_id INT AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	team_id INT NOT NULL,
	batstyle VARCHAR(5) NOT NULL,
	matches INT,
	runs INT,
	highest_score INT,
	average FLOAT,
	strike_rate FLOAT,
	hundreds INT,
	fifties INT,
	fours INT,
	sixes INT,
	wickets INT,
	eco FLOAT,
	fourhaul INT,
	fivehaul INT,
	price INT,
	PRIMARY KEY(player_id),
	FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE groups(
	group_id INT PRIMARY KEY AUTO_INCREMENT,
	groupname VARCHAR(20) NOT NULL
);

CREATE TABLE user_group(
	user_id INT,
	group_id INT,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE
);

CREATE TABLE dismissal(
	dismissal_id INT PRIMARY KEY,
	dismissal_name VARCHAR(10)
);

CREATE TABLE ground(
	ground_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	city VARCHAR(20) NOT NULL,
	country VARCHAR(20) NOT NULL,
	capacity INT
);

CREATE TABLE matches(
	match_id INT PRIMARY KEY AUTO_INCREMENT,
	team1_id INT,
	team2_id INT,
	ground_id INT,
	dates DATE,
	toss INT,
	batfirst INT,
	team_won INT,
	MoM INT,
	FOREIGN KEY (team1_id) REFERENCES team(team_id),
	FOREIGN KEY (team2_id) REFERENCES team(team_id),
	FOREIGN KEY (ground_id) REFERENCES ground (ground_id)
);

CREATE TABLE match_team_performance(
	match_id INT,
	team_id INT,
	tot_runs INT,
	tot_wickets INT,
	overs_played INT,
	wides INT,
	noballs INT,
	byes INT,
	legbyes INT,
	PRIMARY KEY (match_id, team_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE match_player_bowl(
	player_id INT,
	match_id INT,
	overs INT,
	maidens INT,
	runs INT,
	wickets INT,
	ECO FLOAT,
	wides INT,
	noballs INT,
	PRIMARY KEY (player_id, match_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player(player_id)
);

CREATE TABLE match_player_bat(
	player_id INT,
	match_id INT,
	runs INT,
	balls INT,
	fours INT,
	sixes INT,
	strike_rate FLOAT,	
	dismissal_id INT,
	dismissal_assist INT,
	bowler INT,
	isout INT,
	PRIMARY KEY (player_id, match_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player(player_id),
	FOREIGN KEY (dismissal_id) REFERENCES dismissal (dismissal_id)
);

create table userplayer (user_id INT, player_id INT, primary key (user_id, player_id), foreign key (player_id) references player(player_id) on delete cascade, foreign key (user_id) references users(user_id) on delete cascade);

