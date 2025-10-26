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
def set_position(x, y):
    ws = get_world_size()
	if not (x >= 0 and x < ws and y >= 0 and y < ws):
			return
	
	drone_x = get_pos_x()
	drone_y = get_pos_y()
	if x > drone_x:
		if abs(x - drone_x) < abs(drone_x + ws - x):
			x_dir = East
		else:
			x_dir = West
	else:
		if abs(x - drone_x) < abs(x + ws - drone_x):
			x_dir = West
		else:
			x_dir = East
		
			
	if y > drone_y:
		if abs(y - drone_y) < abs(drone_y + ws - y):
			y_dir = North
		else:
			y_dir = South
	else:
		if abs(y - drone_y) < abs(y + ws - drone_y):
			y_dir = South
		else:
			y_dir = North
			
	while x != get_pos_x():
		move(x_dir)
	while y != get_pos_y():
		move(y_dir)


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
