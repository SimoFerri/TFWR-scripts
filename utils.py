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

# This dictionary represent for each Entity the Item which is obtained by its harvesting
entity_item = {
	Entities.Grass: Items.Hay,
	Entities.Bush: Items.Wood,
	Entities.Tree: Items.Wood,
	Entities.Carrot: Items.Carrot,
	Entities.Pumpkin: Items.Pumpkin,
	Entities.Cactus: Items.Cactus,
	Entities.Sunflower: Items.Power
}

# This dictonary represent for each Item the amount under which start its production
item_min = {
	Items.Hay: 100000,
	Items.Wood: 100000,
	Items.Carrot: 100000,
	Items.Pumpkin: 100000,
	Items.Cactus: 100000,
	Items.Gold: 1000000,
	Items.Power: 30000
}

# This dictonary represent for each Item the target amount of its production
item_target = {
	Items.Hay: 1000000,
	Items.Wood: 1000000,
	Items.Carrot: 1000000,
	Items.Pumpkin: 1000000,
	Items.Cactus: 1000000,
	Items.Gold: 10000000,
	Items.Power: 500000
}

# This tuple contains the Entities which can be planted using polycolture
poly_entities = (Entities.Grass, Entities.Bush, Entities.Carrot)

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
