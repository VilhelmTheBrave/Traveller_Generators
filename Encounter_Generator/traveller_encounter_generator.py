#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

# Global Vars
#--------------------------------------------------#
HOSTILE_VESSEL   = "Hostile vessel"
DUMPED_CARGO_POD = "Dumped cargo pod"
ORBITAL_FACTORY  = "Orbital factory"
POSSIBLE_SALVAGE = "possible salvage"
POSSIBLE_MINING  = "possible mining"

class LOCATION_OPTIONS(Enum):
  Random              = 0
  Starport            = 1
  Rural               = 2
  Urban               = 3
  Space_Highport      = 4
  Space_High_Traffic  = 5
  Space_Settled       = 6
  Space_Border_System = 7
  Space_Wild          = 8
  Space_Empty         = 9
#--------------------------------------------------#

# Encounter activities
#--------------------------------------------------#
ENCOUNTER_ACTIVITY_TABLE_HEADER = ["Activity"]

STARPORT_ACTIVITY_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Maintenance robot at work"                                                          ],
  ["Trade ship arrives or departs"                                                      ],
  ["Captain argues about fuel prices"                                                   ],
  ["News report about pirate activity on a starport screen draws a crowd"               ],
  ["Bored clerk makes life diffi cult for the characters"                               ],
  ["Local merchant with cargo to transport seeks a ship"                                ],
  ["None"], ["None"], ["None"], ["None"],
  ["Dissident tries to claim sanctuary from planetary authorities"                      ],
  ["Traders from offworld argue with local brokers"                                     ],
  ["Technician repairing starport computer system"                                      ],
  ["Reporter asks for news from offworld"                                               ],
  ["Bizarre cultural performance"                                                       ],
  ["Patron argues with another group of travellers"                                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Military vessel arrives or departs"                                                 ],
  ["Demonstration outside starport"                                                     ],
  ["Escaped prisoners begs for passage offworld"                                        ],
  ["Impromptu bazaar of bizarre items"                                                  ],
  ["Security patrol"                                                                    ],
  ["Unusual alien"                                                                      ],
  ["None"], ["None"], ["None"], ["None"],
  ["Traders offer spare parts and supplies at cut-price rates"                          ],
  ["Repair yard catches fire"                                                           ],
  ["Passenger liner arrives or departs"                                                 ],
  ["Servant robot offers to guide characters around the spaceport"                      ],
  ["Trader from a distant system selling strange curios"                                ],
  ["Old crippled belter asks for spare change and complains about drones taking his job"],
  ["None"], ["None"], ["None"], ["None"],
  ["Patron offers the characters a job"                                                 ],
  ["Passenger looking for a ship"                                                       ],
  ["Religious pilgrims try to convert the characters"                                   ],
  ["Cargo hauler arrives or departs"                                                    ],
  ["Scout ship arrives or departs"                                                      ],
  ["Illegal or dangerous goods are impounded"                                           ],
  ["None"], ["None"], ["None"], ["None"],
  ["Pickpocket tries to steal from the characters"                                      ],
  ["Drunken crew pick a fight"                                                          ],
  ["Government officials investigate the characters"                                    ],
  ["Random security sweep scans characters & baggage"                                   ],
  ["Starport is temporarily shut down for security reasons"                             ],
  ["Damaged ship makes emergency docking"                                               ])

RURAL_ACTIVITY_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Agricultural robots"                      ],
  ["Crop sprayer drone flies overhead"        ],
  ["Damaged agricultural robot being repaired"],
  ["Small, isolationist community"            ],
  ["Noble hunting party"                      ],
  ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Local landing field"                      ],
  ["Lost child"                               ],
  ["Travelling merchant caravan"              ],
  ["Cargo convoy"                             ],
  ["Police chase"                             ],
  ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Telecommunications black spot"            ],
  ["Security patrol"                          ],
  ["Military facility"                        ],
  ["Bar or waystation"                        ],
  ["Grounded spacecraft"                      ],
  ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Small community – quiet place to live"    ],
  ["Small community – on a trade route"       ],
  ["Small community – festival in progress"   ],
  ["Small community – in danger"              ],
  ["Small community – not what it seems"      ],
  ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Unusual weather"                          ],
  ["Difficult terrain"                        ],
  ["Unusual creature"                         ],
  ["Isolated homestead – welcoming"           ],
  ["Isolated homestead – unfriendly"          ],
  ["None"], ["None"], ["None"], ["None"],
  ["Wild Animal"                              ],
  ["Private villa"                            ],
  ["Monastery or retreat"                     ],
  ["Experimental farm"                        ],
  ["Ruined structure"                         ],
  ["Research facility"                        ])

