def roll_call_dwarves(dwarves):
    num_dwarves = [f'{dwarf[0]}. {dwarf[1]}' for dwarf in enumerate(dwarves,1)]
    for dwarf in num_dwarves:
        print(dwarf)
    pass

# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
def summon_captain_planet(planeteers):
    list = [f'{planeteer.title()}!' for planeteer in planeteers]
    return list
    pass

# summon_captain_planet(["earth", "wind", "fire", "water", "heart"])
def long_planeteer_calls(planeteers):
    list = [True for planeteer in planeteers if len(planeteer) > 4]
    if not list:
        return False 
    else:
        return True


# long_planeteer_calls(["puff", "go", "two"])

def find_the_cheese(list):
    cheese = ['gouda','cheddar','camembert']
    values = []

    for item in list:
        if item in cheese:
            print(item)
    return None 

# find_the_cheese(["crackers", "gouda", "thyme"])
find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"])