#!/usr/bin/env python3

from sys import path

path.append("..")
from support_functions import *

# World Size
#--------------------------------------------------#
WORLD_SIZE_TABLE_HEADER = ("World Size (km)", "Surface Gravity (gs)")

WORLD_SIZE_TABLE = (("800"  , "Negligible"),
                    ("1600" , "0.05"      ),
                    ("3200" , "0.15"      ),
                    ("4800" , "0.25"      ),
                    ("6400" , "0.35"      ),
                    ("8000" , "0.45"      ),
                    ("9600" , "0.70"      ),
                    ("11200", "0.90"      ),
                    ("12800", "1.00"      ),
                    ("14400", "1.25"      ),
                    ("16000", "1.40"      ))

def gen_world_size():
  return roll_dice(2) - 2

def handle_world_size_gen(funcArgs):
  worldSize   = gen_world_size()
  sizeString  = "World Size Info\n" + SEPARATOR_STRING
  sizeString += get_table_entry(WORLD_SIZE_TABLE_HEADER, WORLD_SIZE_TABLE, worldSize) + SEPARATOR_STRING
  return sizeString, worldSize
#--------------------------------------------------#

# World Atmosphere
#--------------------------------------------------#
WORLD_ATMOSPHERE_TABLE_HEADER = ("Atmosphere", "Pressure", "Survival Gear Required", "Minimum TL")

WORLD_ATMOSPHERE_TABLE = (("None"              , "0.00"         , "Vacc Suit"         , "8" ),
                          ("Trace"             , "0.001 to 0.09", "Vacc Suit"         , "8" ),
                          ("Very Thin, Tainted", "0.10 to 0.42" , "Respirator, Filter", "5" ),
                          ("Very Thin"         , "0.10 to 0.42" , "Respirator"        , "5" ),
                          ("Thin, Tainted"     , "0.43 to 0.70" , "Filter"            , "3" ),
                          ("Thin"              , "0.43 to 0.70" , "None"              , "0" ),
                          ("Standard"          , "0.71 to 1.49" , "None"              , "0" ),
                          ("Standard, Tainted" , "0.71 to 1.49" , "Filter"            , "3" ),
                          ("Dense"             , "1.50 to 2.49" , "None"              , "0" ),
                          ("Dense, Tainted"    , "1.50 to 2.49" , "Filter"            , "3" ),
                          ("Exotic"            , "Varies"       , "Air Supply"        , "8" ),
                          ("Corrosive"         , "Varies"       , "Vacc Suit"         , "9" ),
                          ("Insidious"         , "Varies"       , "Vacc Suit"         , "10"),
                          ("Dense, High"       , "2.50 or more" , "None"              , "5" ),
                          ("Thin, Low"         , "0.50 or less" , "None"              , "5" ),
                          ("Unusual"           , "Varies"       , "Varies"            , "8" ))

def gen_world_atmosphere(worldSizeNum):
  worldAtmosphereNum = roll_dice(2) - 7 + worldSizeNum
  return worldAtmosphereNum if worldAtmosphereNum >= 0 else 0

def handle_world_atmos_gen(funcArgs):
  worldSize         = funcArgs[0]
  worldAtmosphere   = gen_world_atmosphere(worldSize)
  atmosphereString  = "World Atmosphere Info\n" + SEPARATOR_STRING
  atmosphereString += get_table_entry(WORLD_ATMOSPHERE_TABLE_HEADER, WORLD_ATMOSPHERE_TABLE, worldAtmosphere) + SEPARATOR_STRING
  return atmosphereString, worldAtmosphere
#--------------------------------------------------#

# World Temperature
#--------------------------------------------------#
WORLD_TEMPERATURE_TABLE_HEADER = ("Type", "Average Temperature (degrees Celsius)", "Description")

WORLD_TEMPERATURE_TABLE = (("Frozen"   , "-51 or less", "Frozen world. No liquid water, very dry atmosphere."                                    ),
                           ("Frozen"   , "-51 or less", "Frozen world. No liquid water, very dry atmosphere."                                    ),
                           ("Frozen"   , "-51 or less", "Frozen world. No liquid water, very dry atmosphere."                                    ),
                           ("Cold"     , "-51 to 0"   , "Icy world. Little liquid water, extensive ice caps, few clouds."                        ),
                           ("Cold"     , "-51 to 0"   , "Icy world. Little liquid water, extensive ice caps, few clouds."                        ),
                           ("Temperate", "0 to 30"    , "Temperate world. Earthlike. Liquid and vaporised water are common, moderate ice caps."  ),
                           ("Temperate", "0 to 30"    , "Temperate world. Earthlike. Liquid and vaporised water are common, moderate ice caps."  ),
                           ("Temperate", "0 to 30"    , "Temperate world. Earthlike. Liquid and vaporised water are common, moderate ice caps."  ),
                           ("Temperate", "0 to 30"    , "Temperate world. Earthlike. Liquid and vaporised water are common, moderate ice caps."  ),
                           ("Temperate", "0 to 30"    , "Temperate world. Earthlike. Liquid and vaporised water are common, moderate ice caps."  ),
                           ("Hot"      , "31 to 80"   , "Hot world. Small or no ice caps, little liquid water. Most water in the form of clouds."),
                           ("Hot"      , "31 to 80"   , "Hot world. Small or no ice caps, little liquid water. Most water in the form of clouds."),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ),
                           ("Roasting" , "81 or more" , "Boiling world. No ice caps, little liquid water."                                       ))