URBAN_ACTIVITY_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Street riot in progress"                                   ],
  ["Characters pass a charming restaurant"                     ],
  ["Trader in illegal goods"                                   ],
  ["Public argument"                                           ],
  ["Sudden change of weather"                                  ],
  ["NPC asks for the character’s help"                         ],
  ["None"], ["None"], ["None"], ["None"],
  ["Characters pass a bar or pub"                              ],
  ["Characters pass a theatre or other entertainment venue"    ],
  ["Curiosity Shop"                                            ],
  ["Street market stall tries to sell the characters something"],
  ["Fire, dome breach or other emergency in progress"          ],
  ["Attempted robbery of characters"                           ],
  ["None"], ["None"], ["None"], ["None"],
  ["Vehicle accident involving characters"                     ],
  ["Low-flying spacecraft flies overhead"                      ],
  ["Alien or other offworlder"                                 ],
  ["Random NPC bumps into character"                           ],
  ["Pickpocket"                                                ],
  ["Media team or journalist"                                  ],
  ["None"], ["None"], ["None"], ["None"],
  ["Security Patrol"                                           ],
  ["Ancient building or archive"                               ],
  ["Festival"                                                  ],
  ["Someone is following the characters"                       ],
  ["Unusual cultural group or event"                           ],
  ["Planetary official"                                        ],
  ["None"], ["None"], ["None"], ["None"],
  ["Characters spot someone they recognise"                    ],
  ["Public demonstration"                                      ],
  ["Robot or other servant passes characters"                  ],
  ["Prospective patron"                                        ],
  ["Crime such as robbery or attack in progress"               ],
  ["Street preacher rants at the characters"                   ],
  ["None"], ["None"], ["None"], ["None"],
  ["News broadcast on public screens"                          ],
  ["Sudden curfew or other restriction on movement"            ],
  ["Unusually empty or quiet street"                           ],
  ["Public announcement"                                       ],
  ["Sports event"                                              ],
  ["Imperial Dignitary"                                        ])

def get_random_salvage():
  damageMod   = roll_dice(1,0,6)
  salvageRoll = roll_dice(2) - damageMod
  if salvageRoll < 3:
    salvageString = "Hazard!" + NEW_LINE + "Examples: The ship’s reactor is damaged, the ship is about to break up, there is a virus loose aboard ship, an alien monster killed the crew..." + NEW_LINE
  elif salvageRoll == 4:
    salvageString = "Nothing useful can be recovered." + NEW_LINE
  elif salvageRoll == 5:
    salvageString = "Minor personal effects, spare parts, trophies and other junk." + NEW_LINE
  elif salvageRoll == 6:
    salvageString = str(roll_dice(2) * 10) + " tons of fuel can be extracted from the salvage." + NEW_LINE
  elif salvageRoll == 7:
    salvageString = "Equipment like vacc suits, medical supplies or weapons, with a total value of " + str(roll_dice(2) * 2000) + " credits." + NEW_LINE
  elif salvageRoll == 8:
    salvageString = "Cargo" + NEW_LINE + get_random_trade_goods(roll_dice(2))
  elif salvageRoll == 9:
    salvageString = "Considerable Cargo" + NEW_LINE + get_random_trade_goods(roll_dice(2) * 10)
  elif salvageRoll == 10:
    salvageString = "An alien relic, useful personal data, mail cannister or other adventure hook – or a survivor in a low berth." + NEW_LINE
  elif salvageRoll == 11:
    salvageString = "Weapon turrets, ship’s computers or vehicles, with a total value of " + str(roll_dice(2) * 25000) + " credits." + NEW_LINE
  else:
    salvageString = "The ship is potentially repairable." + NEW_LINE
  return "Salvage: " + salvageString

