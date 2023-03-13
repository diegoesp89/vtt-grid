import character
import monster
import requests
import json
import random

API_URL = "https://api.open5e.com/monsters/"
SEARCH_URL = "https://api.open5e.com/monsters/?search="

monsters = []

def dice(d):
    d = d.split("d")
    num_dice = int(d[0])
    d = d[1].split("+")
    num_sides = int(d[0])
    if len(d) > 1:
        modifier = int(d[1])
    else:
        modifier = 0
    result = 0
    for i in range(num_dice):
        result += random.randint(1, num_sides)
    result += modifier
    return result


def main():
    player = character.Character("Player", 10, 10, 10, 10, 10, 10, 15, 30, [], [], [], [], [], [], [], 0, 1, "Fighter", "Champion", 0, 0, 0, 0, 0, 0, "Arcana")
    #we ask the user for a monster name and how many of them are in the encounter
    monster_name = input("What monster do you want to fight? ")
    num_monsters = int(input("How many of them are there? "))
    hp_type = input("Do you want to use the monster's HP or roll for it? (m/r) ")
    monster_url = API_URL + monster_name
    response = requests.get(monster_url)
    if(response.text.find("Not found.") != -1):
        print("Monster not found.")
        search = SEARCH_URL + monster_name
        response = requests.get(search)
        if(response.text.find("Not found.") != -1):
            print("No results found.")
            exit()
        elif(response.text.find("results") != -1):
            monster_data = json.loads(response.text)
            print("Did you mean:")
            for i in range(len(monster_data["results"])):
                print(str(i) + ":" + monster_data["results"][i]["name"] + "- CR: " + str(monster_data["results"][i]["challenge_rating"]) + " - Size: " + monster_data["results"][i]["size"] + " - Type: " + monster_data["results"][i]["type"] + " - Alignment: " + monster_data["results"][i]["alignment"] + " - Source: " + monster_data["results"][i]["document__title"])
            selection = input("Enter the number of the monster you want to add: ")
            monster_url = API_URL + monster_data["results"][int(selection)]["slug"]
            response = requests.get(monster_url)
            if(response.text.find("Not found.") != -1):
                print("Monster not found.")
                exit()
        else:
            print("Not found.")
            exit()
    monster_data = json.loads(response.text)
    #print(monster_data)

    #we create a monster object
    for i in range(num_monsters):
        if hp_type == "m":
            hp = monster_data["hit_points"]
            max_hp = hp
        else:
            hp = dice(monster_data["hit_dice"])
            max_hp = hp
        monsters.append(monster.Monster(monster_data["slug"], monster_data["name"] + " " + str(i+1), monster_data["size"], monster_data["type"], monster_data["subtype"], monster_data["group"], monster_data["alignment"], monster_data["armor_class"], monster_data["armor_desc"], hp, max_hp, monster_data["hit_dice"], monster_data["speed"], monster_data["strength"], monster_data["dexterity"], monster_data["constitution"], monster_data["intelligence"], monster_data["wisdom"], monster_data["charisma"], monster_data["strength_save"], monster_data["dexterity_save"], monster_data["constitution_save"], monster_data["intelligence_save"], monster_data["wisdom_save"], monster_data["charisma_save"], monster_data["perception"], monster_data["skills"], monster_data["damage_vulnerabilities"], monster_data["damage_resistances"], monster_data["damage_immunities"], monster_data["condition_immunities"], monster_data["senses"], monster_data["languages"], monster_data["challenge_rating"], monster_data["cr"], monster_data["actions"], monster_data["reactions"], monster_data["legendary_desc"], monster_data["legendary_actions"], monster_data["special_abilities"], monster_data["spell_list"], monster_data["img_main"], monster_data["document__slug"], monster_data["document__title"], monster_data["document__license_url"]))
    print("Addded " + str(num_monsters) + " " + monster_data["name"] + "s to the encounter.")
    repeat = input("Do you want to add more monsters? (y/n) ")
    if repeat == "y":
        main()
    else:
        for i in range(len(monsters)):
            print(monsters[i].name + " - " + str(monsters[i].hit_points) + "/" + str(monsters[i].max_hit_points) + " HP")

if __name__ == "__main__":
    main()

