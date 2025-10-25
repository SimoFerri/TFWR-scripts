# Author: Simone Ferri
# Date: 24/10/2025

# This script contains functions that handles the setup and the harvest of the farm in order
# to produce Hay, Wood and Carrots

import utils

# This setups the farm planting all the cultures that are needed. The parameters n and d
# represent the fraction n/d to reserve for Wood and Carrots production
def setup_farm(n=2, d=3):
	change_hat(Hats.Traffic_Cone)
	utils.set_position(0, 0)
	for i in range(get_world_size() * n / d):
		for j in range(get_world_size()):
			harvest()
			if i % 2 == 0:
				if j % 2 == 0:
					if get_ground_type() == Grounds.Soil:
						till()
					plant(Entities.Tree)
				else:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Carrot)
			else:
				if j % 2 == 0:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Carrot)
				else:
					if get_ground_type() == Grounds.Soil:
						till()
					plant(Entities.Tree)
				
			if num_items(Items.Water) > 0:
				use_item(Items.Water)
			
			move(North)
		move(East)
		
	for _ in range(get_world_size() / d):
		for _ in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
				
			move(North)
		move(East)
		
# This harvests all the cultures inside the farm replacing them with fresh ones
def harvest_farm():
	change_hat(Hats.Brown_Hat)
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if can_harvest():
				entity = get_entity_type()
				harvest()
				plant(entity)
				if num_items(Items.Water) > 0:
					use_item(Items.Water)
			move(North)
		move(East)
