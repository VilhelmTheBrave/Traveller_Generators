#!/usr/bin/env python3

from random import randint
from subprocess import call
from platform import system
from os import path,mkdir

def roll_dice(numRolls=1,diceMin=1,diceMax=6):
  curRollCount = 0
  result = 0
  while curRollCount < numRolls:
    result += randint(diceMin, diceMax)
    curRollCount += 1
  return result

def get_table_entry(header, table, index):
  selectedEntry = table[index]
  headerLength = len(header)
  entryString = ""
  i = 0
  while i < headerLength:
    entryString += header[i] + ": " + table[index][i] + "\n"
    i += 1
  return entryString

def convert_slist_to_string(listOfStrings):
  stringListLen = len(listOfStrings)
  retString = ""
  for entry in listOfStrings:
    retString += ", " if len(retString) > 0 and len(entry) > 0 else ""
    retString += entry
  retString = "None" if len(retString) == 0 else retString
  return retString

def clear_screen():
  sysName = system()
  if sysName == 'Windows':
    call("cls", shell=True)
  elif sysName == 'Linux':
    call("clear", shell=True)

def print_option_list(optionList):
  for option in optionList:
    print(str(option.value) + " = " + option.name)

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

def get_cur_dir_path(fileSelfRef):
  return path.dirname(path.realpath(fileSelfRef))