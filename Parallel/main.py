import utils

from parallel_poly_prod import produce_poly
from parallel_power import produce_power
from parallel_pumpkins import produce_pump

while True:
	if num_items(Items.Power) < utils.item_min[Items.Power]:
		produce_power()		
	for entity in utils.poly_entities:
		if num_items(utils.entity_item[entity]) < utils.item_min[utils.entity_item[entity]]:
			produce_poly(entity)
	if num_items(Items.Pumpkin) < utils.item_min[Items.Pumpkin]:
		produce_pump()
