#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

# Creature Movement
#--------------------------------------------------#
CREATURE_MOVEMENT_TABLE_HEADER = ["Creature Movement"]

CLEAR_JUNGLE_MOVEMENT_TABLE  = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Walk +2"], ["Fly -6" ])
PLAIN_MOVEMENT_TABLE         = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk +2"], ["Walk +4"], ["Fly -6" ])
DESERT_FOREST_MOVEMENT_TABLE = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
HILLS_ROUGH_MOVEMENT_TABLE   = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk +2"], ["Fly -4" ], ["Fly -6" ])
WOODS_MOVEMENT_TABLE         = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Walk"   ], ["Fly -6" ])
SWAMP_MOVEMENT_TABLE         = (["Swim -6"], ["Amphibious +2"], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
BEACH_MOVEMENT_TABLE         = (["Swim +1"], ["Amphibious +2"], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
RIVERBANK_MOVEMENT_TABLE     = (["Swim -4"], ["Amphibious"   ], ["Walk"   ], ["Walk"   ], ["Walk"   ], ["Fly -6" ])
SHALLOWS_MOVEMENT_TABLE      = (["Swim +4"], ["Swim +2"      ], ["Swim"   ], ["Swim"   ], ["Fly -4" ], ["Fly -6" ])
OPEN_MOVEMENT_TABLE          = (["Swim +6"], ["Swim +4"      ], ["Swim +2"], ["Swim"   ], ["Fly -4" ], ["Fly -6" ])
DEEP_MOVEMENT_TABLE          = (["Swim +8"], ["Swim +6"      ], ["Swim +4"], ["Swim +2"], ["Swim"   ], ["Swim -2"])

def gen_creature_movement():
  return roll_dice()
#--------------------------------------------------#

class TERRAIN_OPTIONS(Enum):
  Clear           = 1
  Plain_Prairie   = 2
  Desert          = 3
  Hills_Foothills = 4
  Mountain        = 5
  forest          = 6
  Woods           = 7
  Jungle          = 8
  Rainforest      = 9
  Rough_Broken    = 10
  Swamp_Marsh     = 11
  Beach_Shore     = 12
  Riverbank       = 13
  Ocean_Shallows  = 14
  Open_Ocean      = 15
  Deep_Ocean      = 16

def generate_creature(creatureGenOption):
  clear_screen()
  selectedTerrain = user_input_dialog(TERRAIN_OPTIONS, "Decide which terrain this creature resides in.\n")


  return ""

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_creature, "Creature")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
