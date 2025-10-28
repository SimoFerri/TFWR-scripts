# Author: Simone Ferri
# Date: 26/10/2025

# This script contains all the functions that handle the parallel production exploiting
# the polycultures to increase the efficency

import utils

# This verifies if the specified coordinates are inside a subgrid
def c_valid(x, y):
	return x >= 0 and x < sg_size and y >= 0 and y < sg_size

# This plants the specified entity and its companion inside a subgrid (sg_size x sg_size) of the entire farm
def plant_poly():
	global entity
    global sg_size

	min_x = get_pos_x()
	min_y = get_pos_y()
	max_x = min_x + sg_size # It is not included in the valid x values
	max_y = min_y + sg_size # It is not included in the valid y values


    while num_items(utils.entity_item[entity]) < utils.item_goal[entity_target[entity]]:
        if num_items(Items.Power) < utils.item_min[Items.Power]:
			return
		for item in cost:
			if num_items(item) < cost[item]:
				return
		occupied = []
		for _ in range(sg_size):
			for _ in range(sg_size):
				occupied.append(False)

		utils.set_position(min_x, min_y)
		for i in range(sg_size):
			for j in range(sg_size):
				utils.set_position(min_x + i, min_y + j)
				if num_items(Items.Water) > 0 and get_water() < 0.5:
					use_item(Items.Water)
				if not occupied[i * sg_size + j]:
					harvest()
					if get_ground_type() != utils.entity_ground[entity]:
						till()
					plant(entity)
					occupied[i * sg_size + j] = True
					
					companion = get_companion()
					c_entity = companion[0]
					c_x = companion[1][0] - min_x
					c_y = companion[1][1] - min_y
					if companion != None and c_valid(c_x, c_y) and not occupied[c_x * sg_size + c_y]:
						utils.set_position(min_x + c_x, min_y + c_y)
						harvest()
						if get_ground_type() != utils.entity_ground[c_entity]:
							till()
						plant(c_entity)
						occupied[c_x * sg_size + c_y] = True
		
		utils.set_position(min_x, min_y)
		for i in range(sg_size):
			for j in range(sg_size):
				e = get_entity_type()
				harvest()
				plant(e)
				if i % 2 == 0 and j < sg_size - 1:
					move(North)
				elif j < sg_size - 1:
					move(South)
			if i < sg_size - 1:
				move(East)

# This wraps up the production of Hay
def produce_poly(e):
	global entity
	global sg_size

	entity = e

	side = 1
	while (side + 1)**2 <= max_drones():
		side += 1

	sg_size = 1
	while side * (sg_size + 1) <= get_world_size():
		sg_size += 1

	ws = side * sg_size

	set_world_size(ws)
	utils.set_position(0, 0)

	for i in range(side):
		for j in range(side):
			spawn_drone(plant_poly)
			if i < side - 1 or j < side - 1:
				for _ in range(sg_size):
					move(East)
		if i < side - 1:
			for _ in range(sg_size):
				move(North)
	plant_poly()

	while num_drones() > 1:
			continue

	set_world_size(0)
