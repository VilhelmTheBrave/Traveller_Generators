#!/usr/bin/env python3

from sys import path

path.append("..")
from support_functions import *

# Global Vars
#--------------------------------------------------#
OPPOSITION          = "Opposition"
COMMON_TRADE_GOODS  = "Common Trade Goods"
RANDOM_TRADE_GOODS  = "Random Trade Goods"
ILLEGAL_TRADE_GOODS = "Illegal Trade Goods"
#--------------------------------------------------#

# Mission patron
#--------------------------------------------------#
MISSION_PATRON_TABLE_HEADER = [PATRON]

def handle_mission_patron_gen(funcArgs):
  missionPatron = roll_d_six_six()
  patronString  = "Mission Patron Info\n" + SEPARATOR_STRING
  patronString += get_table_entry(MISSION_PATRON_TABLE_HEADER, MISSION_PATRON_TABLE, missionPatron) + SEPARATOR_STRING
  return patronString, missionPatron
#--------------------------------------------------#

# Mission objective
#--------------------------------------------------#
MISSION_OBJECTIVE_TABLE_HEADER = ["Objective"]

MISSION_OBJECTIVE_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Assassinate a target"                                     ],
  ["Frame a target"                                           ],
  ["Destroy a target"                                         ],
  ["Steal from a target"                                      ],
  ["Aid in a burglary"                                        ],
  ["Stop a burglary"                                          ],
  ["None"], ["None"], ["None"], ["None"],
  ["Retrieve data or an object from a secure facility"        ],
  ["Discredit a target"                                       ],
  ["Find a lost cargo"                                        ],
  ["Find a lost person"                                       ],
  ["Deceive a target"                                         ],
  ["Sabotage a target"                                        ],
  ["None"], ["None"], ["None"], ["None"],
  ["Transport goods"                                          ],
  ["Transport a person"                                       ],
  ["Transport data"                                           ],
  ["Transport goods secretly"                                 ],
  ["Transport goods quickly"                                  ],
  ["Transport dangerous goods"                                ],
  ["None"], ["None"], ["None"], ["None"],
  ["Investigate a crime"                                      ],
  ["Investigate a theft"                                      ],
  ["Investigate a murder"                                     ],
  ["Investigate a mystery"                                    ],
  ["Investigate a target"                                     ],
  ["Investigate an event"                                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Join an expedition"                                       ],
  ["Survey a planet"                                          ],
  ["Explore a new system"                                     ],
  ["Explore a ruin"                                           ],
  ["Salvage a ship"                                           ],
  ["Capture a creature"                                       ],
  ["None"], ["None"], ["None"], ["None"],
  ["Hijack a ship"                                            ],
  ["Entertain a noble"                                        ],
  ["Protect a target"                                         ],
  ["Save a target"                                            ],
  ["Aid a target"                                             ],
  ["It’s a trap – the patron intends to betray the characters"])

def handle_mission_obj_gen(funcArgs):
  missionObj = roll_d_six_six()
  objString  = "Mission Objective Info\n" + SEPARATOR_STRING
  objString += get_table_entry(MISSION_OBJECTIVE_TABLE_HEADER, MISSION_OBJECTIVE_TABLE, missionObj) + SEPARATOR_STRING
  return objString, missionObj
#--------------------------------------------------#

# Mission target
#--------------------------------------------------#
MISSION_TARGET_TABLE_HEADER = ["Target"]

