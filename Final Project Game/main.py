import random

# Player stats
player = {
    "health": 50,
    "max_health": 50,
    "damage": 15,
    "inventory": [],
    "equipped": {"weapon": None, "chest_armor": None, "boots": None},
    "defeated_monsters": [],
}

# Locations
locations = {
    "Center Plaza": {"description": "The starting point of your journey.", "unlocked": True, "item_obtained": True},
    "North House": {"description": "An easy monster to fight.", "monster": "A beast lies here, but he seems to be invisible!", "unlocked": True, "item_obtained": False},
    "East House": {"description": "An easy monster with a 10% chance to drop the Severed Hand.", "monster": "A monster with blades for hands!", "unlocked": True, "item_obtained": False},
    "West House": {"description": "An easy monster with a 10% chance to drop Rotten Teeth.", "monster": "The undead has come back! He seems to own the house and pay the mortage too!", "unlocked": True, "item_obtained": False},
    "Western School District": {"description": "Stronger monster that fights back.", "monster": "The Janitor Rebels!", "unlocked": False, "item_obtained": False},
    "Eastern School District": {"description": "Stronger monster that fights back.", "monster": "Rick The Door Technician", "unlocked": False, "item_obtained": False},
    "Western Military": {"description": "Requires weapons to defeat.", "monster": "Field Guard", "unlocked": False, "item_obtained": False},
    "Eastern Military": {"description": "Requires weapons to defeat.", "monster": "A juggernaut!(not from marvel, trust)", "unlocked": False, "item_obtained": False},
    "City Border": {"description": "Boss fight requiring specific items.", "monster": "The Undead City Border Police", "unlocked": False, "item_obtained": False},
    "State Line": {"description": "The final boss awaits you.", "monster": "Satan Himself!", "unlocked": False, "item_obtained": False},
}

# Monsters
monsters = {
    "A beast lies here, but he seems to be invisible!": {"health": 20, "damage": 5},
    "A monster with blades for hands!": {"health": 20, "damage": 5},
    "The undead has come back! He seems to own the house and pay the mortage too!": {"health": 20, "damage": 5},
    "The Janitor Rebels!": {"health": 50, "damage": 10},
    "Rick The Door Technician": {"health": 50, "damage": 10},
    "Field Guard": {"health": 75, "damage": 12}, 
    "A juggernaut!(not from marvel, trust)": {"health": 75, "damage": 12},
    "The Undead City Border Police": {"health": 100, "damage": 15},
    "Satan Himself!": {"health": 150, "damage": 20},
}

# Items
items = {
    "Weak Knife": {"type": "weapon", "boost": {"damage": 5}, "description": "Increases damage by 5."},
    "Weak Chest Plate": {"type": "chest_armor", "boost": {"max_health": 10}, "description": "Boosts max health by 10."},
    "Bandage": {"type": "healing", "boost": {"health": 20}, "description": "Heals 20 health. One-time use."},
    "Vaporub": {"type": "healing", "boost": {"health": 10}, "description": "Heals 10 health. One-time use."},
    "Weak Boots": {"type": "boots", "boost": {"dodge_chance": 0.1}, "description": "10% chance to avoid damage."},
    "Severed Hand": {"type": "special", "boost": {}, "description": "One-hit kill on any monster. One-time use."},
    "Rotten Teeth": {"type": "boots", "boost": {"steal_health": 20}, "description": "Steals 20 health from a monster."},
    "Military Helmet": {"type": "head_gear", "boost": {"damage": 10}, "description": "Increases damage by 10."},
    "Bulletproof Armor": {"type": "chest_armor", "boost": {"max_health": 25}, "description": "Increases health by 25."},
    "Field Officer Sword": {"type": "weapon", "boost": {"damage": 25}, "description": "Increases damage by 25."},
    "Blast Suit": {"type": "chest_armor", "boost": {"damage": 5, "max_health": 75}, "description": "Increases damage by 5 and max health by 75."},
    "Hand Grenades": {"type": "weapon", "boost": {"damage": 50}, "description": "Increases damage by 50."},
}

