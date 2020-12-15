#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

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
    while not currentOption == Generator_Options.Exit.value:
      print_option_list(Generator_Options)
      currentOptionInput = input ("\nChoose a valid option: ")
      currentOption = int(currentOptionInput) if currentOptionInput.isdigit() else 0
      if currentOption == Generator_Options.Generate_Encounter.value:
        currentEncounterInfo = ""
      elif currentOption == Generator_Options.Save_Current_Encounter.value:
        save_output_dialog(currentDirectory, currentEncounterInfo, "Encounter")
      elif currentOption == Generator_Options.Exit.value:
        clear_screen()
      else:
        clear_screen()
        print(currentEncounterInfo) if len(currentEncounterInfo) > 0 else 0
  except KeyboardInterrupt:
    clear_screen()
#--------------------------------------------------#

if __name__ == "__main__":
  main()