MISSION_TARGET_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  [COMMON_TRADE_GOODS                  ],
  [COMMON_TRADE_GOODS                  ],
  [RANDOM_TRADE_GOODS                  ],
  [RANDOM_TRADE_GOODS                  ],
  [ILLEGAL_TRADE_GOODS                 ],
  [ILLEGAL_TRADE_GOODS                 ],
  ["None"], ["None"], ["None"], ["None"],
  ["Computer Data"                     ],
  ["Alien Artefact"                    ],
  ["Personal Effects"                  ],
  ["Work of Art"                       ],
  ["Historical Artifact"               ],
  ["Weapon"                            ],
  ["None"], ["None"], ["None"], ["None"],
  ["Starport"                          ],
  ["Asteroid Base"                     ],
  ["City"                              ],
  ["Research station"                  ],
  ["Bar or Nightclub"                  ],
  ["Medical Facility"                  ],
  ["None"], ["None"], ["None"], ["None"],
  [PATRON                              ],
  [PATRON                              ],
  [PATRON                              ],
  [OPPOSITION                          ],
  [OPPOSITION                          ],
  [OPPOSITION                          ],
  ["None"], ["None"], ["None"], ["None"],
  ["Local Government"                  ],
  ["Planetary Government"              ],
  ["Corporation"                       ],
  ["Imperial Intelligence"             ],
  ["Criminal Syndicate"                ],
  ["Criminal Gang"                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Free Trader"                       ],
  ["Yacht"                             ],
  ["Cargo Hauler"                      ],
  ["Police Cutter"                     ],
  ["Space Station"                     ],
  ["Warship"                           ])

def get_common_trade_goods():
  tradeTable = (("Basic Electronics"        , "All", str(roll_dice() * 10), "10000", "Industrial +2, High Technology +3, Rich +1"             , "Non-Industrial +2, Low Technology +1, Poor +1"                  ),
                ("Basic Machine Parts"      , "All", str(roll_dice() * 10), "10000", "Non-Agricultural +2, Industrial +5"                     , "Non-Industrial +3, Agricultural +2"                             ),
                ("Basic Manufactured Goods" , "All", str(roll_dice() * 10), "10000", "Non-Agricultural +2, Industrial +5"                     , "Non-Industrial +3, High Population +2"                          ),
                ("Basic Raw Materials"      , "All", str(roll_dice() * 10), "5000" , "Agricultural +3, Garden +2"                             , "Industrial +2, Poor +2"                                         ),
                ("Basic Consumables"        , "All", str(roll_dice() * 10), "2000" , "Agricultural +3, Water World +2, Garden +1, Asteroid -4", "Asteroid +1, Fluid Oceans +1, Ice-Capped +1, High Population +1"),
                ("Basic Ore"                , "All", str(roll_dice() * 10), "1000" , "Asteroid +4, Ice-Capped +0"                             , "Industrial +3, Non-Industrial +1"                               ))
  return get_table_entry(TRADE_GOODS_TABLE_HEADER, tradeTable, roll_dice(1,0,5))

def get_illegal_trade_goods():
  tradeTable = (("Illegal Biochemicals", "Agricultural, Water World"                     , str(roll_dice() * 5), "50000" , "Agricultural +0, Water World +2"                  , "Industrial +6"                                                  ),
                ("Illegal Cybernetics" , "High Technology"                               , str(roll_dice())    , "250000", "High Technology +0"                               , "Asteroid +4, Ice-Capped +4, Rich +8, Amber Zone +6, Red Zone +6"),
                ("Illegal Drugs"       , "Asteroid, Desert, High Population, Water World", str(roll_dice())    , "100000", "Asteroid +0, Desert +0, Garden +0, Water World +0", "Rich +6, High Population +6"                                    ),
                ("Illegal Luxuries"    , "Agricultural, Garden, Water World"             , str(roll_dice())    , "50000" , "Agricultural +2, Garden +0, Water World +1"       , "Rich +6, High Population +4"                                    ),
                ("Illegal Weapons"     , "Industrial, High Technology"                   , str(roll_dice() * 5), "150000", "Industrial +0, High Technology +2"                , "Poor +6, Amber Zone +8, Red Zone +10"                           ))
  return get_table_entry(TRADE_GOODS_TABLE_HEADER, tradeTable, roll_dice(1,0,4))

