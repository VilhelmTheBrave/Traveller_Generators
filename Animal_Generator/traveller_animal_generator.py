#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

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

def generate_animal():
  clear_screen()
  selectedTerrain = user_input_dialog(TERRAIN_OPTIONS, "Decide which terrain this animal resides in.\n")
  return ""

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_world, "Animal")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
