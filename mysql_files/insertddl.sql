insert into dismissal values (1, 'caught');
insert into dismissal (dismissal_name) values ('caught');
update dismissal set dismissal_name='bowled' where dismissal_id = 1;
insert into dismissal (dismissal_name) values ('run out');
insert into dismissal (dismissal_name) values ('hit wicket');
insert into dismissal (dismissal_name) values ('obs.field');
insert into dismissal (dismissal_name) values ('stumped');

insert into ground values (1, 'Wankhede Stadium', 'Mumbai', 'India', 30000);
insert into ground values (2, 'Gahunje Stadium MCA', 'Pune', 'India', 25000);
insert into ground values (3, 'Feroz Shah Kotla', 'New Delhi', 'India', 31000);
insert into ground values (4, 'Eden Gardens', 'Kolkata', 'India', 50000);
insert into ground values (5, 'Chidambaram Stadium', 'Chennai', 'India', 20000);
insert into ground values (6, 'Braborne Stadium', 'Mumbai', 'India', 22000);
insert into ground values (7, 'Green Park Stadium', 'Kanpur', 'India', 25000);
insert into ground values (8, 'Chinnaswamy Stadium', 'Bengaluru', 'India', 23000);
insert into ground values (10, 'Sawai Mansingh Stadium', 'Bengaluru', 'India'
insert into ground values (11, 'Punjab CA Stadium', 'Bengaluru', 'India', 27000);
insert into ground values (9, 'Sardar Patel Stadium', 'Bengaluru', 'India', 23000);
insert into ground values (12, 'Vidarbha CA Stadium', 'Nagpur', 'India', 24000);
update ground set city='Ahemdabad' where ground_id = 9;
update ground set city='Jaipur' where ground_id = 10;
update ground set city='Chandigarh' where ground_id = 11;
insert into ground values (13, 'Saurashtra CA', 'Rajkot', 'India', 20000);

insert into ground values (14, 'Melbourne CG', 'Melbourne', 'Australia', 75000);
insert into ground values (15, 'Sydney Cricket', 'Sydney', 'Australia', 60000);
insert into ground values (16, 'WACA Stadium', 'Perth', 'Australia', 40000);
insert into ground values (17, 'Gabba Stadium', 'Brisbane', 'Australia', 50000);
insert into ground values (18, 'Adelaide CG', 'Adelaide', 'Australia', 45000);
insert into ground values (19, 'Blundstone Arena', 'Hobart', 'Australia', 25000);

insert into ground values (20, 'The Oval', 'London', 'England', 45000);
insert into ground values (21, 'Old Trafford', 'Manchester', 'England', 40000);
insert into ground values (22, 'Lords', 'London', 'England', 50000);
insert into ground values (23, 'Trent Bridge', 'Nottingham', 'England', 30000);
insert into ground values (24, 'Headingly', 'Leeds', 'England', 35000);
insert into ground values (25, 'Edgabaston', 'Birmingham', 'England', 42000);
insert into ground values (26, 'Rose Bowl', 'Southamton', 'England', 35000);
insert into ground values (27, 'SuperSport Park', 'Centurion', 'RSA', 15000);
insert into ground values (28, 'Buffalo Park', 'E London', 'RSA', 12000);
insert into ground values (29, 'Newlands', 'Cape Town', 'RSA', 10000);
insert into ground values (30, 'Old Wanderers', 'Johnesburg', 'RSA', 20000);
insert into ground values (31, 'AMI Stadium', 'Christcurch', 'New Zealand', 25000);
insert into ground values (32, 'Basin Reserve', 'Wellington', 'NewZealand', 30000);

insert into ground values (33, 'Craisbrook', 'Dunedin', 'NewZealand', 27000);
insert into ground values (34, 'Kensington Oval', 'Bridgetown', 'WestIndies', 10000);
insert into ground values (35, 'Boruda', 'Guyana', 'WestIndies', 8000);
insert into ground values (36, 'Sabina Park', 'Kingston', 'WestIndies', 13000);
insert into ground values (37, 'Asgiriya Stadium', 'Kandy', 'Sri Lanka', 5000);
insert into ground values (38, 'Colombo Cricket', 'Colombo', 'Sri Lanka', 6000);
insert into ground values (39, 'Dubai International', 'Dubai', 'UAE', 26000);
insert into ground values (40, 'Sharjah Cricket', 'Sharjah', 'UAE', 35000);
insert into ground values (41, 'Uppal', 'Hyderabad', 'India', 40000);

insert into team values (1, 'MI', 14, 10, 20);
insert into team values (2, 'RPS', 14, 9, 18);
insert into team values (3, 'SRH', 14, 8, 17);
insert into team values (4, 'KKR', 14, 8, 16);
insert into team values (5, 'KP', 14, 7, 14);
insert into team values (6, 'DD', 14, 6, 12);
insert into team values (7, 'GL', 14, 4, 8);
insert into team values (8, 'RCB', 14, 3, 7);