def gen_world_temperature(worldAtmosphereNum):
  if worldAtmosphereNum in (2,3):
    atmosphereMod = -2
  elif worldAtmosphereNum in (4,5,14):
    atmosphereMod = -1
  elif worldAtmosphereNum in (8,9):
    atmosphereMod = 1
  elif worldAtmosphereNum in (10,13,15):
    atmosphereMod = 2
  elif worldAtmosphereNum in (11,12):
    atmosphereMod = 6
  else:
    atmosphereMod = 0

  temperatureRoll = roll_dice(2) + atmosphereMod
  temperatureRoll = temperatureRoll if temperatureRoll >= 0 else 0
  return temperatureRoll

def handle_world_temp_gen(funcArgs):
  worldAtmosphere    = funcArgs[0]
  worldTemperature   = gen_world_temperature(worldAtmosphere)
  temperatureString  = "World Temperature Info\n" + SEPARATOR_STRING
  temperatureString += get_table_entry(WORLD_TEMPERATURE_TABLE_HEADER, WORLD_TEMPERATURE_TABLE, worldTemperature)
  if worldAtmosphere in (0,1):
    temperatureString += "Notes: Temperature swings from roasting during the day to frozen at night.\n" + SEPARATOR_STRING
  else:
    temperatureString += SEPARATOR_STRING
  return temperatureString, worldTemperature
#--------------------------------------------------#

# World Hydrographics
#--------------------------------------------------#
WORLD_HYDROGRAPHICS_TABLE_HEADER = ("Hydrographic Percentage", "Description")

WORLD_HYDROGRAPHICS_TABLE = (("0%-5%"   , "Desert world."                             ),
                             ("6%-15%"  , "Dry world."                                ),
                             ("16%-25%" , "A few small seas."                         ),
                             ("26%-35%" , "Small seas and oceans."                    ),
                             ("36%-45%" , "Wet world."                                ),
                             ("46%-55%" , "Large oceans."                             ),
                             ("56%-65%" , "Large oceans."                             ),
                             ("66%-75%" , "Earth-like world."                         ),
                             ("76%-85%" , "Water world."                              ),
                             ("86%-95%" , "Only a few small islands and archipelagos."),
                             ("96%-100%", "Almost entirely water."                    ))

def gen_world_hydrographics(worldSizeNum, worldAtmosphereNum, worldTemperatureNum):
  if worldSizeNum in (0,1):
    return 0

  atmosphereMod = -4 if worldAtmosphereNum in (0,1,10,11,12) else 0

  if worldTemperatureNum == 3:
    temperatureMod = -2
  elif worldTemperatureNum == 4:
    temperatureMod = -6
  else:
    temperatureMod = 0

  hydrographicsRoll = roll_dice(2) - 7 + worldSizeNum + atmosphereMod + temperatureMod
  hydrographicsRoll = hydrographicsRoll if hydrographicsRoll >= 0 else 0
  hydrographicsRoll = hydrographicsRoll if hydrographicsRoll <= 10 else 10
  return hydrographicsRoll

def handle_world_hydro_gen(funcArgs):
  worldSize            = funcArgs[0]
  worldAtmosphere      = funcArgs[1]
  worldTemperature     = funcArgs[2]
  worldHydrographics   = gen_world_hydrographics(worldSize, worldAtmosphere, worldTemperature)
  hydrographicsString  = "World Hydrographics Info\n" + SEPARATOR_STRING
  hydrographicsString += get_table_entry(WORLD_HYDROGRAPHICS_TABLE_HEADER, WORLD_HYDROGRAPHICS_TABLE, worldHydrographics) + SEPARATOR_STRING
  return hydrographicsString, worldHydrographics
#--------------------------------------------------#

# World Population
#--------------------------------------------------#
WORLD_POPULATION_TABLE_HEADER = ("Population", "Range", "Description")

WORLD_POPULATION_TABLE = (("None"                 , "0"             , "Uninhabited."                        ),
                          ("Few"                  , "1+"            , "A tiny farmstead or a single family."),
                          ("Hundreds"             , "100+"          , "A village."                          ),
                          ("Thousands"            , "1000+"         , "A village."                          ),
                          ("Tens of thousands"    , "10000+"        , "Small town."                         ),
                          ("Hundreds of thousands", "100000+"       , "Average city."                       ),
                          ("Millions"             , "1000000+"      , "Average city."                       ),
                          ("Tens of Millions"     , "10000000+"     , "Large city."                         ),
                          ("Hundreds of Millions" , "100000000+"    , "Large city."                         ),
                          ("Billions"             , "1000000000+"   , "Present day Earth."                  ),
                          ("Tens of Billions"     , "10000000000+"  , "Crowded world."                      ),
                          ("Hundreds of Billions" , "100000000000+" , "Incredibly crowded world."           ),
                          ("Trillions"            , "1000000000000+", "World-city."                         ))