def handle_mission_target_gen(funcArgs):
  missiontarget    = roll_d_six_six()
  targetString     = "Mission Target Info\n" + SEPARATOR_STRING
  tempTargetString = get_table_entry(MISSION_TARGET_TABLE_HEADER, MISSION_TARGET_TABLE, missiontarget)
  if PATRON in tempTargetString:
    targetString += get_table_entry(MISSION_PATRON_TABLE_HEADER, MISSION_PATRON_TABLE, roll_d_six_six())
  elif OPPOSITION in tempTargetString:
    targetString += get_table_entry(MISSION_OPPOSITION_TABLE_HEADER, MISSION_OPPOSITION_TABLE, roll_d_six_six())
  elif COMMON_TRADE_GOODS in tempTargetString:
    targetString += get_common_trade_goods()
  elif RANDOM_TRADE_GOODS in tempTargetString:
    targetString += get_random_trade_goods()
  elif ILLEGAL_TRADE_GOODS in tempTargetString:
    targetString += get_illegal_trade_goods()
  else:
    targetString += tempTargetString
  targetString += SEPARATOR_STRING
  return targetString, missiontarget
#--------------------------------------------------#

# Mission opposition
#--------------------------------------------------#
MISSION_OPPOSITION_TABLE_HEADER = [OPPOSITION]

MISSION_OPPOSITION_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Animals"                               ],
  ["Large animal"                          ],
  ["Bandits and thieves"                   ],
  ["Fearful peasants"                      ],
  ["Local authorities"                     ],
  ["Local lord"                            ],
  ["None"], ["None"], ["None"], ["None"],
  ["Criminals – thugs or corsairs"         ],
  ["Criminals – thieves or saboteurs"      ],
  ["Police – ordinary security forces"     ],
  ["Police – inspectors and detectives"    ],
  ["Corporate – agents"                    ],
  ["Corporate – legal"                     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Starport security"                     ],
  ["Imperial marines"                      ],
  ["Interstellar corporation"              ],
  ["Alien – private citizen or corporation"],
  ["Alien – government"                    ],
  ["Space travellers or rival ship"        ],
  ["None"], ["None"], ["None"], ["None"],
  ["Target is in deep space"               ],
  ["Target is in orbit"                    ],
  ["Hostile weather conditions"            ],
  ["Dangerous organisms or radiation"      ],
  ["Target is in a dangerous region"       ],
  ["Target is in a restricted area"        ],
  ["None"], ["None"], ["None"], ["None"],
  ["Target is under electronic observation"],
  ["Hostile guard robots or ships"         ],
  ["Biometric identification required"     ],
  ["Mechanical failure or computer hacking"],
  ["Characters are under surveillance"     ],
  ["Out of fuel or ammunition"             ],
  ["None"], ["None"], ["None"], ["None"],
  ["Police investigation"                  ],
  ["Legal barriers"                        ],
  ["Nobility"                              ],
  ["Government officials"                  ],
  ["Target is protected by a third party"  ],
  ["Hostages"                              ])

def handle_mission_opp_gen(funcArgs):
  missionOpp = roll_d_six_six()
  oppString  = "Mission Opposition Info\n" + SEPARATOR_STRING
  oppString += get_table_entry(MISSION_OPPOSITION_TABLE_HEADER, MISSION_OPPOSITION_TABLE, missionOpp) + SEPARATOR_STRING
  return oppString, missionOpp
#--------------------------------------------------#

# Generate a new mission
#--------------------------------------------------#
def generate_mission(missionGenOption):
  try:
    # Patron
    noArgs = []
    missionGenOption, patronString, missionPatron = do_interactive_gen_loop(missionGenOption, handle_mission_patron_gen, noArgs)
    printString = patronString + NEW_LINE

    # Objective
    missionGenOption, objString, missionObj = do_interactive_gen_loop(missionGenOption, handle_mission_obj_gen, noArgs)
    printString += objString + NEW_LINE

    # Target
    missionGenOption, targetString, missiontarget = do_interactive_gen_loop(missionGenOption, handle_mission_target_gen, noArgs)
    printString += targetString + NEW_LINE

    # Target
    missionGenOption, oppString, missionOpp = do_interactive_gen_loop(missionGenOption, handle_mission_opp_gen, noArgs)
    printString += oppString + NEW_LINE

    clear_screen()
    print(printString)

  except KeyboardInterrupt:
    clear_screen()
    print("Failed to generate Mission\n")
    printString = ""

  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_mission, "Mission")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
