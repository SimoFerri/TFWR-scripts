# Author: Simone Ferri
# Date: 24/10/2025

# This script contains the functions that handle Power production via the planting and
# the harvesting of Sunflowers

import utils

# This is an implementation of the well known counting sort algorithm used to sort the list of
# Sunflowers positions based on their number of petals that is always between 7 and 15.
# Note that the list must be a list of lists, index is the index of the entries used to sort
# the list.
def counting_sort(list, k, index):
	result = []
	prevs = []
	
	for _ in range(list.len()):
		result.append(0)
	for _ in range(k + 1):
		prevs.append(0)
		
	for val in list:
		prevs[val[index]] += 1
		
	for i in range(1, k + 1):
		prevs[i] += prevs[i - 1]
		
	for i in range(list.len() - 1, 0, -1):
		result[prevs[list[i][index]] - 1] = list[i]
		prevs[list[i][index]] -= 1
		
	result.remove(0)
	
	return result
	
# This plants all the Sunflowers and fills the positions list with lists of the form
# [number of petals, x, y] for each planted Sunflower
def plant_sf():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)

		if num_items(Items.Water) > 0 and get_water() < 0.5:
			use_item(Items.Water)
			
		move(North)
		
# This harvests all Sunflowers until they are 10 (this is because it's meaningless to harvest
# the biggest Sunflower when they are less than 10, the bonus will not be given) assuming
# that the list positions is sorted in an increasing order
def harvest_sf(positions):
	while positions.len() > 10:
		pos = positions.pop()
		utils.set_position(pos[1], pos[2])
		while not can_harvest():
			continue
		harvest()
		
# This function wraps up the Power production taking as argument the target amount of
# Power that the user wants to acheive
def produce_power():
	set_world_size(8)
	change_hat(Hats.Straw_Hat)
	while num_items(Items.Power) < utils.item_target[Items.Power]:
		positions = []
		for _ in range(get_world_size()):
			while num_drones() >= max_drones():
				continue
			spawn_drone(plant_sf)
			move(East)
		
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
                while measure() == None:
                    continue
                positions.append([measure(), get_pos_x(), get_pos_y()])
				move(North)
			move(East)	
		
		harvest_sf(counting_sort(positions, 15, 0))
	set_world_size(0)