def gen_world_population():
  return roll_dice(2) - 2

def handle_world_pop_gen(funcArgs):
  worldPopulation   = gen_world_population()
  populationString  = "World Population Info\n" + SEPARATOR_STRING
  populationString += get_table_entry(WORLD_POPULATION_TABLE_HEADER, WORLD_POPULATION_TABLE, worldPopulation) + SEPARATOR_STRING
  return populationString, worldPopulation
#--------------------------------------------------#

# World Government
#--------------------------------------------------#
WORLD_GOVERNMENT_TABLE_HEADER = ("Government", "Description")

WORLD_GOVERNMENT_TABLE = (("None"                       ,
                           "No government structure. In many cases, family bonds predominate."                                                                                                                                  ),
                          ("Company/Corporation"        ,
                           "Ruling functions are assumed by a company managerial elite, and most citizenry are company employees or dependants."                                                                                ),
                          ("Participating Democracy"    ,
                           "Ruling functions are reached by the advice and consent of the citizenry directly."                                                                                                                  ),
                          ("Self-perpetuating Oligarchy",
                           "Ruling functions are performed by a restricted minority, with little or no input from the mass of citizenry."                                                                                       ),
                          ("Representative Democracy"   ,
                           "Ruling functions are performed by elected representatives."                                                                                                                                         ),
                          ("Feudal Technocracy"         ,
                           "Ruling functions are performed by specific individuals for persons who agree to be ruled by them. Relationships are based on the performance of technical activities which are mutually beneficial."),
                          ("Captive Government"         ,
                           "Ruling functions are performed by an imposed leadership answerable to an outside group."                                                                                                            ),
                          ("Balkanisation"              ,
                           "No central authority exists; rival governments complete for control. Law level refers to the government nearest the starport."                                                                      ),
                          ("Civil Service Bureaucracy"  ,
                           "Ruling functions are performed by government agencies employing individuals selected for their expertise."                                                                                          ),
                          ("Impersonal Bureaucracy"     ,
                           "Ruling functions are performed by agencies which have become insulated from the governed citizens."                                                                                                 ),
                          ("Charismatic Dictator"       ,
                           "Ruling functions are performed by agencies directed by a single leader who enjoys the overwhelming confidence of the citizens."                                                                     ),
                          ("Non-charismatic Dictator"   ,
                           "A previous charismatic dictator has been replaced by a leader through normal channels."                                                                                                             ),
                          ("Charismatic Oligarchy"      ,
                           "Ruling functions are performed by a select group of members of an organisation or class which enjoys the overwhelming confidence of the citizenry."                                                 ),
                          ("Religious Dictatorship"     ,
                           "Ruling functions are performed by a religious organisation without regard to the specific individual needs of the citizenry."                                                                       ))

def gen_world_government(worldPopulationNum):
  governmentRoll = roll_dice(2) - 7 + worldPopulationNum
  governmentRoll = governmentRoll if governmentRoll >= 0 else 0
  governmentRoll = governmentRoll if governmentRoll <= 13 else 13
  return governmentRoll

def handle_world_gov_gen(funcArgs):
  populationNotZero = funcArgs[0]
  worldPopulation   = funcArgs[1]
  worldGovernment   = gen_world_government(worldPopulation) if populationNotZero else 0
  governmentString  = "World Government Info\n" + SEPARATOR_STRING
  governmentString += get_table_entry(WORLD_GOVERNMENT_TABLE_HEADER, WORLD_GOVERNMENT_TABLE, worldGovernment) + SEPARATOR_STRING
  return governmentString, worldGovernment
#--------------------------------------------------#

# World Factions
#--------------------------------------------------#
WORLD_FACTIONS_TABLE_HEADER = ["Relative Strength"]

WORLD_FACTIONS_TABLE = (["None"                                                            ],
                        ["Obscure group – few have heard of them, no popular support"      ],
                        ["Obscure group – few have heard of them, no popular support"      ],
                        ["Obscure group – few have heard of them, no popular support"      ],
                        ["Fringe group – few supporters"                                   ],
                        ["Fringe group – few supporters"                                   ],
                        ["Minor group – some supporters"                                   ],
                        ["Minor group – some supporters"                                   ],
                        ["Notable group – significant support, well known"                 ],
                        ["Notable group – significant support, well known"                 ],
                        ["Significant – nearly as powerful as the government"              ],
                        ["Significant – nearly as powerful as the government"              ],
                        ["Overwhelming popular support – more powerful than the government"])

def gen_world_factions(worldGovernmentNum):
  if worldGovernmentNum in (0,7):
    governmentMod = 1
  elif worldGovernmentNum >= 10:
    governmentMod = -1
  else:
    governmentMod = 0

  numFactions = roll_dice(1, 1, 3) + governmentMod
  factionList = []
  i = 0
  while i < numFactions:
    factionList.append(roll_dice(2))
    i += 1
  return factionList

