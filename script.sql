drop table if exists VideoGames;
drop table if exists library;
drop table if exists users;


CREATE TABLE VideoGames (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    producer VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    release_date DATE
);

CREATE TABLE library (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   user_id INTEGER NOT NULL,
   game_id INTEGER NOT NULL,
   status TEXT
);

CREATE TABLE  users (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   surname TEXT NOT NULL,
   email TEXT NOT NULL UNIQUE,
   salt TEXT NOT NULL,
   password TEXT NOT NULL
);

INSERT INTO VideoGames (id, name, producer, genre, release_date)
VALUES
    (1, 'The Legend of Zelda: Breath of the Wild', 'Nintendo', 'Action-adventure', '03-03-2017'),
            (2, 'Red Dead Redemption 2', 'Rockstar Games', 'Action-adventure', '26-10-2018'),
            (3, 'Fortnite', 'Epic Games', 'Battle royale', '25-07-2017'),
            (4, 'Grand Theft Auto V', 'Rockstar Games', 'Action-adventure', '17-09-2013'),
            (5, 'Minecraft', 'Mojang Studios', 'Sandbox', '18-11-2011'),
            (6, 'The Witcher 3: Wild Hunt', 'CD Projekt', 'Action role-playing', '19-05-2015'),
            (7, 'Overwatch', 'Blizzard Entertainment', 'First-person shooter', '24-05-2016'),
            (8, 'Super Mario Odyssey', 'Nintendo', 'Platformer', '27-10-2017'),
            (9, 'Call of Duty: Modern Warfare', 'Activision', 'First-person shooter', '25-10-2019'),
            (10, 'FIFA 21', 'EA Sports', 'Sports', '09-10-2020'),
            (11, 'Assassin s Creed Valhalla', 'Ubisoft', 'Action role-playing', '10-11-2020'),
            (12, 'Cyberpunk 2077', 'CD Projekt', 'Action role-playing', '10-12-2020'),
            (13, 'Super Smash Bros. Ultimate', 'Nintendo', 'Fighting', '07-12-2018'),
            (14, 'God of War', 'Santa Monica Studio', 'Action-adventure', '20-04-2018'),
            (15, 'Animal Crossing: New Horizons', 'Nintendo', 'Life simulation', '20-03-2020'),
            (16, 'Halo: Combat Evolved', 'Bungie', 'First-person shooter', '15-11-2001'),
            (17, 'World of Warcraft', 'Blizzard Entertainment', 'MMORPG', '23-11-2004'),
            (18, 'Pokémon Sword and Shield', 'Game Freak', 'Role-playing', '15-11-2019'),
            (19, 'Battlefield 1', 'EA DICE', 'First-person shooter', '21-10-2016'),
            (20, 'Super Mario 64', 'Nintendo', 'Platformer', '23-06-1996'),
            (21, 'Uncharted 4: A Thiefs End', 'Naughty Dog', 'Action-adventure', '10-05-2016'),
            (22, 'Final Fantasy VII Remake', 'Square Enix', 'Role-playing', '10-04-2020'),
            (23, 'The Last of Us Part II', 'Naughty Dog', 'Action-adventure', '19-06-2020'),
            (24, 'Gears of War', 'Epic Games', 'Third-person shooter', '07-11-2006'),
            (25, 'World of Tanks', 'Wargaming', 'Tank simulation', '12-08-2010'),
            (26, 'Resident Evil 2', 'Capcom', 'Survival horror', '25-01-2019'),
            (27, 'Super Mario World', 'Nintendo', 'Platformer', '21-11-1990'),
            (28, 'The Elder Scrolls V: Skyrim', 'Bethesda Game Studios', 'Action role-playing', '11-11-2011'),
            (29, 'BioShock', '2K Games', 'First-person shooter', '21-08-2007'),
            (30, 'Metal Gear Solid V: The Phantom Pain', 'Konami', 'Action-adventure', '01-09-2015'),
            (31, 'League of Legends', 'Riot Games', 'MOBA', '27-10-2009'),
            (32, 'Doom', 'id Software', 'First-person shooter', '10-12-1993'),
            (33, 'Persona 5', 'Atlus', 'Role-playing', '15-09-2016'),
            (34, 'Mortal Kombat 11', 'NetherRealm Studios', 'Fighting', '23-04-2019'),
            (35, 'Splatoon 2', 'Nintendo', 'Third-person shooter', '21-07-2017'),
            (36, 'StarCraft II: Wings of Liberty', 'Blizzard Entertainment', 'Real-time strategy', '27-07-2010'),
            (37, 'Half-Life 2', 'Valve Corporation', 'First-person shooter', '16-11-2004'),
            (38, 'Diablo III', 'Blizzard Entertainment', 'Action role-playing', '15-05-2012'),
            (39, 'Pokémon Go', 'Niantic', 'Augmented reality', '06-07-2016'),
            (40, 'Super Metroid', 'Nintendo', 'Action-adventure', '19-03-1994'),
            (41, 'Mass Effect 2', 'BioWare', 'Action role-playing', '26-01-2010'),
            (42, 'The Sims 4', 'Maxis', 'Life simulation', '02-09-2014'),
            (43, 'Street Fighter II', 'Capcom', 'Fighting', '06-02-1991'),
            (44, 'The Legend of Zelda: Ocarina of Time', 'Nintendo', 'Action-adventure', '23-11-1998'),
            (45, 'Counter-Strike: Global Offensive', 'Valve Corporation', 'First-person shooter', '21-08-2012'),
            (46, 'The Last of Us', 'Naughty Dog', 'Action-adventure', '14-06-2013'),
            (47, 'Kingdom Hearts III', 'Square Enix', 'Action role-playing', '29-01-2019'),
            (48, 'Grand Theft Auto: San Andreas', 'Rockstar Games', 'Action-adventure', '26-10-2004'),
            (49, 'Portal', 'Valve Corporation', 'Puzzle-platform', '10-10-2007'),
            (50, 'Batman: Arkham City', 'Rocksteady Studios', 'Action-adventure', '18-10-2011'),
            (51, 'Tom Clancys Rainbow Six Siege', 'Ubisoft', 'First-person shooter', '01-12-2015'),
            (52, 'The Sims', 'Maxis', 'Life simulation', '04-02-2000'),
            (53, 'God of War (2018)', 'Santa Monica Studio', 'Action-adventure', '20-04-2018'),
            (54, 'Pokémon Red and Blue', 'Game Freak', 'Role-playing', '27-02-1996'),
            (55, 'The Legend of Zelda: A Link to the Past', 'Nintendo', 'Action-adventure', '21-11-1991'),
            (56, 'Rocket League', 'Psyonix', 'Sports', '07-07-2015'),
            (57, 'Super Smash Bros. Melee', 'Nintendo', 'Fighting', '21-11-2001'),
            (58, 'Horizon Zero Dawn', 'Guerrilla Games', 'Action role-playing', '28-02-2017'),
            (59, 'Fire Emblem: Three Houses', 'Intelligent Systems', 'Tactical role-playing', '26-07-2019'),
            (60, 'BioShock Infinite', 'Irrational Games', 'First-person shooter', '26-03-2013'),
            (61, 'Tetris', 'Various', 'Puzzle', '06-06-1984'),
            (62, 'Resident Evil 4', 'Capcom', 'Survival horror', '11-01-2005'),
            (63, 'Civilization VI', 'Firaxis Games', 'Turn-based strategy', '21-10-2016'),
            (64, 'Super Mario Bros.', 'Nintendo', 'Platformer', '13-09-1985'),
            (65, 'The Legend of Zelda: Link s Awakening', 'Nintendo', 'Action-adventure', '06-06-1993'),
            (66, 'Far Cry 5', 'Ubisoft', 'First-person shooter', '27-03-2018'),
            (67, 'FIFA 20', 'EA Sports', 'Sports', '27-09-2019'),
            (68, 'Final Fantasy X', 'Square', 'Role-playing', '19-07-2001'),
            (69, 'The Sims 3', 'Maxis', 'Life simulation', '02-06-2009'),
            (70, 'Stardew Valley', 'ConcernedApe', 'Simulation', '26-02-2016'),
            (71, 'Bioshock 2', '2K Marin', 'First-person shooter', '09-02-2010'),
            (72, 'Undertale', 'Toby Fox', 'Role-playing', '15-09-2015'),
            (73, 'Super Mario Galaxy', 'Nintendo', 'Platformer', '01-11-2007'),
            (74, 'World of Warcraft: The Burning Crusade', 'Blizzard Entertainment', 'MMORPG', '16-01-2007'),
            (75, 'Deus Ex', 'Ion Storm', 'Action role-playing', '23-06-2000'),
            (76, 'Metroid Prime', 'Retro Studios', 'Action-adventure', '17-11-2002'),
            (77, 'Resident Evil', 'Capcom', 'Survival horror', '22-03-1996'),
            (78, 'Crash Bandicoot', 'Naughty Dog', 'Platformer', '09-09-1996'),
            (79, 'Super Mario Kart', 'Nintendo', 'Racing', '27-08-1992'),
            (80, 'Mass Effect', 'BioWare', 'Action role-playing', '16-11-2007'),
            (81, 'The Legend of Zelda: Majoras Mask', 'Nintendo', 'Action-adventure', '27-04-2000'),
            (82, 'Final Fantasy VI', 'Square', 'Role-playing', '02-04-1994'),
            (83, 'Resident Evil 3', 'Capcom', 'Survival horror', '22-09-1999'),
            (84, 'Dark Souls', 'FromSoftware', 'Action role-playing', '22-09-2011'),
            (85, 'Mass Effect 3', 'BioWare', 'Action role-playing', '06-03-2012'),
            (86, 'The Legend of Zelda: Skyward Sword', 'Nintendo', 'Action-adventure', '18-11-2011'),
            (87, 'Diablo II', 'Blizzard Entertainment', 'Action role-playing', '29-06-2000'),
            (88, 'Mortal Kombat X', 'NetherRealm Studios', 'Fighting', '14-04-2015'),
            (89, 'Resident Evil 7: Biohazard', 'Capcom', 'Survival horror', '24-01-2017'),
            (90, 'The Sims 2', 'Maxis', 'Life simulation', '14-09-2004'),
            (91, 'Civilization V', 'Firaxis Games', 'Turn-based strategy', '21-09-2010'),
            (92, 'The Legend of Zelda: The Wind Waker', 'Nintendo', 'Action-adventure', '13-12-2002'),
            (93, 'Crash Bandicoot: Warped', 'Naughty Dog', 'Platformer', '31-10-1998'),
            (94, 'Donkey Kong Country', 'Rare', 'Platformer', '21-11-1994'),
            (95, 'Final Fantasy IX', 'Square', 'Role-playing', '07-07-2000'),
            (96, 'Mega Man 2', 'Capcom', 'Platformer', '24-12-1988'),
            (97, 'Assassins Creed II', 'Ubisoft', 'Action-adventure', '17-11-2009'),
            (98, 'Star Wars Jedi: Fallen Order', 'Respawn Entertainment', 'Action-adventure', '15-11-2019'),
            (99, 'Grand Theft Auto IV', 'Rockstar Games', 'Action-adventure', '29-04-2008'),
            (100, 'World of Warcraft: Wrath of the Lich King', 'Blizzard Entertainment', 'MMORPG', '13-11-2008');