# Random Item Drop Function
def drop_random_item(location):
    if location == "Western School District" or location == "Eastern School District":
        item_type = random.choice(["boots", "chest_armor", "weapon"])
        if item_type == "boots":
            item_name = "Weak Boots"
            item = items[item_name]
        elif item_type == "chest_armor":
            item_name = "Weak Chest Plate"
            item = items[item_name]
        elif item_type == "weapon":
            item_name = "Weak Knife"
            item = items[item_name]
        
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "Western Military":
        item_name = random.choice(["Military Helmet", "Field Officer Sword", "Bulletproof Armor"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "Eastern Military":
        item_name = random.choice(["Military Helmet", "Field Officer Sword", "Bulletproof Armor"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    elif location == "City Border":
        item_name = random.choice(["Blast Suit", "Hand Grenades"])
        item = items[item_name]
        print(f"You defeated the monster and found a {item_name}!")
        player["inventory"].append(item_name)
    else:
        # For other locations, just add random item
        item_name = random.choice(list(items.keys()))
        item = items[item_name]
        print(f"You found a {item_name}!")
        player["inventory"].append(item_name)

# Combat function
def combat(monster_name):
    monster = monsters[monster_name]
    print(f"A {monster_name} appears! It has {monster['health']} health and does {monster['damage']} damage.")
    while player["health"] > 0 and monster["health"] > 0:
        action = input("Do you want to (attack), (use item), or (equip/unequip item)? ").lower()
        if action == "attack":
            monster["health"] -= player["damage"]
            print(f"You hit the {monster_name}. It has {max(0, monster['health'])} health left.")
        elif action == "use item":
            if "Severed Hand" in player["inventory"]:
                print(f"You used the Severed Hand! The {monster_name} is defeated instantly.")
                player["inventory"].remove("Severed Hand")
                monster["health"] = 0
            else:
                print("You don't have any usable items.")
        elif action == "equip":
            item_name = input("Which item do you want to equip? ").strip()
            equip_item(item_name)
        elif action == "unequip":
            item_type = input("Which type of item do you want to unequip? (weapon, chest_armor, boots) ").strip()
            unequip_item(item_type)
        if monster["health"] > 0:
            player["health"] -= monster["damage"]
            print(f"The {monster_name} hit you. You have {player['health']} health left.")
    if player["health"] <= 0:
        print("You have been defeated. Game over!")
        exit()
    else:
        print(f"You defeated the {monster_name}!")
        player["defeated_monsters"].append(monster_name)
        drop_random_item(current_location)

# Unlock new areas
def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["A beast lies here, but he seems to be invisible!", "A monster with blades for hands!", "The undead has come back! He seems to own the house and pay the mortage too!"]):
        locations["Western School District"]["unlocked"] = True
        locations["Eastern School District"]["unlocked"] = True
        print("The school districts are now unlocked! Type west or east school to go there!")

def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["A beast lies here, but he seems to be invisible!", "A monster with blades for hands!", "The undead has come back! He seems to own the house and pay the mortage too!", "The Janitor Rebels!", "Rick The Door Technician"]):
        locations["Western Military"]["unlocked"] = True
        locations["Eastern Military"]["unlocked"] = True
        print("The Militaries are now unlocked! Type west or east military to go there!")

def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["A beast lies here, but he seems to be invisible!", "A monster with blades for hands!", "The undead has come back! He seems to own the house and pay the mortage too!", "The Janitor Rebels!", "Rick The Door Technician", "Field Guard" "A juggernaut!(not from marvel, trust)"]):
        locations["City Border"] = True
        print("The City Border is now unlocked! Type city border to go there!")

def unlock_locations():
    if all(monster in player["defeated_monsters"] for monster in ["A beast lies here, but he seems to be invisible!", "A monster with blades for hands!", "The undead has come back! He seems to own the house and pay the mortage too!", "The Janitor Rebels!", "Rick The Door Technician", "Field Guard" "A juggernaut!(not from marvel, trust)", "The Undead City Border Police"]):
        locations["State Line"] = True
        print("The State Line is now unlocked! Type state line to go there!")

# Item drop function
def drop_item(location):
    if not locations[location]["item_obtained"]:
        if location == "East House" and random.random() < 0.1:
            print("You found the Severed Hand!")
            player["inventory"].append("Severed Hand")
        elif location == "West House" and random.random() < 0.1:
            print("You found Rotten Teeth!")
            player["inventory"].append("Rotten Teeth")
        else:
            item = random.choice(list(items.keys()))
            print(f"You found a {item}!")
            player["inventory"].append(item)
        locations[location]["item_obtained"] = True

# Main game loop
def play_game():
    print("Welcome to the game!")
    current_location = "Center Plaza"
    while True:
        unlock_locations()
        print(f"You are at {current_location}.")
        print_stats()
        command = input("Enter a command (north, east, west, equip, unequip, inventory, or quit): ").lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "equip":
            item_name = input("Which item do you want to equip? ").strip()
            equip_item(item_name)
        elif command == "unequip":
            item_type = input("Which type of item do you want to unequip? (weapon, chest_armor, boots) ").strip()
            unequip_item(item_type)
        elif command == "inventory":
            print("Your Inventory:")
            for item in player["inventory"]:
                print(f"- {item}: {items[item]['description']}")
        elif command == "north":
            current_location = "North House"
            combat("A beast lies here, but he seems to be invisible!")
            drop_item(current_location)
        elif command == "east":
            current_location = "East House"
            combat("A monster with blades for hands!")
            drop_item(current_location)
        elif command == "west":
            current_location = "West House"
            combat("The undead has come back! He seems to own the house and pay the mortage too!")
            drop_item(current_location)
        elif command == "west school" and locations["Western School District"]["unlocked"]:
            current_location = "Western School District"
            combat("The Janitor Rebels!")
        elif command == "east school" and locations["Eastern School District"]["unlocked"]:
            current_location = "Eastern School District"
            combat("Rick The Door Technician")
        elif command == "west military" and locations["Western School District"]["unlocked"]:
            current_location = "Western Military"
            combat("Field Guard")
        elif command == "east military" and locations["Eastern School District"]["unlocked"]:
            current_location = "Eastern Military"
            combat("A juggernaut!(not from marvel, trust)")
        elif command == "city border" and locations["Eastern School District"]["unlocked"]:
            current_location = "City Border"
            combat("The Undead City Border Police")
        elif command == "state line" and locations["Eastern School District"]["unlocked"]:
            current_location = "State Line"
            combat("Satan Himself!")
        else:
            print("Invalid command.")

play_game()

#Fix the bugs