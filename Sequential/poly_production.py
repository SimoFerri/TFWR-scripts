# Author: Simone Ferri
# Date: 26/10/2025

# This script contains all the functions that handle the production exploiting
# the polycultures to increase the efficency

import utils

ws = 8

# This plants the specified entity and its companion until it reaches a certain occupancy
def plant_poly(entity):
	occupied = []
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			occupied.append(False)

	planted = 0
	limit = get_world_size()**2 * 3 / 4
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			utils.set_position(i, j)
			if not occupied[i * get_world_size() + j]:
				harvest()
				if get_ground_type() != utils.entity_ground[entity]:
					till()
				plant(entity)
				occupied[i * get_world_size() + j] = True
				planted += 1
				if planted == limit:
					return
				companion = get_companion()
				if companion != None and not occupied[companion[1][0] * get_world_size() + companion[1][1]]:
					utils.set_position(companion[1][0], companion[1][1])
					harvest()
					if get_ground_type() != utils.entity_ground[companion[0]]:
						till()
					plant(companion[0])
					occupied[companion[1][0] * get_world_size() + companion[1][1]] = True
					planted += 1
					if planted == limit:
						return

# This wraps up the production of Hay
def produce_poly(entity):
	set_world_size(ws)
	utils.set_position(0, 0)
	while num_items(utils.entity_item[entity]) < 1000000:
		plant_poly(entity)
		utils.harvest_all()
		