def get_random_mining():
  miningRoll = roll_dice(2)
  if miningRoll == 2:
    miningString = str(roll_dice(2)) + " tons of crystals and gems"
  elif miningRoll in (3,4):
    miningString = str(roll_dice(2) * 20) + " tons of common ore"
  elif miningRoll in (5,6):
    miningString = str(roll_dice(2) * 50) + " tons of common ore"
  elif miningRoll in (7,8):
    miningString = str(roll_dice(2) * 10) + " tons of uncommon ore"
  elif miningRoll in (9,10,11):
    miningString = str(roll_dice(2) * 20) + " tons of uncommon ore"
  else:
    miningString = str(roll_dice()) + " tons of radioactives"
  return "Mining: " + miningString + NEW_LINE

def get_space_activity(location):
  alienVesselRoll = roll_dice()
  if alienVesselRoll <= 3:
    alienVesselType = "trader"
  elif alienVesselRoll <= 5:
    alienVesselType = "explorer"
  else:
    alienVesselType = "spy"

  activityTable = ("",
                   "Alien derelict (" + POSSIBLE_SALVAGE + ")"                                                 ,
                   "Solar Flare (unignorable - " + str(roll_dice() * 100) + " rads)"                           ,
                   "Asteroid (empty rock)"                                                                     ,
                   "Ore-bearing asteroid (" + POSSIBLE_MINING + ")"                                            ,
                   "Alien vessel on a mission"                                                                 ,
                   "Rock hermit (inhabited rock)"                                                              ,
                   "", "", "", "",
                   "Pirate (unignorable)"                                                                      ,
                   "Derelict vessel (" + POSSIBLE_SALVAGE + ")"                                                ,
                   "Derelict space station (" + POSSIBLE_SALVAGE + ")" if roll_dice() < 5 else "Space station" ,
                   "Comet (may be ancient derelict at its core)"                                               ,
                   "Ore-bearing asteroid (" + POSSIBLE_MINING + ")"                                            ,
                   "Ship in distress"                                                                          ,
                   "", "", "", "",
                   "Pirate"                                                                                    ,
                   "Free trader"                                                                               ,
                   "Micrometeorite storm (unignorable collision - " + str(roll_dice(2)) + " damage)"           ,
                   HOSTILE_VESSEL                                                                              ,
                   "Mining ship"                                                                               ,
                   "Scout ship"                                                                                ,
                   "", "", "", "",
                   "Alien vessel (" + alienVesselType + ")"                                                    ,
                   "Space junk (" + POSSIBLE_SALVAGE + ")"                                                     ,
                   "Far trader"                                                                                ,
                   "Derelict vessel (" + POSSIBLE_SALVAGE + ")"                                                ,
                   "Safari or science vessel"                                                                  ,
                   "Escape pod"                                                                                ,
                   "", "", "", "",
                   "Passenger liner"                                                                           ,
                   "Ship in distress"                                                                          ,
                   "Colony ship or passenger liner"                                                            ,
                   "Scout ship"                                                                                ,
                   "Space station"                                                                             ,
                   "X-boat courier"                                                                            ,
                   "", "", "", "",
                   HOSTILE_VESSEL                                                                              ,
                   "Garbage ejected from a ship"                                                               ,
                   "Medical ship or hospital"                                                                  ,
                   "Lab ship or scout"                                                                         ,
                   PATRON                                                                                      ,
                   "Police ship"                                                                               ,
                   "", "", "", "",
                   "Unusually daring pirate"                                                                   ,
                   "Noble yacht"                                                                               ,
                   "Warship"                                                                                   ,
                   "Cargo vessel"                                                                              ,
                   "Navigational buoy or beacon"                                                               ,
                   "Unusual ship"                                                                              ,
                   "", "", "", "",
                   "Collision with space junk (unignorable collision - " + str(roll_dice(2)) + " damage)"      ,
                   "Automated vessel"                                                                          ,
                   "Free trader"                                                                               ,
                   DUMPED_CARGO_POD                                                                            ,
                   "Police vessel"                                                                             ,
                   "Cargo hauler"                                                                              ,
                   "", "", "", "",
                   "Passenger liner"                                                                           ,
                   ORBITAL_FACTORY                                                                             ,
                   "Orbital habitat"                                                                           ,
                   "Orbital habitat"                                                                           ,
                   "Communications satellite"                                                                  ,
                   "Defence satellite"                                                                         ,
                   "", "", "", "",
                   "Pleasure craft"                                                                            ,
                   "Space station"                                                                             ,
                   "Police vessel"                                                                             ,
                   "Cargo hauler"                                                                              ,
                   "System defence boat"                                                                       ,
                   "Grand fleet warship"                                                                       )
  
  if location == LOCATION_OPTIONS.Space_Highport:
    activityMod = 3
  elif location == LOCATION_OPTIONS.Space_High_Traffic:
    activityMod = 2
  elif location == LOCATION_OPTIONS.Space_Settled:
    activityMod = 1
  elif location == LOCATION_OPTIONS.Space_Border_System:
    activityMod = 0
  elif location == LOCATION_OPTIONS.Space_Wild:
    activityMod = -1
  else:
    activityMod = -4
  
  spaceActivity = roll_d_six_six(activityMod)

  activityString = "Activity: "
  chosenActivity = activityTable[spaceActivity]
  if chosenActivity == HOSTILE_VESSEL:
    chosenVessel = activityTable[roll_d_six_six(activityMod)]
    while True:
      if ("vessel" in chosenVessel) and ("Derelict" not in chosenVessel) and ("Hostile" not in chosenVessel):
        break
      elif ("ship" in chosenVessel) and ("Garbage" not in chosenVessel) and ("distress" not in chosenVessel):
        break
      elif "Pirate" in chosenVessel:
        break
      else:
        chosenVessel = activityTable[roll_d_six_six(activityMod)]
    activityString += chosenActivity + " - " + chosenVessel + (" (unignorable)" if "unignorable" not in chosenVessel else "") + NEW_LINE
  elif chosenActivity == PATRON:
    activityString += chosenActivity + " - " + MISSION_PATRON_TABLE[roll_d_six_six()][0] + " (unignorable)" + NEW_LINE
  elif chosenActivity == DUMPED_CARGO_POD or chosenActivity == ORBITAL_FACTORY:
    activityString += chosenActivity + NEW_LINE + get_random_trade_goods()
  elif POSSIBLE_SALVAGE in chosenActivity:
    activityString += chosenActivity + NEW_LINE + get_random_salvage()
  elif POSSIBLE_MINING in chosenActivity:
    activityString += chosenActivity + NEW_LINE + get_random_mining()
  else:
    activityString += chosenActivity + NEW_LINE
  activityString += SEPARATOR_STRING

  return activityString

