# Author: Simone Ferri
# Date: 26/10/2025

# This dictionary represent for each Entity the Ground on which it has to be planted
entity_ground = {
    Entities.Grass: Grounds.Grassland,
    Entities.Bush: Grounds.Grassland,
    Entities.Tree: Grounds.Grassland,
    Entities.Carrot: Grounds.Soil,
    Entities.Pumpkin: Grounds.Soil,
    Entities.Cactus: Grounds.Soil,
    Entities.Sunflower: Grounds.Soil
}

# Sets the drone position at the specified coordinates
# note: when unlock the abs function this can be optimized in a clean way
def set_position(x, y):
	if not (x >= 0 and x < get_world_size() and y >= 0 and y < get_world_size()):
		return
		
	while x < get_pos_x():
		move(West)
	while x > get_pos_x():
		move(East)
	while y < get_pos_y():
		move(South)
	while y > get_pos_y():
		move(North)

# This function harvests and replaces the entire farm
def harvest_all():
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            entity = get_entity_type()
            if can_harvest():
                harvest()
            if entity != None:
                plant(entity)
            move(North)
        move(East)