def handle_world_factions_gen(funcArgs):
  populationNotZero = funcArgs[0]
  worldGovernment   = funcArgs[1]
  worldFactions     = gen_world_factions(worldGovernment) if populationNotZero else []
  factionString     = "World Factions Info\n" + SEPARATOR_STRING
  factionListLength = len(worldFactions)
  if factionListLength > 0:
    fIndex = 0
    while fIndex < factionListLength:
      factionString += NEW_LINE if fIndex > 0 else ""
      factionString += "Name: Faction" + str(fIndex + 1)  + NEW_LINE
      factionString += get_table_entry(WORLD_FACTIONS_TABLE_HEADER, WORLD_FACTIONS_TABLE, worldFactions[fIndex])
      fIndex += 1
  else:
    factionString += "None\n"
  factionString += SEPARATOR_STRING
  return factionString, worldFactions
#--------------------------------------------------#

# World Law Level
#--------------------------------------------------#
WORLD_LAW_TABLE_HEADER = ("Weapons", "Drugs", "Information", "Technology", "Travellers", "Psionics")

WORLD_LAW_TABLE = (("No restrictions.", "No restrictions.",
                    "No restrictions.", "No restrictions.",
                    "No restrictions.", "No restrictions."                                                                                                                ),
                   ("Poison gas, explosives, undetectable weapons, WMD.", "Highly addictive and dangerous narcotics.",
                    "Intellect programs.", "Dangerous technologies such as nanotechnology.",
                    "Visitors must contact planetary authorities by radio, landing is permitted anywhere.", "Dangerous talents must be registered."                       ),
                   ("Portable energy weapons (except ship-mounted weapons).", "Highly addictive narcotics.",
                    "Agent programs.", "Alien technology.",
                    "Visitors must report passenger manifest, landing is permitted anywhere.", "All psionic powers must be registered; use of dangerous powers forbidden."),
                   ("Heavy weapons.", "Combat drugs.",
                    "Intrusion programs.", "TL 15 items.",
                    "Landing only at starport or other authorised sites.", "Use of telepathy restricted to government approved telepaths."                                ),
                   ("Light assault weapons and submachine guns.", "Addictive narcotics.",
                    "Security programs.", "TL 13 items.",
                    "Landing only at starport.", "Use of teleportation and clairvoyance restricted."                                                                      ),
                   ("Personal concealable weapons.", "Anagathics.",
                    "Expert programs.", "TL 11 items.",
                    "Citizens must register offworld travel, visitors must register all business.", "Use of all psionic powers restricted to government psionicists."     ),
                   ("All firearms except shotguns and stunners; carrying weapons discouraged.", "Fast and Slow drugs.",
                    "Recent news from offworld.", "TL 9 items.",
                    "Visits discouraged; excessive contact with citizens forbidden.", "Possession of psionic drugs banned."                                               ),
                   ("Shotguns.", "All narcotics.",
                    "Library programs, unfiltered data about other worlds. Free speech curtailed.", "TL 7 items.",
                    "Citizens may not leave planet; visitors may not leave starport.", "Use of psionics forbidden."                                                       ),
                   ("All bladed weapons, stunners.", "Medicinal drugs.",
                    "Information technology, any non-critical data from offworld, personal media.", "TL 5 items.",
                    "Landing permitted only to imperial agents.", "Psionic-related technology banned."                                                                    ),
                   ("Any weapons.", "All drugs.",
                    "Any data from offworld. No free press.", "TL 3 items.",
                    "No offworlders permitted.", "All psionics."                                                                                                          ))

def gen_world_law_level(worldGovernmentNum):
  lawRoll = roll_dice(2) - 7 + worldGovernmentNum
  lawRoll = lawRoll if lawRoll >= 0 else 0
  lawRoll = lawRoll if lawRoll <= 9 else 9
  return lawRoll

def handle_world_law_gen(funcArgs):
  populationNotZero = funcArgs[0]
  worldGovernment   = funcArgs[1]
  worldLawLevel     = gen_world_law_level(worldGovernment) if populationNotZero else 0
  lawString         = "World Illegal Possessions Info\n" + SEPARATOR_STRING
  lawString        += "Law Level: " + str(worldLawLevel) + NEW_LINE
  lawString        += get_table_entry(WORLD_LAW_TABLE_HEADER, WORLD_LAW_TABLE, worldLawLevel) + SEPARATOR_STRING
  return lawString, worldLawLevel
#--------------------------------------------------#

# World Cultural Differences
#--------------------------------------------------#
WORLD_CULTURE_TABLE_HEADER = ["Culture"]

