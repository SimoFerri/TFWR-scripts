# Author: Simone Ferri
# Date: 26/10/2025

# This script contains all the functions that handle the parallel production exploiting
# the polycultures to increase the efficency

import utils

sg_size = 8

# This verifies if the specified coordinates are inside a subgrid
def c_valid(x, y):
	return x >= 0 and x < sg_size and y >= 0 and y < sg_size

# This plants the specified entity and its companion inside a subgrid (sg_size x sg_size) of the entire farm
def plant_poly():
	global entity

	min_x = get_pos_x()
	min_y = get_pos_y()
	max_x = min_x + sg_size # It is not included in the valid x values
	max_y = min_y + sg_size # It is not included in the valid y values


	while num_items(utils.entity_item[entity]) < 1000000:
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
	
	entity = e

	ws = get_world_size()
	while ws % sg_size != 0:
		ws -= 1
	
	set_world_size(ws)
	utils.set_position(0, 0)

	for _ in range(ws / sg_size):
		for _ in range(ws / sg_size):
			spawn_drone(plant_poly)
			for _ in range(sg_size):
				move(East)
		for _ in range(sg_size):
			move(North)

	while num_drones() > 1:
		continue
		
