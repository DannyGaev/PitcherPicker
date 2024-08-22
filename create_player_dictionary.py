import requests
from requests.exceptions import ConnectionError
import threading
import time
import argparse
import datetime
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *

player_dict = {}

def main(file_name='',names=False):
    if file_name=='':
        file_name = 'player_dictionary'
    print(f"\n[>] Player dictionary will be saved to: {file_name}\n")
    time.sleep(2)

    player_names = ['Brennan Bernardino', 'Shane Bieber', 'Hunter Bigge', 'Ryan Brasier', 'Josh Fleming', 'Brenan Hanifee', 'Brent Honeywell', 'Brandon Hughes', 'Kyle Hurt', 'Ben Joyce', 'Zack Kelly', 'Orion Kerkering', 'Jared Koenig', 'Chad Kuhl', 'Luke Little', 'Anthony Maldonado', 'Steven Okert', 'Emilio Pagán', 'Trevor Richards', 'Tony Santillan', 'Tayler Scott', 'AJ Smith-Shawver', 'Brent Suter', 'Jacob Waguespack', 'Ryan Walker', 'Tyler Holton', 'Erik Miller', 'Michael McGreevy', 'River Ryan', 'Matthew Boyd', 'Spencer Turnbull', 'Spencer Bivens', 'Garrett Whitlock', 'Blake Walston', 'Bryan Woo', 'Reynaldo López', 'Carmen Mlodzinski', 'Cody Poteet', 'Trevor Williams', 'Joan Adon', 'Shawn Armstrong', 'Jakob Junis', 'Paul Skenes', 'Cody Bradford', 'Josh Winckowski', 'Valente Bellozo', 'Gerson Garabito', 'Tarik Skubal', 'Clarke Schmidt', 'Robert Gasser', 'John Means', 'Chris Sale', 'Clayton Kershaw', 'Alex Faedo', 'Rob Zastryzny', 'Landon Knack', 'Zack Wheeler', 'Kyle Bradish', 'Hogan Harris', 'Hunter Greene', 'Tobias Myers', 'Ranger Suárez', 'Ronel Blanco', 'Yoshinobu Yamamoto', 'Davis Martin', 'Logan Gilbert', 'Tanner Houck', 'David Peterson', 'Seth Lugo', 'Jack Flaherty', 'Michael King', 'José Buttó', 'Justin Steele', 'Corbin Burnes', 'Shota Imanaga', 'Logan Webb', 'Bradley Blalock', 'Cole Ragans', 'Brady Singer', 'Javier Assad', 'Albert Suárez', 'Yu Darvish', 'Framber Valdez', 'Ben Brown', 'Reese Olson', 'Luis Gil', 'Bryce Miller', 'Tyler Anderson', 'Luis Ortiz', 'Michael Wacha', 'Tanner Bibee', 'José Soriano', 'Randy Rodríguez', 'Kodai Senga', 'Erick Fedde', 'George Kirby', 'Aaron Nola', 'Dylan Cease', 'Sean Manaea', 'Cristopher Sánchez', 'Tyler Glasnow', 'Bailey Ober', 'Taj Bradley', 'Luis Castillo', 'Ryan Weathers', 'Jared Jones', 'Zebby Matthews', 'Joe Ryan', 'Garrett Crochet', 'Max Fried', 'Jameson Taillon', 'Merrill Kelly', 'Gavin Stone', 'Blake Snell', 'Ben Lively', 'Colin Rea', 'Ky Bush', 'Ryan Pepiot', 'Alek Manoah', 'Andrew Abbott', 'Zach Eflin', 'Michael Lorenzen', 'Andre Pallante', 'Nathan Eovaldi', 'Simeon Woods Richardson', 'Jake Irvin', 'Marcus Stroman', 'Zac Gallen', 'José Berríos', 'Tanner Banks', 'Grayson Rodriguez', 'Jackson Rutledge', 'Jeffrey Springs', 'Zack Littell', 'Max Scherzer', 'Cristian Javier', 'Hunter Brown', 'Luis Severino', 'Sonny Gray', 'Yariel Rodriguez', 'Jon Gray', 'Justin Verlander', 'Mitch Keller', 'Brandon Pfaadt', 'Freddy Peralta', 'Kolby Allard', 'Jordan Hicks', 'Jonathan Cannon', 'Cooper Criswell', 'Bailey Falter', 'Hayden Wesneski', 'Spencer Schwellenbach', 'Yilber Diaz', 'Cole Irvin', 'Lance Lynn', 'Kyle Harrison', 'JP Sears', 'Gerrit Cole', 'Paul Blackburn', 'Kevin Gausman', 'Nestor Cortes', 'Shane Baz', 'Casey Mize', 'Kutter Crawford', 'DJ Herz', 'Jose Quintana', 'Kyle Gibson',
                    'Andrew Heaney', 'Charlie Morton', 'Matt Waldron', 'Osvaldo Bido', 'Chris Bassitt', 'Carlos Rodón', 'Alex Cobb', 'Bowden Francis', 'Jordan Wicks', 'James Paxton', 'Mitchell Parker', 'Pablo López', 'Dean Kremer', 'Nick Pivetta', 'Yusei Kikuchi', 'Shawn Dubin', 'Elieser Hernández', 'Hoby Milner', 'Marco Gonzales', 'Nick Lodolo', 'Christian Scott', 'Grant Holmes', 'Cal Quantrill', 'Martín Pérez', 'Randy Vásquez', 'MacKenzie Gore', 'Darius Vines', 'Ryne Nelson', 'Justin Wrobleski', 'Mitch Spence', 'Bryse Wilson', 'Alec Marsh', 'Emerson Hancock', 'Aaron Civale', 'Brayan Bello', 'Carson Fulmer', 'Austin Gomber', 'Quinn Priester', 'Frankie Montas', 'Joey Estes', 'Matt Manning', 'Keider Montero', 'Trevor Rogers', 'Jared Shuster', 'Dane Dunning', 'Nick Martinez', 'Joe Musgrove', 'Tyler Mahle', 'Joe Ross', 'Chris Paddack', 'Jesús Luzardo', 'Ryan Feltner', 'Hayden Birdsong', 'Gavin Williams', 'Tyler Alexander', 'Jhonathan Diaz', 'Eduardo Rodriguez', 'José Ureña', 'Patrick Sandoval', 'Triston McKenzie', 'Luis Medina', 'Tylor Megill', 'Spencer Arrighetti', 'Graham Ashcraft', 'Alex Wood', 'Xzavion Curry', 'Braxton Garrett', 'David Festa', 'Dallas Keuchel', 'Joe Mantiply', 'Carson Spiers', 'Miles Mikolas', 'Griffin Canning', 'Kyle Tyler', 'Drew Thorpe', 'Logan Allen', 'Max Meyer', 'Carlos Carrasco', 'Chris Flexen', 'Taijuan Walker', 'Ross Stripling', 'Slade Cecconi', 'Edward Cabrera', 'Cade Povich', 'Aaron Brooks', 'Tyler Wells', 'Tyler Phillips', 'Patrick Corbin', 'Roddery Muñoz', 'Kyle Freeland', 'Scott McGough', 'Robbie Ray', 'Walker Buehler', 'Sixto Sánchez', 'Reid Detmers', 'Dakota Hudson', 'Jake Woodford', 'Steven Matz', 'Aaron Ashby', 'Joey Cantillo', 'Davis Daniel', 'Jordan Montgomery', 'Yonny Chirinos', 'Matthew Liberatore', 'Michael Soroka', 'Louie Varland', 'DL Hall', 'Daniel Lynch', 'Wade Miley', 'Tommy Henry', 'Bryce Elder', 'Jack Kochanowicz', 'Ty Blach', 'Mike Clevinger', 'Chayce McDermott', 'Germán Márquez', 'Chase Silseth', 'Kyle Hendricks', 'Jake Bloss', 'Zack Thompson', 'Tanner Gordon', 'Spencer Strider', 'Keaton Winn', 'Kenta Maeda', 'Carlos Rodriguez', 'Joe Boyle', 'J.P. France', 'Adam Mazur', 'Bryan Hoeing', 'Mason Black', 'Beau Brieske', 'Bobby Miller', 'Gordon Graceffo', 'Spencer Howard', 'Michael Mercado', 'Roansy Contreras', 'Zach Plesac', 'Brad Keller', 'Nick Nastrini', 'Adrian Houser', 'Will Warren', 'Anthony Banda', 'Paolo Espino', 'Drew Rasmussen', 'A.J. Puk', 'Ray Kerr', 'Joey Lucchesi', 'Cristian Mena', 'Jonathan Bowlan', 'José Suarez', 'Julio Teheran', 'Josiah Gray', 'Michael Grove', 'Shaun Anderson', 'Allan Winans', 'Anthony Molina', 'Kenny Rosenberg', 'Peter Lambert', 'Jack Leiter', 'Hurston Waldrep', 'Jonathan Hernández', 'Daulton Jefferies', 'Chase Anderson', 'Dan Altavilla', 'Blair Henley']
    if names:
        player_names = get_player_names()
    time.sleep(2)

    # Create a URL to an api endpoint which will contain data for all games from the beginning of the 2024 season leading up to the current date
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
    URL = f"https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2024-03-28&endDate={
        currentDate}"
    gamePkResponse = requests.get(URL)
    gamePkData = gamePkResponse.json()
    threads = []

    # Get the maximum number of days for which game data can be found
    days_of_games = get_days_of_games(gamePkData)
    print(f"\n[*] Days of Games Played: {days_of_games}")
    time.sleep(2)

    # Start up a quantity of threads equal to days_of_games which will all process data in parallel; start them and join (end) them once they
    # all complete
    for _ in range(days_of_games):
        posting = threading.Thread(
            target=getData, args=(_, gamePkData, player_names, ))
        threads.append(posting)
        posting.start()
        time.sleep(0.1)
    for thread in threads:
        thread.join()

    # Save the dictionary (player_dict) to a .json file
    print(f"\n[>] Saved player dictionary to: {file_name}")
    with open(f"{file_name}.json", 'a') as f:
        f.write('{\n')
    with open(f"{file_name}.json", 'a') as f:
        for key, value in player_dict.items():
            f.write(f'\t"{key}": {value},\n')
    with open(f"{file_name}.json", 'a') as f:
        f.write('\n}')


