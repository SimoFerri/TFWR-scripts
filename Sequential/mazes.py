# Author: Simone Ferri
# Date: 25/10/2025

# This script contains the functions responsible for the maze solving and so for the
# Treasure production

import utils

directions = [North, East, West, South]

opp_dirs = {
	North: South,
	East: West,
	West: East,
	South: North
}

# This recursively finds the Treasure using a DFS algorithm
def find_treasure(directions, coming):
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	
	if coming == None:
		coming = South
	for dir in directions:
		if dir != coming and can_move(dir):
			move(dir)
			found = find_treasure(directions, opp_dirs[dir])
			if found:
				return True
	move(coming)
	
	return False

# This wraps up the Treasure production
def produce_treasures(n):
	change_hat(Hats.Gold_Hat)
	harvest()
	for _ in range(n):
		utils.set_position(0, 0)
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		find_treasure(directions, None)
