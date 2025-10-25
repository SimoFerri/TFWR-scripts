# Author: Simone Ferri
# Date: 25/10/2025

# This script contains the functions that handles the Cactus production
import utils

# This plants all the cactuses
def plant_cac():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			
			move(North)
		move(East)
		
# This sort the x-th row
def sort_row(x):
	utils.set_position(x, 0)
	while True:
		operations = 0
		for i in range(get_world_size()):
			if i < get_world_size() - 1 and measure() > measure(North):
				swap(North)
				operations += 1
			move(North)
		if operations == 0:
			return
			
# This sort the x-th column
def sort_col(x):
	utils.set_position(0, x)
	while True:
		operations = 0
		for i in range(get_world_size()):
			if i < get_world_size() - 1 and measure() > measure(East):
				swap(East)
				operations += 1
			move(East)
		if operations == 0:
			return
			
# This wraps up the Cactuses production
def produce_cac():
	plant_cac()
	for i in range(get_world_size()):
		sort_row(i)
	for i in range(get_world_size()):
		sort_col(i)
	utils.set_position(0, 0)
	harvest()
