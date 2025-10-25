# Author: Simone Ferri
# Date: 24/10/2025

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
