# Author: Simone Ferri
# Date: 26/10/2025

# This script includes the functions that handle the planting and the harvesting
# of pumpkins
import utils

# This plants all the Pumpkins in a column, this is executed by a "Worker Drone"
def plant_pump_col():
	for _ in range(get_world_size()):
        if num_items(Items.Power) < utils.item_min[Items.Power]:
			return
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)

		if num_items(Items.Water) > 0 and get_water() < 0.5:
			use_item(Items.Water)

		move(North)

# This plants Pumpkins all across the farm
def plant_pump():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		spawn_drone(plant_pump_col)
		move(East)
		
	while num_drones() > 1:
		continue

# This replace all Dead_Pumpkins with a Pumpkin in a column
def remove_dead_pump_col():
	for _ in range(get_world_size()):
        if num_items(Items.Power) < utils.item_min[Items.Power]:
			return
		while not can_harvest():
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)

		move(North)
			

# This replace all the Dead_Pumpkins with Pumpkins by re-planting them, this leads to the
# generation of the biggest possible pumpking for the farm dimensions
def remove_dead_pump():
	utils.set_position(0, 0)
	for _ in range(get_world_size()):
		while num_drones() >= max_drones():
			continue
		spawn_drone(remove_dead_pump_col)
		move(East)
		
	while num_drones() > 1:
		continue

# This wraps up the Pumpkin production
def produce_pump():
	change_hat(Hats.Purple_Hat)
    while num_items(Items.Pumpkin) < utils.item_target[Items.Pumpkin]:
        plant_pump()
        remove_dead_pump()
        harvest()
        
