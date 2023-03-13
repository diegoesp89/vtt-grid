import character
import itertools
import monster
import requests
import json
import random
import pygame

API_URL = "https://api.open5e.com/monsters/"
SEARCH_URL = "https://api.open5e.com/monsters/?search="

player = character.Character("Player", 10, 10, 10, 10, 10, 10, 15, 30, [], [], [], [], [], [], [], 0, 1, "Fighter", "Champion", 0, 0, 0, 0, 0, 0, "Arcana", 10, 10)
monsters = []
#we make a grid of XxY squares
grid_x_len = 20
grid_y_len = 20
grid = []
for i in range(grid_x_len):
    grid.append([])
    for j in range(grid_y_len):
        grid[i].append(".") #empty space
        

def dice(d):
    d = d.split("d")
    num_dice = int(d[0])
    #the modifier can be positive or negative
    if(d[1].find("+") != -1):
        d = d[1].split("+")
        num_sides = int(d[0])
        modifier = int(d[1])
    elif(d[1].find("-") != -1):
        d = d[1].split("-")
        num_sides = int(d[0])
        modifier = -int(d[1])   
    else:
        num_sides = int(d[1])
        modifier = 0

    result = 0
    for i in range(num_dice):
        result += random.randint(1, num_sides)
    result += modifier
    return result


def main():
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
        monsters.append(monster.Monster(monster_data["slug"], monster_data["name"] + " " + str(i+1), monster_data["size"], monster_data["type"], monster_data["subtype"], monster_data["group"], monster_data["alignment"], monster_data["armor_class"], monster_data["armor_desc"], hp, max_hp, monster_data["hit_dice"], monster_data["speed"], monster_data["strength"], monster_data["dexterity"], monster_data["constitution"], monster_data["intelligence"], monster_data["wisdom"], monster_data["charisma"], monster_data["strength_save"], monster_data["dexterity_save"], monster_data["constitution_save"], monster_data["intelligence_save"], monster_data["wisdom_save"], monster_data["charisma_save"], monster_data["perception"], monster_data["skills"], monster_data["damage_vulnerabilities"], monster_data["damage_resistances"], monster_data["damage_immunities"], monster_data["condition_immunities"], monster_data["senses"], monster_data["languages"], monster_data["challenge_rating"], monster_data["cr"], monster_data["actions"], monster_data["reactions"], monster_data["legendary_desc"], monster_data["legendary_actions"], monster_data["special_abilities"], monster_data["spell_list"], monster_data["img_main"], monster_data["document__slug"], monster_data["document__title"], monster_data["document__license_url"], random.randint(0, grid_x_len-1), random.randint(0, grid_y_len-1)))
    print("Addded " + str(num_monsters) + " " + monster_data["name"] + "s to the encounter.")
    repeat = input("Do you want to add more monsters? (y/n) ")
    if repeat == "y":
        main()
    else:
        for i in range(len(monsters)):
            print("id:" + str(i) + " - " + monsters[i].name + " - " + str(monsters[i].hit_points) + "/" + str(monsters[i].max_hit_points) + " HP - pos: " + str(monsters[i].pos_x) + ", " + str(monsters[i].pos_y))
            #show the grid
        print("---------------------")

        #we print the grid, with the monsters and the player in thei console, with their positions, and the rest of the squares as a "." symbol, the player is represented by a "P" symbol and the monsters by their index in the monsters list
        """ for i in range(grid_x_len):
            for j in range(grid_y_len):
                for k in range(len(monsters)):
                    if monsters[k].pos_x == i and monsters[k].pos_y == j:
                        grid[i][j] = str(k)
                if player.pos_x == i and player.pos_y == j:
                    grid[i][j] = "P"
                print(grid[i][j], end=" ")
            print() """
        show_grid()


#we use pygame to create a window with a grid, and we use the arrow keys to move the player
def show_grid():
    pygame.init()
    screen = pygame.display.set_mode((grid_x_len*50, grid_y_len*50))
    pygame.display.set_caption("Encounter Grid")
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if player.pos_x > 0:
                        player.pos_x -= 1
                if event.key == pygame.K_RIGHT:
                    if player.pos_x < grid_x_len-1:
                        player.pos_x += 1
                if event.key == pygame.K_UP:
                    if player.pos_y > 0:
                        player.pos_y -= 1
                if event.key == pygame.K_DOWN:
                    if player.pos_y < grid_y_len-1:
                        player.pos_y += 1
        screen.fill((0, 0, 0))
        for i in range(grid_x_len):
            for j in range(grid_y_len):
                for k in range(len(monsters)):
                    if monsters[k].pos_x == i and monsters[k].pos_y == j:
                        grid[i][j] = str(k)
                if player.pos_x == i and player.pos_y == j:
                    grid[i][j] = "P"
                if grid[i][j] == "P":
                    pygame.draw.rect(screen, (255, 0, 0), (i*50, j*50, 50, 50))
                elif grid[i][j] == ".":
                    pygame.draw.rect(screen, (255, 255, 255), (i*50, j*50, 50, 50))
                else:
                    pygame.draw.rect(screen, (0, 255, 0), (i*50, j*50, 50, 50))
                
                #if there is a monster in the square, we draw its index in the grid
                if grid[i][j] != "P" and grid[i][j] != ".": 
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render(grid[i][j], True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (i*50+25, j*50+25)
                    screen.blit(text, textRect)
        pygame.display.update()
    pygame.quit()
    

if __name__ == "__main__":
    main()