WORLD_CULTURE_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Sexist – one gender is considered subservient or inferior to the other."                                                                                                                                                                                        ],
  ["Religious – culture is heavily influenced by a religion or belief system, possibly one unique to this world."                                                                                                                                                   ],
  ["Artistic – art and culture are highly prized. Aesthetic design is important in all artefacts produced onworld."                                                                                                                                                 ],
  ["Ritualised – social interaction and trade is highly formalised. Politeness and adherence to traditional forms is considered very important."                                                                                                                    ],
  ["Conservative – the culture resists change and outside influences."                                                                                                                                                                                              ],
  ["Xenophobic – the culture distrusts outsiders and alien influences. Offworlders will face considerable prejudice."                                                                                                                                               ],
  ["None"], ["None"], ["None"], ["None"],
  ["Taboo – a particular topic is forbidden and cannot be discussed. Characters who unwittingly mention this topic will be ostracised."                                                                                                                             ],
  ["Deceptive – trickery and equivocation are considered acceptable. Honesty is a sign of weakness."                                                                                                                                                                ],
  ["Liberal – the culture welcomes change and offworld influence. Characters who bring new and strange ideas will be welcomed."                                                                                                                                     ],
  ["Honourable – one’s word is one’s bond in the culture. Lying is both rare and despised."                                                                                                                                                                         ],
  ["Influenced – the culture is heavily influenced by another, neighbouring world. If you have the details for the neighbouring world, choose a cultural quirk that this world has adopted. If not, roll for one."                                                  ],
  ["Fusion – the culture is a merger of two distinct cultures. Roll again twice to determine the quirks inherited from these cultures. If the quirks are incompatible then the culture is likely divided."                                                          ],
  ["None"], ["None"], ["None"], ["None"],
  ["Barbaric – physical strength and combat prowess are highly valued in the culture. Characters may be challenged to a fight, or dismissed if they seem incapable of defending themselves. Sports tend towards the bloody and violent."                            ],
  ["Remnant – the culture is a surviving remnant of a once-great and vibrant civilisation, clinging to its former glory. The world is filled with crumbling ruins, and every story revolves around the good old days."                                              ],
  ["Degenerate – the culture is falling apart and is on the brink of war or economic collapse. Violent protests are common and the social order is decaying."                                                                                                       ],
  ["Progressive – the culture is expanding and vibrant. Fortunes are being made in trade; science is forging bravely ahead."                                                                                                                                        ],
  ["Recovering – a recent trauma, such as a plague, war, disaster or despotic regime has left scars on the culture."                                                                                                                                                ],
  ["Nexus – members of many different cultures and species visit here."                                                                                                                                                                                             ],
  ["None"], ["None"], ["None"], ["None"],
  ["Tourist Attraction – some aspect of the culture or the planet draws visitors from all over charted space."                                                                                                                                                      ],
  ["Violent – physical conflict is common, taking the form of duels, brawls or other contests. Trial by combat is a part of their judicial system."                                                                                                                 ],
  ["Peaceful – physical conflict is almost unheard-of. The culture produces few soldiers and diplomacy reigns supreme. Forceful characters will be ostracised."                                                                                                     ],
  ["Obsessed – everyone is obsessed with or addicted to a substance, personality, act or item. This monomania pervades every aspect of the culture."                                                                                                                ],
  ["Fashion – fine clothing and decoration are considered vitally important in the culture. Underdressed characters have no standing here."                                                                                                                         ],
  ["At war – the culture is at war, either with another planet or polity, or is troubled by terrorists or rebels."                                                                                                                                                  ],
  ["None"], ["None"], ["None"], ["None"],
  ["Unusual Custom: Offworlders – space travellers hold a unique position in the culture’s mythology or beliefs, and travellers will be expected to live up to these myths."                                                                                        ],
  ["Unusual Custom: Starport – the planet’s starport is more than a commercial centre; it might be a religious temple, or be seen as highly controversial and surrounded by protestors."                                                                            ],
  ["Unusual Custom: Media – news agencies and telecommunications channels are especially strange here. Getting accurate information may be difficult."                                                                                                              ],
  ["Unusual Customs: Technology – the culture interacts with technology in an unusual way. Telecommunications might be banned, robots might have civil rights, cyborgs might be property."                                                                          ],
  ["Unusual Customs: Lifecycle – there might be a mandatory age of termination, or anagathics might be widely used. Family units might be different, with children being raised by the state or banned in favour of cloning."                                       ],
  ["Unusual Customs: Social Standings – the culture has a distinct caste system. Characters of a low social standing who do not behave appropriately will face punishment."                                                                                         ],
  ["None"], ["None"], ["None"], ["None"],
  ["Unusual Customs: Trade – the culture has an odd attitude towards some aspect of commerce, which may interfere with trade at the spaceport. For example, merchants might expect a gift as part of a deal, or some goods may only be handled by certain families."],
  ["Unusual Customs: Nobility – those of high social standing have a strange custom associated with them; perhaps nobles are blinded, or must live in gilded cages, or only serve for a single year before being exiled."                                           ],
  ["Unusual Customs: Sex – the culture has an unusual attitude towards intercourse and reproduction. Perhaps cloning is used instead, or sex is used to seal commercial deals."                                                                                     ],
  ["Unusual Customs: Eating – food and drink occupies an unusual place in the culture. Perhaps eating is a private affair, or banquets and formal dinners are seen as the highest form of politeness."                                                              ],
  ["Unusual Customs: Travel – travellers may be distrusted or feted, or perhaps the culture frowns on those who leave their homes."                                                                                                                                 ],
  ["Unusual Custom: Conspiracy – something strange is going on. The government is being subverted by another group or agency."                                                                                                                                      ])

def gen_world_cultural_differences():
  return roll_d_six_six()

def handle_world_culture_gen(funcArgs):
  populationNotZero = funcArgs[0]
  worldCulture      = gen_world_cultural_differences() if populationNotZero else 0
  cultureString     = "World Cultural Differences Info\n" + SEPARATOR_STRING
  cultureString    += get_table_entry(WORLD_CULTURE_TABLE_HEADER, WORLD_CULTURE_TABLE, worldCulture) + SEPARATOR_STRING
  return cultureString, worldCulture
