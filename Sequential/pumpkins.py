# Author: Simone Ferri
# Date: 25/10/2025

# This script includes the functions that handle the planting and the harvesting
# of pumpkins
import utils

# This plants Pumpkins all across the farm
def plant_pump():
    utils.set_position(0, 0)
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)

            if num_items(Items.Water) > 0 and get_water() < 0.5:
                use_item(Items.Water)

            move(North)
        move(East)

# This replace all the Dead_Pumpkins with Pumpkins by re-planting them, this leads to the
# generation of the biggest possible pumpking for the farm dimensions
def remove_dead_pump():
    utils.set_position(0, 0)
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            while not can_harvest():
                if get_entity_type() == Entities.Dead_Pumpkin:
                    plant(Entities.Pumpkin)

            move(North)
        move(East)

# This wraps up the Pumpkin production
def produce_pump(target):
    change_hat(Hats.Purple_Hat)
    plant_pump()
    remove_dead_pump()
    harvest()

