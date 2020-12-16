#!/usr/bin/env python3

from random import randint
from subprocess import call
from platform import system
from os import path,mkdir
from enum import Enum

# Global vars
#--------------------------------------------------#
SEPARATOR_STRING  = "-----------------------------------\n"
NEW_LINE = "\n"

class GENERATOR_OPTIONS(Enum):
  Generate_Random        = 1
  Interactive_Generation = 2
  Save_Current           = 3
  Exit                   = 4

class INTERACTIVE_GEN_OPTIONS(Enum):
  ReRoll   = 1
  Continue = 2
  Quit     = 3
#--------------------------------------------------#

# Roll a dice, defaults to d6
#--------------------------------------------------#
def roll_dice(numRolls=1,diceMin=1,diceMax=6):
  curRollCount = 0
  result = 0
  while curRollCount < numRolls:
    result += randint(diceMin, diceMax)
    curRollCount += 1
  return result
#--------------------------------------------------#

# Gets an entry from a table
#--------------------------------------------------#
def get_table_entry(header, table, index):
  selectedEntry = table[index]
  headerLength = len(header)
  entryString = ""
  i = 0
  while i < headerLength:
    entryString += header[i] + ": " + table[index][i] + "\n"
    i += 1
  return entryString
#--------------------------------------------------#

# Combines a list of strings into a single string
#--------------------------------------------------#
def convert_slist_to_string(listOfStrings):
  stringListLen = len(listOfStrings)
  retString = ""
  for entry in listOfStrings:
    retString += ", " if len(retString) > 0 and len(entry) > 0 else ""
    retString += entry
  retString = "None" if len(retString) == 0 else retString
  return retString
#--------------------------------------------------#

# Clears the terminal
#--------------------------------------------------#
def clear_screen():
  sysName = system()
  if sysName == 'Windows':
    call("cls", shell=True)
  elif sysName == 'Linux':
    call("clear", shell=True)
#--------------------------------------------------#

# Prints the list of script options
#--------------------------------------------------#
def print_option_list(optionList):
  for option in optionList:
    print(str(option.value) + " = " + option.name)
#--------------------------------------------------#

# Gets the list of valid script option values
#--------------------------------------------------#
def get_option_values(optionList):
  valueList = []
  for option in optionList:
    valueList.append(option.value)
  return valueList
#--------------------------------------------------#

# Prompts the user to save an asset
#--------------------------------------------------#
def save_output_dialog(scriptDir, outputData, outputTypeName):
  try:
    if len(outputData) > 0:
      savedWorldsDir = path.join(scriptDir, "Saved_" + outputTypeName + "s")
      clear_screen()
      saveName = input ("Enter a " + outputTypeName + " name to save: ")
      if len(saveName) > 0:
        if not path.exists(savedWorldsDir):
          mkdir(savedWorldsDir)
        saveTextFileLocation = path.join(savedWorldsDir, saveName + ".txt")
        with open(saveTextFileLocation, "w") as outTextFile:
          outTextFile.write(outputData)
        clear_screen()
        print(outputData + outputTypeName + " Saved\n")
      else:
        clear_screen()
        print(outputData + outputTypeName + " name empty, skipping save\n")
    else:
      clear_screen()
      print("Generate a " + outputTypeName + " first\n")
  except KeyboardInterrupt:
    clear_screen()
    print(outputData + "Failed to save " + outputTypeName + "\n")
#--------------------------------------------------#

# Gets the path to the script directory
#--------------------------------------------------#
def get_cur_dir_path(fileSelfRef):
  return path.dirname(path.realpath(fileSelfRef))
#--------------------------------------------------#

# Prompts the user to choose a script option
#--------------------------------------------------#
def user_input_dialog(genOptions, extraDisplayString):
  currentOption = 0
  valid_option_values = get_option_values(genOptions)
  while not currentOption in valid_option_values:
    clear_screen()
    print(extraDisplayString)
    print_option_list(genOptions)
    currentOptionInput = input ("\nChoose a valid option: ")
    currentOption = int(currentOptionInput) if currentOptionInput.isdigit() else 0
  return currentOption
#--------------------------------------------------#

# Prompts the user to do interactive generation
#--------------------------------------------------#
def do_interactive_gen_loop(interactiveGenOption, loopFunc, funcArgs):
  while True:
    retString, retValue = loopFunc(funcArgs)
    if interactiveGenOption == INTERACTIVE_GEN_OPTIONS.ReRoll.value:
      interactiveGenOption = user_input_dialog(INTERACTIVE_GEN_OPTIONS, retString)
    if interactiveGenOption == INTERACTIVE_GEN_OPTIONS.Continue.value:
      interactiveGenOption = INTERACTIVE_GEN_OPTIONS.ReRoll.value
      break
    elif interactiveGenOption == INTERACTIVE_GEN_OPTIONS.Quit.value:
      break
  return interactiveGenOption, retString, retValue
#--------------------------------------------------#

# Main loop for asset generation
#--------------------------------------------------#
def do_main_loop(scriptSelfRef, primaryGenFunc, assetName):
  try:
    currentDirectory = get_cur_dir_path(scriptSelfRef)
    clear_screen()
    currentOption = 0
    currentAssetInfo = ""
    while True:
      print_option_list(GENERATOR_OPTIONS)
      currentOptionInput = input ("\nChoose a " + assetName + " generation option: ")
      currentOption = int(currentOptionInput) if currentOptionInput.isdigit() else 0
      if currentOption == GENERATOR_OPTIONS.Generate_Random.value:
        currentAssetInfo = primaryGenFunc(INTERACTIVE_GEN_OPTIONS.Quit.value)
      elif currentOption == GENERATOR_OPTIONS.Interactive_Generation.value:
        currentAssetInfo = primaryGenFunc(INTERACTIVE_GEN_OPTIONS.ReRoll.value)
      elif currentOption == GENERATOR_OPTIONS.Save_Current.value:
        save_output_dialog(currentDirectory, currentAssetInfo, assetName)
      elif currentOption == GENERATOR_OPTIONS.Exit.value:
        clear_screen()
        break
      else:
        clear_screen()
        print(currentAssetInfo) if len(currentAssetInfo) > 0 else 0
  except KeyboardInterrupt:
    clear_screen()
#--------------------------------------------------#