#--------------------------------------------------#

# World Star Port
#--------------------------------------------------#
WORLD_STAR_PORT_TABLE_HEADER = ("Starport Class", "Quality", "Berthing Cost (Cr)", "Fuel", "Facilities", "Bases")

def gen_world_star_port_table(worldStarportNum):
  starPortTable = []
  i = 0
  while i < 13:
    if not i == worldStarportNum:
      starPortTable.append(("", "", "", "", "", ""))
    elif i in (0,1,2):
      starPortTable.append(("X", "No Starport", "0", "None", "None", "None"))
    elif i in (3,4):
      starPortTable.append(("E", "Frontier", "0", "None", "None", "Pirate" if roll_dice(2) >= 12 else "None"))
    elif i in (5,6):
      pirateString = "Pirate" if roll_dice(2) >= 12 else ""
      scoutString  = "Scout" if roll_dice(2) >= 7 else ""
      baseString   = convert_slist_to_string((pirateString, scoutString))
      starPortTable.append(("D", "Poor", str(roll_dice() * 10), "Unrefined", "Limited Repair", baseString))
    elif i in (7,8):
      pirateString    = "Pirate" if roll_dice(2) >= 10 else ""
      scoutString     = "Scout" if roll_dice(2) >= 8 else ""
      tasString       = "TAS" if roll_dice(2) >= 10 else ""
      researchString  = "Research" if roll_dice(2) >= 10 else ""
      consulateString = "Imperial Consulate" if roll_dice(2) >= 10 else ""
      baseString      = convert_slist_to_string((pirateString, scoutString, tasString, researchString, consulateString))
      starPortTable.append(("C", "Routine", str(roll_dice() * 100), "Unrefined", "Shipyard (small craft) Repair", baseString))
    elif i in (9,10):
      pirateString    = "Pirate" if roll_dice(2) >= 12 else ""
      scoutString     = "Scout" if roll_dice(2) >= 8 else ""
      tasString       = "TAS" if roll_dice(2) >= 6 else ""
      researchString  = "Research" if roll_dice(2) >= 10 else ""
      consulateString = "Imperial Consulate" if roll_dice(2) >= 8 else ""
      navalString     = "Naval" if roll_dice(2) >= 8 else ""
      baseString      = convert_slist_to_string((pirateString, scoutString, tasString, researchString, consulateString, navalString))
      starPortTable.append(("B", "Good", str(roll_dice() * 500), "Refined", "Shipyard (spacecraft) Repair", baseString))
    else:
      scoutString     = "Scout" if roll_dice(2) >= 10 else ""
      tasString       = "TAS" if roll_dice(2) >= 4 else ""
      researchString  = "Research" if roll_dice(2) >= 8 else ""
      consulateString = "Imperial Consulate" if roll_dice(2) >= 6 else ""
      navalString     = "Naval" if roll_dice(2) >= 8 else ""
      baseString      = convert_slist_to_string((scoutString, tasString, researchString, consulateString, navalString))
      starPortTable.append(("A", "Excellent", str(roll_dice() * 1000), "Refined", "Shipyard (all) Repair", baseString))
    i += 1
  return starPortTable

def gen_world_star_port():
  return roll_dice(2)

def handle_world_starport_gen(funcArgs):
  populationNotZero  = funcArgs[0]
  worldStarport      = gen_world_star_port() if populationNotZero else 0
  worldStarportTable = gen_world_star_port_table(worldStarport)
  starportString     = "World Starport Info\n" + SEPARATOR_STRING
  starportString    += get_table_entry(WORLD_STAR_PORT_TABLE_HEADER, worldStarportTable, worldStarport) + SEPARATOR_STRING
  return starportString, worldStarport
#--------------------------------------------------#

# World Technology Level
#--------------------------------------------------#
def gen_world_tech_level(starPortNum, sizeNum, atmosNum, hydroNum, popNum, govNum):
  if starPortNum in (11,12):
    starPortMod = 6
  elif starPortNum in (9,10):
    starPortMod = 4
  elif starPortNum in (7,8):
    starPortMod = 2
  elif starPortNum in (3,4,5,6):
    starPortMod = 0
  else:
    starPortMod = -4

  if sizeNum in (0,1):
    sizeMod = 2
  elif sizeNum in (2,3,4):
    sizeMod = 1
  else:
    sizeMod = 0

  if atmosNum in (0,1,2,3,10,11,12,13,14,15):
    atmosphereMod = 1
  else:
    atmosphereMod = 0

  if hydroNum in (0,9):
    hydrographicsMod = 1
  elif hydroNum == 10:
    hydrographicsMod = 2
  else:
    hydrographicsMod = 0

  if popNum in (1,2,3,4,5,9):
    populationMod = 1
  elif popNum == 10:
    populationMod = 2
  elif popNum == 11:
    populationMod = 3
  elif popNum == 12:
    populationMod = 4
  else:
    populationMod = 0

  if govNum in (0,5):
    governmentMod = 1
  elif govNum == 7:
    governmentMod = 2
  elif govNum in (13,14):
    governmentMod = -2
  else:
    governmentMod = 0

  techRoll = roll_dice() + starPortMod + sizeMod + atmosphereMod + hydrographicsMod + populationMod + governmentMod
  techRoll = techRoll if techRoll >= 0 else 0
  techRoll = techRoll if techRoll <= 15 else 15
  return techRoll

