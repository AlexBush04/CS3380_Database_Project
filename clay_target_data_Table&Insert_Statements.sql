CREATE SCHEMA clay_target_data;

CREATE TABLE clay_target_data.TEAM
	(Team_ID			char(9)			NOT NULL,
     Name				varchar(20)		NOT NULL,
     Location			varchar(25),
     PRIMARY KEY(Team_ID));
    
CREATE TABLE clay_target_data.ATHLETE
	(Athlete_ID			char(10)		NOT NULL,
     Name				varchar(20)		NOT NULL,
     Grade_level		INT CHECK(Grade_level >= 4 AND Grade_level <= 12)	NOT NULL,
	 Team_ID			char(9)			DEFAULT NULL,
     PRIMARY KEY(Athlete_ID),
     FOREIGN KEY(Team_ID) REFERENCES TEAM(Team_ID)
		ON DELETE SET NULL	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.COACH
	(Certification_no	char(10)		NOT NULL,
     Name				varchar(20)		NOT NULL,
     Start_date			DATE			DEFAULT NULL,
     Team_ID			char(9)			DEFAULT NULL,
     PRIMARY KEY(Certification_no),
     FOREIGN KEY(Team_ID) REFERENCES TEAM(Team_ID)
		ON DELETE SET NULL	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.AREA_OF_EXPERTISE
	(Cert_no			char(10)		NOT NULL,
     Expertise			ENUM('trap', 'skeet', 'sporting clays')	NOT NULL,
     PRIMARY KEY(Cert_no, Expertise),
     FOREIGN KEY(Cert_no) REFERENCES COACH(Certification_no)
		ON DELETE CASCADE 	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.WORKS_WITH
	(Ath_ID				char(10)		NOT NULL,
     Cert_no			char(10)		NOT NULL,
	 Start_date			date			NOT NULL,
     PRIMARY KEY(Ath_ID, Cert_no),
     FOREIGN KEY(Ath_ID) REFERENCES ATHLETE(Athlete_ID)
		ON DELETE CASCADE	ON UPDATE CASCADE,
	 FOREIGN KEY(Cert_no) REFERENCES COACH(Certification_no)
		ON DELETE CASCADE	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.TRAP_SCORE
	(Ath_ID				char(10)		NOT NULL,
     Date				DATE 			NOT NULL,
     Round_no			INT 			NOT NULL,
     Type				ENUM('practice', 'competition')			NOT NULL,
     Location			varchar(25)								DEFAULT NULL,
     Score				INT CHECK (Score >= 0 AND Score <= 25)	NOT NULL,
     Sta_1				INT CHECK (Sta_1 >=0 AND Sta_1 <= 5)	NOT NULL,
     Sta_2				INT	CHECK (Sta_2 >=0 AND Sta_2 <= 5)	NOT NULL,
     Sta_3				INT	CHECK (Sta_3 >=0 AND Sta_3 <= 5)	NOT NULL,
     Sta_4				INT CHECK (Sta_4 >=0 AND Sta_4 <= 5)	NOT NULL,
     Sta_5				INT CHECK (Sta_5 >=0 AND Sta_5 <= 5)	NOT NULL,
     PRIMARY KEY(Ath_ID, Date, Round_no),
     FOREIGN KEY(Ath_ID) REFERENCES ATHLETE(Athlete_ID)
		ON DELETE CASCADE	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.SKEET_SCORE
	(Ath_ID				char(10)		NOT NULL,
     Date				DATE 			NOT NULL,
     Round_no			INT 			NOT NULL,
     Type				ENUM('practice', 'competition')			NOT NULL,
     Location			varchar(25)								DEFAULT NULL,
     Score				INT CHECK (Score >= 0 AND Score <= 25)	NOT NULL,
     Sta_1				INT CHECK (Sta_1 >=0 AND Sta_1 <= 5)	NOT NULL,
     Sta_2				INT CHECK (Sta_2 >=0 AND Sta_2 <= 5)	NOT NULL,
     Sta_3				INT CHECK (Sta_3 >=0 AND Sta_3 <= 3)	NOT NULL,
     Sta_4				INT CHECK (Sta_4 >=0 AND Sta_4 <= 3)	NOT NULL,
     Sta_5				INT CHECK (Sta_5 >=0 AND Sta_5 <= 3)	NOT NULL,
     Sta_6				INT CHECK (Sta_6 >=0 AND Sta_6 <= 5)	NOT NULL,
     Sta_7				INT CHECK (Sta_7 >=0 AND Sta_7 <= 5)	NOT NULL,
     Sta_8				INT	CHECK (Sta_8 >=0 AND Sta_8 <= 3)	NOT NULL,
     PRIMARY KEY(Ath_ID, Date, Round_no),
     FOREIGN KEY(Ath_ID) REFERENCES ATHLETE(Athlete_ID)
		ON DELETE CASCADE	ON UPDATE CASCADE);

CREATE TABLE clay_target_data.SPORTING_CLAYS_SCORE
	(Ath_ID				char(10)		NOT NULL,
     Date				DATE 			NOT NULL,
     No_stations		INT				NOT NULL,
     Type				ENUM('practice', 'competition')			NOT NULL,
     Location			varchar(25)								DEFAULT NULL,
     Score				INT CHECK(Score >=0 AND Score <= 100)	NOT NULL,
     PRIMARY KEY(Ath_ID, Date),
     FOREIGN KEY(Ath_ID) REFERENCES ATHLETE(Athlete_ID)
		ON DELETE CASCADE	ON UPDATE CASCADE);
        
INSERT INTO clay_target_data.TEAM
	VALUES("1234-5678","Central Falcons","Bristol, WI"),
			("2222-3333","Wilmot Shotgun Team","Wilmot, WI"),
            ("2424-5959","Waterford Shotgun","Waterford, WI"),
            ("9876-5432","Burlington Gun Club","Burlington, WI"),
            ("2468-1359","Union Grove","Union Grove, WI"),
            ("3690-4812","Badger Shotgun Team","Lake Geneva, WI");

INSERT INTO clay_target_data.ATHLETE
	VALUES("1234-67890","J.B. Mauney","7","1234-5678"),
			("1738-19510","Kacy Peters","8","1234-5678"),
            ("2222-33333","John Doe","9","1234-5678"),
            ("4444-55555","Alfred Pennyworth","12","1234-5678"),
            ("6666-77777","Bruce Wayne","10","1234-5678"),
            ("8888-99999","Clark Kent","10","1234-5678"),
			("9876-54321","Quincey Jones","12","2424-5959"),
            ("4812-51015","Brett Parker","6","2222-3333");

INSERT INTO clay_target_data.ATHLETE(Athlete_ID, Name, Grade_level)
	VALUES ("2468-36912","Johny B Good","9"),
			("8229-93167","Noah Kahn","11");

INSERT INTO clay_target_data.COACH
	VALUES("1111-99999","Roger Doss","2018-02-10","1234-5678"),
			("2222-88888","Alan Bob","2017-01-26","2222-3333"),
            ("3333-77777","Willie Kringle","2022-03-16","2424-5959"),
            ("4444-66666","Gene Wilder","2015-04-22","9876-5432"),
            ("5555-55555","Percy Jackson","2024-01-16","2468-1359"),
            ("1928-37465","Larry Lobster","2025-02-14","3690-4812");
    
INSERT INTO clay_target_data.AREA_OF_EXPERTISE
	VALUES("1111-99999","trap"),
			("2222-88888","trap"),
            ("2222-88888","skeet"),
            ("4444-66666","sporting clays"),
            ("1928-37465","trap");
    
INSERT INTO clay_target_data.WORKS_WITH
	VALUES("4444-55555","2222-88888","2023-03-01"),
			("8888-99999","4444-66666","2022-05-01"),
            ("2222-33333","1111-99999","2024-02-15");
    
INSERT INTO clay_target_data.TRAP_SCORE
	VALUES("2222-33333","2026-05-01","1","practice","Bristol","25","5","5","5","5","5"),
			("2222-33333","2026-04-01","1","competition","Burlington","24","5","5","5","4","5"),
            ("2222-33333","2025-05-01","1","competition","Burlington","23","5","5","5","4","4"),
            ("2222-33333","2025-04-01","1","practice","Northrook","23","5","5","3","5","5"),
            ("2222-33333","2024-05-01","1","practice","Winchester","21","4","4","5","4","4"),
            ("2222-33333","2024-04-01","1","competition","Bristol","22","5","5","5","3","4"),
            ("2222-33333","2023-05-01","1","practice","Beaver Damn","20","4","4","4","4","4"),
            ("2222-33333","2022-05-01","1","competition","Waukesha","18","4","4","4","4","3"),
            ("2222-33333","2021-05-01","1","practice","Bristol","12","2","3","3","2","2");
INSERT INTO clay_target_data.TRAP_SCORE
	VALUES("1234-67890","2026-05-01","1","practice","Bristol","25","5","5","5","5","5"),
			("1738-19510","2026-05-01","1","practice","Bristol","24","5","5","5","5","4"),
            ("4444-55555","2026-05-01","1","practice","Bristol","23","5","5","5","4","4"),
            ("6666-77777","2026-05-01","1","practice","Bristol","22","5","5","4","4","4"),
            ("8888-99999","2026-05-01","1","practice","Bristol","21","5","4","4","4","4");
    
INSERT INTO clay_target_data.SKEET_SCORE
	VALUES("4444-55555","2026-05-01","1","practice","Burlington","25","4","4","2","2","2","4","4","3"),
			("4444-55555","2026-04-01","1","practice","Bristol","25","4","4","2","2","2","4","4","3"),
            ("4444-55555","2025-05-01","1","practice","Waukesha","24","4","4","2","2","2","4","4","2"),
            ("4444-55555","2024-05-01","1","practice","Northbrook","23","4","4","2","2","2","3","4","2"),
            ("4444-55555","2024-04-01","1","practice","Northbrook","24","4","4","2","2","2","4","4","2"),
            ("4444-55555","2023-05-01","1","practice","Burlington","22","4","4","1","1","2","5","4","1"),
            ("4444-55555","2023-04-01","1","practice","Bristol","21","4","3","1","1","2","4","4","2"),
            ("4444-55555","2022-05-01","1","practice","Winchester","20","4","4","1","1","1","3","4","2"),
            ("4444-55555","2021-05-01","1","practice","Winchester","18","4","2","1","2","1","2","4","2"),
            ("4444-55555","2020-05-01","1","practice","Waukesha","17","4","2","1","1","1","2","4","2"),
            ("4444-55555","2019-05-01","1","practice","Bristol","15","3","2","1","1","1","2","4","1");
INSERT INTO clay_target_data.SKEET_SCORE
	VALUES("1234-67890","2026-05-01","1","practice","Bristol","25","4","4","2","2","2","4","4","3"),
			("1738-19510","2026-05-01","1","practice","Bristol","24","4","4","2","2","2","4","4","2"),
            ("2222-33333","2026-05-01","1","practice","Bristol","23","4","4","2","2","2","4","3","2"),
            ("6666-77777","2026-05-01","1","practice","Bristol","22","4","4","2","2","2","3","3","2"),
            ("8888-99999","2026-05-01","1","practice","Bristol","21","4","4","2","2","1","3","3","2");
    
INSERT INTO clay_target_data.SPORTING_CLAYS_SCORE
	VALUES("8888-99999","2026-05-01","14","practice","Northbrook","88"),
			("8888-99999","2024-05-01","12","competition","Manitowoc","90"),
            ("8888-99999","2023-05-01","16","practice","Northbrook","85"),
            ("8888-99999","2022-05-01","18","competition","Wern Valley","80"),
            ("8888-99999","2021-05-01","13","practice","Northbrook","75"),
            ("8888-99999","2020-05-01","15","competition","Manitowoc","72");
INSERT INTO clay_target_data.SPORTING_CLAYS_SCORE
	VALUES("1234-67890","2026-05-01","14","practice","Northbrook","85"),
			("1738-19510","2026-05-01","14","practice","Northbrook","82"),
            ("2222-33333","2026-05-01","14","practice","Northbrook","80"),
            ("6666-77777","2026-05-01","14","practice","Northbrook","78"),
            ("4444-55555","2026-05-01","14","practice","Northbrook","76");