# Author: Simone Ferri
# Date: 26/10/2025

# This script contains the functions that handles the parallel Cactus production
import utils

# This plant all the cactuses in a column, it's executed by "worker drones"
def plant_cac_col():
	for _ in range(get_world_size()):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		
		move(North)

# This plants all the cactuses
def plant_cac():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		spawn_drone(plant_cac_col)
		move(East)
	while num_drones() > 1:
		continue
		
# This sorts a row using the insertion sort algorithm
def sort_row():
	row = get_pos_y()
	for i in range(get_world_size()):
		utils.set_position(i, row)
		min = measure()
		min_col = get_pos_x()
		for j in range(i, get_world_size()):
			if measure() < min:
				min = measure()
				min_col = get_pos_x()
			if j < get_world_size() - 1:
				move(East)
		utils.set_position(min_col, row)
		while get_pos_x() != i:
			swap(West)
			move(West)
		
# This sorts a column using the insertion sort algorithm
def sort_col():
	col = get_pos_x()
	for i in range(get_world_size()):
		utils.set_position(col, i)
		min = measure()
		min_row = get_pos_y()
		for j in range(i, get_world_size()):
			if measure() < min:
				min = measure()
				min_row = get_pos_y()
			if j < get_world_size() - 1:
				move(North)
		utils.set_position(col, min_row)
		while get_pos_y() != i:
			swap(South)
			move(South)			
			
# This sorts all rows in parallel
def sort_rows():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		spawn_drone(sort_row)
		move(North)
	while num_drones() > 1:
		continue
		
# This sorts all columns in parallel
def sort_cols():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		spawn_drone(sort_col)
		move(East)
	while num_drones() > 1:
		continue
		
# This wraps up the Cactuses production
def produce_cac():
	plant_cac()
	sort_rows()
	sort_cols()
	utils.set_position(get_world_size() - 1, get_world_size() - 1)
	harvest()