def handle_world_tech_gen(funcArgs):
  populationNotZero  = funcArgs[0]
  worldStarport      = funcArgs[1]
  worldSize          = funcArgs[2]
  worldAtmosphere    = funcArgs[3]
  worldHydrographics = funcArgs[4]
  worldPopulation    = funcArgs[5]
  worldGovernment    = funcArgs[6]
  worldTechLevel     = gen_world_tech_level(worldStarport, worldSize, worldAtmosphere, worldHydrographics, worldPopulation, worldGovernment) if populationNotZero else 0
  techString         = "World Technology Info\n" + SEPARATOR_STRING
  techString        += "Tech Level: " + str(worldTechLevel) + NEW_LINE + SEPARATOR_STRING
  return techString, worldTechLevel
#--------------------------------------------------#

# World Trade Codes
#--------------------------------------------------#
WORLD_TRADE_TABLE_HEADER = ("Classification", "Code", "Description")

WORLD_TRADE_TABLE = (("Agricultural"    , "Ag", "Agricultural worlds are dedicated to farming and food production. Often, they are divided into vast semi-feudal estates."        ),
                     ("Asteroid"        , "As", "Asteroids are usually mining colonies, but can also be orbital factories or colonies."                                           ),
                     ("Barren"          , "Ba", "Barren worlds are uncolonised and empty."                                                                                        ),
                     ("Desert"          , "De", "Desert worlds are dry and barely habitable."                                                                                     ),
                     ("Fluid Oceans"    , "Fl", "Fluid Oceans are worlds where the surface liquid is something other than water, and so are incompatible with Earth-derived life."),
                     ("Garden"          , "Ga", "Garden worlds are Earth-like."                                                                                                   ),
                     ("High Population" , "Hi", "High Population worlds have a population in the billions."                                                                       ),
                     ("High Technology" , "Ht", "High Technology worlds are among the most technologically advanced in the Imperium."                                             ),
                     ("Ice-Capped"      , "Ic", "Ice-Capped worlds have most of their surface liquid frozen in polar ice caps, and are cold and dry."                             ),
                     ("Industrial"      , "In", "Industrial worlds are dominated by factories and cities."                                                                        ),
                     ("Low Population"  , "Lo", "Low Population worlds have a population of only a few thousand or less."                                                         ),
                     ("Low Technology"  , "Lt", "Low Technology worlds are preindustrial and cannot produce advanced goods."                                                      ),
                     ("Non-Agricultural", "Na", "Non-Agricultural worlds are too dry or barren to support their populations using conventional food production."                  ),
                     ("Non-Industrial"  , "Ni", "Non-Industrial worlds are too low-population to maintain an industrial base."                                                    ),
                     ("Poor"            , "Po", "Poor worlds lack resources, viable land or sufficient population to be anything other than marginal colonies."                   ),
                     ("Rich"            , "Ri", "Rich worlds are blessed with a stable government and viable biosphere, making them economic powerhouses."                        ),
                     ("Vaccum"          , "Va", "Vacuum worlds have no atmosphere."                                                                                               ),
                     ("Water World"     , "Wa", "Water Worlds are nearly entirely water-ocean."                                                                                   ))

def gen_world_trade_codes(sizeNum, atmosNum, hydroNum, popNum, govNum, lawNum, techNum):
  tradeCodes = []
  if atmosNum in (4,5,6,7,8,9) and hydroNum in (4,5,6,7,8) and popNum in (5,6,7):
    tradeCodes.append(0)
  if sizeNum == 0 and atmosNum == 0 and hydroNum == 0:
    tradeCodes.append(1)
  if popNum == 0 and govNum == 0 and lawNum == 0:
    tradeCodes.append(2)
  if atmosNum >= 2 and hydroNum == 0:
    tradeCodes.append(3)
  if atmosNum >= 10 and hydroNum >= 1:
    tradeCodes.append(4)
  if sizeNum >= 5 and atmosNum in (4,5,6,7,8,9) and hydroNum in (4,5,6,7,8):
    tradeCodes.append(5)
  if popNum >= 9:
    tradeCodes.append(6)
  if techNum >= 12:
    tradeCodes.append(7)
  if atmosNum in (0,1) and hydroNum >= 1:
    tradeCodes.append(8)
  if atmosNum in (0,1,2,4,7,9) and popNum >= 9:
    tradeCodes.append(9)
  if popNum in (1,2,3):
    tradeCodes.append(10)
  if techNum <= 5:
    tradeCodes.append(11)
  if atmosNum in (0,1,2,3) and hydroNum in (0,1,2,3) and popNum >= 6:
    tradeCodes.append(12)
  if popNum in (4,5,6):
    tradeCodes.append(13)
  if atmosNum in (2,3,4,5) and hydroNum in (0,1,2,3):
    tradeCodes.append(14)
  if atmosNum in (6,8) and popNum in (6,7,8):
    tradeCodes.append(15)
  if atmosNum == 0:
    tradeCodes.append(16)
  if hydroNum == 10:
    tradeCodes.append(17)
  return tradeCodes

