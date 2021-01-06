#!/usr/bin/env python3

from sys import path

path.append("..")
from support_functions import *

# Global Vars
#--------------------------------------------------#
PATRON     = "Patron"
OPPOSITION = "Opposition"
TARGET     = "target"
#--------------------------------------------------#

# Mission patron
#--------------------------------------------------#
MISSION_PATRON_TABLE_HEADER = [PATRON]

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
#--------------------------------------------------#

# Mission objective
#--------------------------------------------------#
MISSION_OBJECTIVE_TABLE_HEADER = ["Objective"]

MISSION_OBJECTIVE_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Assassinate a " + TARGET                                  ],
  ["Frame a " + TARGET                                        ],
  ["Destroy a " + TARGET                                      ],
  ["Steal from a " + TARGET                                   ],
  ["Aid in a burglary"                                        ],
  ["Stop a burglary"                                          ],
  ["None"], ["None"], ["None"], ["None"],
  ["Retrieve data or an object from a secure facility"        ],
  ["Discredit a " + TARGET                                    ],
  ["Find a lost cargo"                                        ],
  ["Find a lost person"                                       ],
  ["Deceive a " + TARGET                                      ],
  ["Sabotage a " + TARGET                                     ],
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
  ["Investigate a " + TARGET                                  ],
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
  ["Protect a " + TARGET                                      ],
  ["Save a " + TARGET                                         ],
  ["Aid a " + TARGET                                          ],
  ["It’s a trap – the patron intends to betray the characters"])
#--------------------------------------------------#

# Mission target
#--------------------------------------------------#
MISSION_TARGET_TABLE_HEADER = ["Target"]

MISSION_TARGET_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Common Trade Goods"                ],
  ["Common Trade Goods"                ],
  ["Random Trade Goods"                ],
  ["Random Trade Goods"                ],
  ["Illegal Trade Goods"               ],
  ["Illegal Trade Goods"               ],
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
#--------------------------------------------------#

# Mission patron generation
#--------------------------------------------------#
def handle_mission_patron_gen(funcArgs):
  missionPatron = roll_d_six_six()
  patronString  = "Mission Patron Info\n" + SEPARATOR_STRING
  patronString += get_table_entry(MISSION_PATRON_TABLE_HEADER, MISSION_PATRON_TABLE, missionPatron) + SEPARATOR_STRING
  return patronString, missionPatron
#--------------------------------------------------#

# Mission objective generation
#--------------------------------------------------#
def handle_mission_obj_gen(funcArgs):
  missionObj = roll_d_six_six()
  objString  = "Mission Objective Info\n" + SEPARATOR_STRING
  objString += get_table_entry(MISSION_OBJECTIVE_TABLE_HEADER, MISSION_OBJECTIVE_TABLE, missionObj) + SEPARATOR_STRING
  return objString, missionObj
#--------------------------------------------------#

# Mission target generation
#--------------------------------------------------#
def handle_mission_target_gen(funcArgs):
  missiontarget    = roll_d_six_six()
  targetString     = "Mission Target Info\n" + SEPARATOR_STRING
  tempTargetString = get_table_entry(MISSION_TARGET_TABLE_HEADER, MISSION_TARGET_TABLE, missiontarget)
  if PATRON in tempTargetString:
    targetString += get_table_entry(MISSION_PATRON_TABLE_HEADER, MISSION_PATRON_TABLE, roll_d_six_six())
  elif OPPOSITION in tempTargetString:
    targetString += get_table_entry(MISSION_OPPOSITION_TABLE_HEADER, MISSION_OPPOSITION_TABLE, roll_d_six_six())
  else:
    targetString += tempTargetString
  targetString += SEPARATOR_STRING
  return targetString, missiontarget
#--------------------------------------------------#

# Mission opposition generation
#--------------------------------------------------#
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
    if TARGET in objString:
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
