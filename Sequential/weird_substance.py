# Author: Simone Ferri
# Date: 25/10/2025

# This script contain the functions that are responsible for the Weird_Substance production

import utils
import pumpkins

# This wraps up the Wierd_Substance production using pumpkins
def produce_ws():
	pumpkins.plant_pump()
	pumpkins.remove_dead_pump()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if i % 3 == 0 and j % 3 == 0:
				if num_items(Items.Fertilizer) > 1:
					utils.set_position(i, j)
					use_item(Items.Fertilizer)
					if num_items(Items.Weird_Substance) > 0:
						use_item(Items.Weird_Substance)
					use_item(Items.Fertilizer)
			elif i % 3 != 0 and j % 3 != 0:
				if num_items(Items.Fertilizer) > 1:
					utils.set_position(i, j)
					use_item(Items.Fertilizer)
				
	harvest()