def handle_world_trade_gen(funcArgs):
  worldSize           = funcArgs[0]
  worldAtmosphere     = funcArgs[1]
  worldHydrographics  = funcArgs[2]
  worldPopulation     = funcArgs[3]
  worldGovernment     = funcArgs[4]
  worldLawLevel       = funcArgs[5]
  worldTechLevel      = funcArgs[6]
  worldTradeCodes     = gen_world_trade_codes(worldSize, worldAtmosphere, worldHydrographics, worldPopulation, worldGovernment, worldLawLevel, worldTechLevel)
  tradeString         = "World Trade Code Info\n" + SEPARATOR_STRING
  tradeCodeListLength = len(worldTradeCodes)
  if tradeCodeListLength > 0:
    tIndex = 0
    while tIndex < tradeCodeListLength:
      tradeString += get_table_entry(WORLD_TRADE_TABLE_HEADER, WORLD_TRADE_TABLE, worldTradeCodes[tIndex]) + (NEW_LINE if not tIndex == tradeCodeListLength - 1 else "")
      tIndex += 1
  else:
    tradeString += "None\n"
  tradeString += SEPARATOR_STRING
  return tradeString
#--------------------------------------------------#

# Generate a new world
#--------------------------------------------------#
def generate_world(worldGenOption):
  try:
    # Size
    noArgs = []
    worldGenOption, sizeString, worldSize = do_interactive_gen_loop(worldGenOption, handle_world_size_gen, noArgs)
    printString = sizeString + NEW_LINE

    # Atmosphere
    worldGenOption, atmosphereString, worldAtmosphere = do_interactive_gen_loop(worldGenOption, handle_world_atmos_gen, [worldSize])
    printString += atmosphereString + NEW_LINE

    # Temperature
    worldGenOption, temperatureString, worldTemperature = do_interactive_gen_loop(worldGenOption, handle_world_temp_gen, [worldAtmosphere])
    printString += temperatureString + NEW_LINE
    
    # Hydrographics
    worldGenOption, hydrographicsString, worldHydrographics = do_interactive_gen_loop(worldGenOption, handle_world_hydro_gen, [worldSize, worldAtmosphere, worldTemperature])
    printString += hydrographicsString + NEW_LINE

    # Population
    worldGenOption, populationString, worldPopulation = do_interactive_gen_loop(worldGenOption, handle_world_pop_gen, noArgs)
    populationNotZero = worldPopulation > 0
    printString += populationString + NEW_LINE
    
    # Government
    govArgs = [populationNotZero, worldPopulation]
    if populationNotZero:
      worldGenOption, governmentString, worldGovernment = do_interactive_gen_loop(worldGenOption, handle_world_gov_gen, govArgs)
    else:
      governmentString, worldGovernment = handle_world_gov_gen(govArgs)
    printString += governmentString + NEW_LINE

    # Factions
    facLawArgs = [populationNotZero, worldGovernment]
    if populationNotZero:
      worldGenOption, factionString, worldFactions = do_interactive_gen_loop(worldGenOption, handle_world_factions_gen, facLawArgs)
    else:
      factionString, worldFactions = handle_world_factions_gen(facLawArgs)
    printString += factionString + NEW_LINE
    
    # Law
    if populationNotZero:
      worldGenOption, lawString, worldLawLevel = do_interactive_gen_loop(worldGenOption, handle_world_law_gen, facLawArgs)
    else:
      lawString, worldLawLevel = handle_world_law_gen(facLawArgs)
    printString += lawString + NEW_LINE

    # Culture
    culStarArgs = [populationNotZero]
    if populationNotZero:
      worldGenOption, cultureString, worldCulture = do_interactive_gen_loop(worldGenOption, handle_world_culture_gen, culStarArgs)
    else:
      cultureString, worldCulture = handle_world_culture_gen(culStarArgs)
    printString += cultureString + NEW_LINE

    # Starport
    if populationNotZero:
      worldGenOption, starportString, worldStarport = do_interactive_gen_loop(worldGenOption, handle_world_starport_gen, culStarArgs)
    else:
      starportString, worldStarport = handle_world_starport_gen(culStarArgs)
    printString += starportString + NEW_LINE

    # Tech
    techArgs = [populationNotZero, worldStarport, worldSize, worldAtmosphere, worldHydrographics, worldPopulation, worldGovernment]
    if populationNotZero:
      worldGenOption, techString, worldTechLevel = do_interactive_gen_loop(worldGenOption, handle_world_tech_gen, techArgs)
    else:
      techString, worldTechLevel = handle_world_tech_gen(techArgs)
    printString += techString + NEW_LINE

    # Trade Codes
    tradeArgs = [worldSize, worldAtmosphere, worldHydrographics, worldPopulation, worldGovernment, worldLawLevel, worldTechLevel]
    printString += handle_world_trade_gen(tradeArgs) + NEW_LINE

    clear_screen()
    print(printString)

  except KeyboardInterrupt:
    clear_screen()
    print("Failed to generate World\n")
    printString = ""

  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_world, "World")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
