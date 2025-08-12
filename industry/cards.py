from funcs import *
from objects import Effect, Manufactories

compensation1 = Effect(coil=1, steel=1)
compensation2 = Effect(coil=2)
compensation3 = Effect(modernization_tockens=1)

production1 = Effect(modernization_tockens=1, funcs=[coil2_to_points, mt_n_coil_to_upgrade])
production2 = production1
production2.effect['funcs'][0] = oil_to_points
production3 = production1
production3.effect['funcs'][0] = coil3_to_points
production4 = production1
production4.effect['funcs'][0] = coil_n_steel_to_points
production5 = production1
production5.effect['funcs'][0] = steel_to_points_2x

start_card1 = Manufactories(description='Start card 1\n Compensation: 1 coil, 1 steel\n Production: 1 modernisation tocken, 2 coil -> 2 vp (2x), modernization_tocken + coil -> upgrade', compensation=compensation1, production=production1)

start_card2 = Manufactories(description='Start card 2\n Compensation: 1 coil, 1 steel\n Production: 1 modernisation tocken, oil -> 4 vp (1x) , modernization_tocken + coil -> upgrade', compensation=compensation1, production=production2)

start_card3 = Manufactories(description='Start card 3\n Compensation: 2 coil\n Production: 1 modernisation tocken, 3 coil -> 4 vp (1x), modernization_tocken + coil -> upgrade', compensation=compensation2, production=production3)

start_card4 = Manufactories(description='Start card 4\n Compensation: 1 modernisation_tocken\n Production: 1 modernisation tocken, coil + steel -> 4 vp (1x), modernization_tocken + coil -> upgrade', compensation=compensation3, production=production4)

start_card5 = Manufactories(description='Start card 2\n Compensation: 2 coil\n Production: 1 modernisation tocken, oil -> 4 vp (1x) , modernization_tocken + coil -> upgrade', compensation=compensation2, production=production5)

start_cards = [start_card1, start_card2, start_card3, start_card4, start_card5]

#cards
comp1 = Effect(steel=1)
comp2 = Effect(funcs=[steel_to_oil])
comp3 = Effect(funcs=[steel_to_mt])
comp4 = Effect(funcs=[coil_to_oil])

prod1 = Effect(coil=2, funcs=[steel_n_oil_to_points_mod])
prod2 = Effect(steel=1, funcs=[mt_to_points_mod])
prod3 = Effect(steel=1, funcs=[coil_n_oil_to_points_mod])
prod4 = Effect(funcs=[steel_to_mt, steel_to_points_4x_mod])
prod5 = Effect(coil=2, funcs=[steel_to_points_4x_mod])
prod6 = Effect(coil=2, funcs=[mt_to_vp_mod])
prod7 = Effect(funcs=[steel_to_points_2x, coil3_mod])
prod8 = Effect(funcs=[coil_to_oil_2x, mt_mod])
prod9 = Effect(steel=1, funcs=[oil_to_points_mod])

card1 = Manufactories(description='Card 1\n Compensation: 2 coil\n Production: 2 coil, (if mod) steel + oil -> 7 vp (2x)', compensation=compensation2, production=prod1)
card2 = Manufactories(description='Card 2\n Compensation: 1 steel\n Production: 1 steel, (if mod) modernisation_tocken -> 5 vp (2x)', compensation=comp1, production=prod2)
card3 = Manufactories(description='Card 3\n Compensation: 2 coil\n Production: 1 steel, (if mod) coil + oil -> 6 vp (2x)', compensation=compensation2, production=prod3)
card4 = Manufactories(description='Card 4\n Compensation: steel -> oil\n Production: steel -> modernisation_tocken (1x), (if mod) steel -> 2 vp (4x)', compensation=comp2, production=prod4)
card5 = Manufactories(description='Card 5\n Compensation: 2 coil\n Production: 2 coil, (if mod) steel -> 2 vp (4x)', compensation=compensation2, production=prod5)
card6 = Manufactories(description='Card 6\n Compensation: 2 coil\n Production: 2 coil, (if mod) modernisation_tocken -> 5 vp (2x)', compensation=compensation2, production=prod6)
card7 = Manufactories(description='Card 7\n Compensation: 2 coil\n Production: steel -> 2 vp (2x), (if mod) 3 coil', compensation=compensation2, production=prod7)
card8 = Manufactories(description='Card 8\n Compensation: steel -> modernisation_tocken\n Production: 2 coil, (if mod) steel -> 2 vp (4x)', compensation=comp3, production=prod5)
card9 = Manufactories(description='Card 9\n Compensation: 2 coil -> oil\n Production: 2 coil -> oil (2x), (if mod) modernisation_tocken', compensation=comp4, production=prod8)
card10 = Manufactories(description='Card 10\n Compensation: 1 steel\n Production: 1 steel, (if mod) oil -> 4 vp (2x)', compensation=comp1, production=prod9)
