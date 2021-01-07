#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

# Global Enums
#--------------------------------------------------#
class LOCATION_OPTIONS(Enum):
  Random   = 0
  Starport = 1
  Rural    = 2
  Urban    = 3
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

def handle_encounter_activity_gen(funcArgs):
  encounterLocation = funcArgs[0]
  encounterActivity = roll_d_six_six()
  actString  = "Encounter Activity Info\n" + SEPARATOR_STRING
  if encounterLocation == LOCATION_OPTIONS.Starport:
    activityTable = STARPORT_ACTIVITY_TABLE
  elif encounterLocation == LOCATION_OPTIONS.Rural:
    activityTable = RURAL_ACTIVITY_TABLE
  else:
    activityTable = URBAN_ACTIVITY_TABLE
  actString += get_table_entry(ENCOUNTER_ACTIVITY_TABLE_HEADER, activityTable, encounterActivity) + SEPARATOR_STRING
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
      selectedLocation = get_option_by_value(LOCATION_OPTIONS, roll_dice(1,1,3))

    printString = "Encounter Location Info\n" + SEPARATOR_STRING
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
