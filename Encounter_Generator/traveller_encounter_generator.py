#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

class ENCOUNTER_OPTIONS(Enum):
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

def generate_encounter():
  clear_screen()
  user_input_dialog(ENCOUNTER_OPTIONS, "Decide which terrain this encounter will take place on.\n")
  return ""

# Main
#--------------------------------------------------#
def main():
  class Generator_Options(Enum):
    Generate_Encounter     = 1
    Save_Current_Encounter = 2
    Exit                   = 3

  try:
    currentDirectory = get_cur_dir_path(__file__)
    clear_screen()
    currentOption = 0
    currentEncounterInfo = ""
    while True:
      print_option_list(Generator_Options)
      currentOptionInput = input ("\nChoose a valid option: ")
      currentOption = int(currentOptionInput) if currentOptionInput.isdigit() else 0
      if currentOption == Generator_Options.Generate_Encounter.value:
        currentEncounterInfo = generate_encounter()
      elif currentOption == Generator_Options.Save_Current_Encounter.value:
        save_output_dialog(currentDirectory, currentEncounterInfo, "Encounter")
      elif currentOption == Generator_Options.Exit.value:
        clear_screen()
        break
      else:
        clear_screen()
        print(currentEncounterInfo) if len(currentEncounterInfo) > 0 else 0
  except KeyboardInterrupt:
    clear_screen()
#--------------------------------------------------#

if __name__ == "__main__":
  main()