def handle_encounter_activity_gen(funcArgs):
  encounterLocation = funcArgs[0]
  encounterActivity = roll_d_six_six()
  actString         = "Encounter Activity Info\n" + SEPARATOR_STRING
  if encounterLocation == LOCATION_OPTIONS.Starport:
    actString +=  get_table_entry(ENCOUNTER_ACTIVITY_TABLE_HEADER, STARPORT_ACTIVITY_TABLE, encounterActivity) + SEPARATOR_STRING
  elif encounterLocation == LOCATION_OPTIONS.Rural:
    actString +=  get_table_entry(ENCOUNTER_ACTIVITY_TABLE_HEADER, RURAL_ACTIVITY_TABLE, encounterActivity) + SEPARATOR_STRING
  elif encounterLocation == LOCATION_OPTIONS.Urban:
    actString +=  get_table_entry(ENCOUNTER_ACTIVITY_TABLE_HEADER, URBAN_ACTIVITY_TABLE, encounterActivity) + SEPARATOR_STRING
  else:
    actString += get_space_activity(encounterLocation)
  return actString, encounterActivity
#--------------------------------------------------#

# Generate a new encounter
#--------------------------------------------------#
def generate_encounter(encounterGenOption):
  try:
    # Location
    if encounterGenOption == INTERACTIVE_GEN_OPTIONS.ReRoll:
      selectedLocation = user_input_dialog(LOCATION_OPTIONS, "Decide which location this encounter will take place in.\n")
    else:
      selectedLocation = LOCATION_OPTIONS.Random
    
    if selectedLocation == LOCATION_OPTIONS.Random:
      selectedLocation = get_option_by_value(LOCATION_OPTIONS, roll_dice(1,1,9))

    printString  = "Encounter Location Info\n" + SEPARATOR_STRING
    printString += "Location: " + selectedLocation.name  + NEW_LINE + SEPARATOR_STRING + NEW_LINE

    # Activity
    encounterGenOption, locationString, encounterLocation = do_interactive_gen_loop(encounterGenOption, handle_encounter_activity_gen, [selectedLocation])
    printString += locationString + NEW_LINE

    clear_screen()
    print(printString)

  except KeyboardInterrupt:
    clear_screen()
    print("Failed to generate Encounter\n")
    printString = ""

  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_encounter, "Encounter")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