def get_player_names():

    print("[>] Updating list of player names\n[!] This may take up to several minutes\n")
    numPages = 14
    names = []

    for page in range(numPages):
        URL = f'https://www.mlb.com/stats/pitching?split=sp&page={
            page+1}&playerPool=ALL&sortState=asc'

        options = Options()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
        driver.get(URL)
        entries = driver.find_elements("xpath", '//span[@class="full-G_bAyq40"]')
        # print(entries)

        name = ""
        for x in range(len(entries)):
            name += entries[x].text+" "
            if x % 2 != 0 and x != 0:
                names.append(name.strip())
                name = ""
        print(f"[*] Finished gathering names for page {page+1}/{numPages}")
    return names

"""
Method will return the uppermost valid day for which data will return for games played

@param gamePkData: The full data which will be parsed to determine the maximum number of days
@return: The maximum number of days
"""
def get_days_of_games(gamePkData):
    days_of_games = 150
    counting = True
    while counting:
        try:
            games = gamePkData["dates"][days_of_games]["games"]
            counting = False
        except:
            days_of_games -= 1
    days_of_games += 1
    return days_of_games

"""
Method will save each player's innings pitched and earned runs to a dictionary, formatted as follows:
    {
        "player_1": ([innings_pitched_1,innings_pitched_2,...inningsPitched_n], [earned_runs_1,earned_runs_2,...earned_runs_n]),
        "player_2": ([innings_pitched_1,innings_pitched_2,...inningsPitched_n], [earned_runs_1,earned_runs_2,...earned_runs_n]),
        ...
        "player_n": ([innings_pitched_1,innings_pitched_2,...inningsPitched_n], [earned_runs_1,earned_runs_2,...earned_runs_n])
    }

@param day: The specific day for which data will be extracted
@param gamePkData: The full data which will be parsed to determine the maximum number of days
@return: None
"""
def getData(day,gamePkData,player_names):
    global player_dict

    # For the specified day in the total days data, retrieve the games that were played that day
    for dayIn in gamePkData["dates"][day+1]["games"]:
        gamePk = dayIn["gamePk"]

        # Get the game's boxscore
        boxscore_url = f"https://statsapi.mlb.com/api/v1/game/{gamePk}/boxscore"
        boxscore_response = requests.get(boxscore_url)

        # If the boxscore URL is valid and exists...
        if boxscore_response.status_code == 200:
            boxscore_data = boxscore_response.json()

            # Set up pre-defined parameters and lists that will be used to retrieve the correct data
            looking_for = ["inningsPitched", "earnedRuns"]
            teams = ["away", "home"]
            
            # For each team type (away and home), retrieve data on the team's players
            for team in teams:
                for teamIn in boxscore_data["teams"][team]["players"]:
                    # For all the players, retrieve only the ones who are pitching
                    for playerIn in boxscore_data["teams"][team]["players"][teamIn]["stats"]["pitching"]:
                        # Determine each pitcher's name and full ID
                        name = boxscore_data["teams"][team]["players"][teamIn]["person"]["fullName"]
                        full_id = boxscore_data["teams"][team]["players"][teamIn]["person"]["id"]
                        # Specifically retrieve either innings pitched or earned runs from the current player's statistics
                        if playerIn in looking_for:
                            # If the player is present in the pre-defined list of players that we are looking for, retrieve that player's data
                            if name in player_names:
                                # If the current player does not yet have an entry in the dictionary, create an empty one
                                if name not in player_dict:
                                    player_dict[name] = [[], []]
                                
                                # Add innings pitched and earned runs to their respective locations in the player's dictionary entry
                                if (float(boxscore_data["teams"][team]["players"][teamIn]["stats"]["pitching"]["inningsPitched"])!=0.0):
                                    if playerIn == "inningsPitched":
                                        player_dict[name][0].append(
                                            float(boxscore_data["teams"][team]["players"][teamIn]["stats"]["pitching"][playerIn]))
                                    elif playerIn == "earnedRuns":
                                        player_dict[name][1].append(
                                            float(boxscore_data["teams"][team]["players"][teamIn]["stats"]["pitching"][playerIn]))
                                    
                                print(f"[*] SAVED => Name: {name} | ID: {full_id} -> {playerIn}: {boxscore_data["teams"][team]["players"][teamIn]["stats"]["pitching"][playerIn]}")

if __name__ == "__main__":

    # Parse arguments for an (optional) user-specified file name
    parser = argparse.ArgumentParser(description='Arrange Player Data in a Dictionary')
    parser.add_argument('-fn', type=str, required=False,
                        help='file name for dictionary')
    parser.add_argument('-names', type=bool, required=False,
                        help='update list of players to look for')
    args = parser.parse_args()

    # Set file name to passed argument if argument exists; otherwise, file name will be called 'player_dictionary'

    main(args.fn,args.names)