#!/usr/bin/env python3

from random import randint
from subprocess import call
from platform import system
from os import path,mkdir
from enum import Enum

# Global vars
#--------------------------------------------------#
SEPARATOR_STRING    = "-----------------------------------\n"
NEW_LINE            = "\n"
PATRON              = "Patron"

TRADE_GOODS_TABLE_HEADER = ("Trade Good Type", "Available", "Tons", "Base Price (Cr)", "Purchase DM", "Sale DM")

MISSION_PATRON_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Assassin"                          ],
  ["Smuggler"                          ],
  ["Terrorist"                         ],
  ["Embezzler"                         ],
  ["Thief"                             ],
  ["Revolutionary"                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Clerk"                             ],
  ["Administrator"                     ],
  ["Mayor"                             ],
  ["Minor Noble"                       ],
  ["Physician"                         ],
  ["Tribal Leader"                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Diplomat"                          ],
  ["Courier"                           ],
  ["Spy"                               ],
  ["Ambassador"                        ],
  ["Noble"                             ],
  ["Police Officer"                    ],
  ["None"], ["None"], ["None"], ["None"],
  ["Merchant"                          ],
  ["Free Trader"                       ],
  ["Broker"                            ],
  ["Corporate Executive"               ],
  ["Corporate Agent"                   ],
  ["Financier"                         ],
  ["None"], ["None"], ["None"], ["None"],
  ["Belter"                            ],
  ["Researcher"                        ],
  ["Naval Officer"                     ],
  ["Pilot"                             ],
  ["Starport Administrator"            ],
  ["Scout"                             ],
  ["None"], ["None"], ["None"], ["None"],
  ["Alien"                             ],
  ["Playboy"                           ],
  ["Stowaway"                          ],
  ["Family Relative"                   ],
  ["Agent of a Foreign Power"          ],
  ["Imperial Agent"                    ])

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

# Rolls d66
#--------------------------------------------------#
def roll_d_six_six(tensMod=0):
  tensNum = roll_dice() + tensMod
  tensNum = 0 if tensNum < 0 else tensNum
  return int(str(tensNum) + str(roll_dice()))
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

# Clears the terminal
#--------------------------------------------------#
def clear_screen():
  sysName = system()
  if sysName == 'Windows':
    call("cls", shell=True)
  elif sysName == 'Linux':
    call("clear", shell=True)
  else:
    0 # Do Nothing
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

# Gets an option using its value
#--------------------------------------------------#
def get_option_by_value(optionList, optionValue):
  retOption = 999
  for option in optionList:
    retOption = option if option.value == optionValue else retOption
  return retOption
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
  currentOption = 999
  valid_option_values = get_option_values(genOptions)
  while not currentOption in valid_option_values:
    clear_screen()
    print(extraDisplayString)
    print_option_list(genOptions)
    currentOptionInput = input ("\nChoose a valid option: ")
    currentOption = int(currentOptionInput) if currentOptionInput.isdigit() else 999
  selectedOption = get_option_by_value(genOptions, currentOption)
  return selectedOption
#--------------------------------------------------#

# Prompts the user to do interactive generation
#--------------------------------------------------#
def do_interactive_gen_loop(interactiveGenOption, loopFunc, funcArgs):
  while True:
    retString, retValue = loopFunc(funcArgs)
    if interactiveGenOption == INTERACTIVE_GEN_OPTIONS.ReRoll:
      interactiveGenOption = user_input_dialog(INTERACTIVE_GEN_OPTIONS, retString)
    if interactiveGenOption == INTERACTIVE_GEN_OPTIONS.Continue:
      interactiveGenOption = INTERACTIVE_GEN_OPTIONS.ReRoll
      break
    elif interactiveGenOption == INTERACTIVE_GEN_OPTIONS.Quit:
      break
  return interactiveGenOption, retString, retValue
#--------------------------------------------------#

# Main loop for asset generation
#--------------------------------------------------#
def do_main_loop(scriptSelfRef, primaryGenFunc, assetName):
  try:
    currentDirectory = get_cur_dir_path(scriptSelfRef)
    clear_screen()
    currentOption = 999
    currentAssetInfo = ""
    while True:
      print_option_list(GENERATOR_OPTIONS)
      currentOptionInput = input ("\nChoose a " + assetName + " generation option: ")
      currentOption = get_option_by_value(GENERATOR_OPTIONS, int(currentOptionInput)) if currentOptionInput.isdigit() else 999
      if currentOption == GENERATOR_OPTIONS.Generate_Random:
        currentAssetInfo = primaryGenFunc(INTERACTIVE_GEN_OPTIONS.Quit)
      elif currentOption == GENERATOR_OPTIONS.Interactive_Generation:
        currentAssetInfo = primaryGenFunc(INTERACTIVE_GEN_OPTIONS.ReRoll)
      elif currentOption == GENERATOR_OPTIONS.Save_Current:
        save_output_dialog(currentDirectory, currentAssetInfo, assetName)
      elif currentOption == GENERATOR_OPTIONS.Exit:
        clear_screen()
        break
      else:
        clear_screen()
        print(currentAssetInfo) if len(currentAssetInfo) > 0 else 0
  except KeyboardInterrupt:
    clear_screen()
#--------------------------------------------------#

# Gets an entry from the random trade goods table
#--------------------------------------------------#
def get_random_trade_goods():
  tradeTable = (("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Basic Electronics"        , "All", str(roll_dice() * 10), "10000", "Industrial +2, High Technology +3, Rich +1"             , "Non-Industrial +2, Low Technology +1, Poor +1"                  ),
                ("Basic Machine Parts"      , "All", str(roll_dice() * 10), "10000", "Non-Agricultural +2, Industrial +5"                     , "Non-Industrial +3, Agricultural +2"                             ),
                ("Basic Manufactured Goods" , "All", str(roll_dice() * 10), "10000", "Non-Agricultural +2, Industrial +5"                     , "Non-Industrial +3, High Population +2"                          ),
                ("Basic Raw Materials"      , "All", str(roll_dice() * 10), "5000" , "Agricultural +3, Garden +2"                             , "Industrial +2, Poor +2"                                         ),
                ("Basic Consumables"        , "All", str(roll_dice() * 10), "2000" , "Agricultural +3, Water World +2, Garden +1, Asteroid -4", "Asteroid +1, Fluid Oceans +1, Ice-Capped +1, High Population +1"),
                ("Basic Ore"                , "All", str(roll_dice() * 10), "1000" , "Asteroid +4, Ice-Capped +0"                             , "Industrial +3, Non-Industrial +1"                               ),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Advanced Electronics"       , "Industrial, High Technology", str(roll_dice() * 5), "100000", "Industrial +2, High Technology +3", "Non-Industrial +1, Rich +2, Asteroid +3"),
                ("Advanced Machine Parts"     , "Industrial, High Technology", str(roll_dice() * 5), "75000" , "Industrial +2, High Technology +1", "Asteroid +2, Non-Industrial +1"         ),
                ("Advanced Manufactured Goods", "Industrial, High Technology", str(roll_dice() * 5), "100000", "Industrial +1, High Technology +0", "High Population +1, Rich +2"            ),
                ("Advanced Weapons"           , "Industrial, High Technology", str(roll_dice() * 5), "150000", "Industrial +0, High Technology +2", "Poor +1, Amber Zone +2, Red Zone +4"    ),
                ("Advanced Vehicles"          , "Industrial, High Technology", str(roll_dice() * 5), "180000", "Industrial +0, High Technology +2", "Asteroid +2, Rich +2"                   ),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Biochemicals"      , "Agricultural, Water World"        , str(roll_dice() * 5) , "50000" , "Agricultural +1, Water World +2"           , "Industrial +2"                      ),
                ("Crystals and Gems" , "Asteroid, Desert, Ice-Capped"     , str(roll_dice() * 5) , "20000" , "Asteroid +2, Desert +1, Ice-Capped +1"     , "Industrial +3, Rich +2"             ),
                ("Cybernetics"       , "High Technology"                  , str(roll_dice())     , "250000", "High Technology +0"                        , "Asteroid +1, Ice-Capped +1, Rich +2"),
                ("Live Animals"      , "Agricultural, Garden"             , str(roll_dice() * 10), "10000" , "Agricultural +0, Garden +0"                , "Low Population +3"                  ),
                ("Luxury Consumables", "Agricultural, Garden, Water World", str(roll_dice() * 10), "20000" , "Agricultural +2, Garden +0, Water World +1", "Rich +2, High Technology +2"        ),
                ("Luxury Goods"      , "High Population"                  , str(roll_dice())     , "200000", "High Population +0"                        , "Rich +4"                            ),
                ("Medical Supplies"  , "High Technology, High Population" , str(roll_dice() * 5) , "50000" , "High Technology +2, High Population +0"    , "Industrial +2, Poor +1, Rich +1"    ),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Petrochemicals" , "Desert, Fluid Ocean, Ice-Capped, Water World"  , str(roll_dice() * 10), "10000"   , "Desert +2, Fluid Oceans +0, Ice-Capped +0, Water World +0" , "Industrial +2, Agricultural +1, Low Technology +2"                    ),
                ("Pharmaceuticals", "Asteroid, Desert, High Population, Water World", str(roll_dice())     , "100000"  , "Asteroid +2, Desert +0, High Population +1, Water World +0", "Rich +2, Low Technology +2"                                           ),
                ("Polymers"       , "Industrial"                                    , str(roll_dice() * 10), "7000"    , "Industrial +0"                                             , "Rich +2, Non-Industrial +1"                                           ),
                ("Precious Metals", "Asteroid, Desert, Ice-Capped, Fluid Oceans"    , str(roll_dice())     , "50000"   , "Asteroid +3, Desert +1, Ice-Capped +2, Fluid Oceans +0"    , "Rich +3, Industrial +2, High Technology +1"                           ),
                ("Radioactives"   , "Asteroid, Desert, Low Population"              , str(roll_dice())     , "1000000" , "Asteroid +2, Desert +0, Low Population -4"                 , "Industrial +3, High Technology +1, Non-Industrial -2, Agricultural -3"),
                ("Robots"         , "Industrial, High Technology"                   , str(roll_dice() * 5) , "400000"  , "Industrial +0"                                             , "Agricultural +2, High Technology +1"                                  ),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Spices"                , "Garden, Desert, Water World"      , str(roll_dice() * 5) , "6000" , "Garden +0, Desert +2, Water World +0"      , "High Population +2, Rich +3, Poor +3"   ),
                ("Textiles"              , "Agricultural, Non-Industrial"     , str(roll_dice() * 10), "3000" , "Agricultural +7, Non-Industrial +0"        , "High Population +3, Non-Agricultural +2"),
                ("Uncommon Ore"          , "Asteroid, Ice-Capped"             , str(roll_dice() * 10), "5000" , "Asteroid +4, Ice-Capped +0"                , "Industrial +3, Non-Industrial +1"       ),
                ("Uncommon Raw Materials", "Agricultural, Desert, Water World", str(roll_dice() * 10), "20000", "Agricultural +2, Desert +0, Water World +1", "Industrial +2, High Technology +1"      ),
                ("Wood"                  , "Agricultural, Garden"             , str(roll_dice() * 10), "1000" , "Agricultural +6, Garden +0"                , "Rich +2, Industrial +1"                 ),
                ("Vehicles"              , "Industrial, High Technology"      , str(roll_dice() * 10), "15000", "Industrial +2, High Technology +1"         , "Non-Industrial +2, High Population +1"  ),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("", "", "", "", "", ""),
                ("Illegal Biochemicals", "Agricultural, Water World"                     , str(roll_dice() * 5), "50000" , "Agricultural +0, Water World +2"                  , "Industrial +6"                                                  ),
                ("Illegal Cybernetics" , "High Technology"                               , str(roll_dice())    , "250000", "High Technology +0"                               , "Asteroid +4, Ice-Capped +4, Rich +8, Amber Zone +6, Red Zone +6"),
                ("Illegal Drugs"       , "Asteroid, Desert, High Population, Water World", str(roll_dice())    , "100000", "Asteroid +0, Desert +0, Garden +0, Water World +0", "Rich +6, High Population +6"                                    ),
                ("Illegal Luxuries"    , "Agricultural, Garden, Water World"             , str(roll_dice())    , "50000" , "Agricultural +2, Garden +0, Water World +1"       , "Rich +6, High Population +4"                                    ),
                ("Illegal Weapons"     , "Industrial, High Technology"                   , str(roll_dice() * 5), "150000", "Industrial +0, High Technology +2"                , "Poor +6, Amber Zone +8, Red Zone +10"                           ),
                ("Exotics"             , "Varies"                                        , "Varies"            , "Varies", "Varies"                                           , "Varies"                                                         ))
  return get_table_entry(TRADE_GOODS_TABLE_HEADER, tradeTable, roll_d_six_six())
#--------------------------------------------------#
