#!/usr/bin/env python3

from sys import path

path.append("..")
from support_functions import *

# Global Vars
#--------------------------------------------------#
STRENGTH            = "Strength"
DEXTERITY           = "Dexterity"
ENDURANCE           = "Endurance"
INTELLIGENCE        = "Intelligence"
EDUCATION           = "Education"
SOCIAL_STANDING     = "Social Standing"
GENERAL             = "General"
SPECS               = "Specs"
AGENT               = "Agent"
ARMY                = "Army"
CITIZEN             = "Citizen"
DRIFTER             = "Drifter"
ENTERTAINER         = "Entertainer"
MARINES             = "Marines"
MERCHANTS           = "Merchants"
NAVY                = "Navy"
NOBILITY            = "Nobility"
ROGUE               = "Rogue"
SCHOLAR             = "Scholar"
SCOUT               = "Scout"
LAW_ENFORCEMENT     = "Law Enforcement"
CORPORATE           = "Corporate"
SUPPORT             = "Support"
INFANTRY            = "Infantry"
CALVALRY            = "Calvalry"
WORKER              = "Worker"
COLONIST            = "Colonist"
BARBARIAN           = "Barbarian"
WANDERER            = "Wanderer"
SCAVENGER           = "Scavenger"
ARTIST              = "Artist"
JOURNALIST          = "Journalist"
PERFORMER           = "Performer"
STAR_MARINE         = "Star Marine"
GROUND_ASSUALT      = "Ground Assault"
MERCHANT_MARINE     = "Merchant Marine"
FREE_TRADER         = "Free Trader"
BROKER              = "Broker"
LINE_CREW           = "Line/Crew"
ENGINEERING_GUNNERY = "Engineering/Gunnery"
FLIGHT              = "Flight"
ADMINISTRATOR       = "Administrator"
DIPLOMAT            = "Diplomat"
DILETTANTE          = "Dilettante"
THIEF               = "Thief"
ENFORCER            = "Enforcer"
PIRATE              = "Pirate"
FIELD_RESEARCHER    = "Field Researcher"
SCIENTIST           = "Scientist"
PHYSICIAN           = "Physician"
COURIER             = "Courier"
SURVEY              = "Survey"
EXPLORATION         = "Exploration"
STREETWISE          = "Streetwise"
DRIVE               = "Drive"
INVESTIGATE         = "Investigate"
COMPUTERS           = "Computers"
RECON               = "Recon"
GUN_COMBAT          = "Gun Combat"
MELEE               = "Melee"
ATHLETICS           = "Athletics"
ADVOCATE            = "Advocate"
COMMS               = "Comms"
MEDIC               = "Medic"
STEALTH             = "Stealth"
REMOTE_OPERATIONS   = "Remote Operations"
PERSUADE            = "Persuade"
DECEPTION           = "Deception"
MECHANIC            = "Mechanic"
FLYER               = "Flyer"
EXPLOSIVES          = "Explosives"
HEAVY_WEAPONS       = "Heavy Weapons"
SENSORS             = "Sensors"
NAVIGATION          = "Navigation"
ENGINEER            = "Engineer"
SURVIVAL            = "Survival"
TACTICS             = "Tactics"
LEADERSHIP          = "Leadership"
ADMIN               = "Admin"
GUNNER              = "Gunner"
GAMBLER             = "Gambler"
TRADE               = "Trade"
SCIENCE             = "Science"
JACK_OF_ALL_TRADES  = "Jack of all Trades"
ANIMALS             = "Animals"
STEWARD             = "Steward"
ART                 = "Art"
LANGUAGE            = "Language"
CAROUSE             = "Carouse"
SEAFARER            = "Seafarer"
PILOT               = "Pilot"
ASTROGATION         = "Astrogation"
VACC_SUIT           = "Vacc Suit"
ZERO_G              = "Zero-G"
BATTLE_DRESS        = "Battle Dress"
SOCIAL_SCIENCE      = "Social Science"
LIFE_SCIENCE        = "Life Science"
SPACE_SCIENCE       = "Space Science"
PHYSICAL_SCIENCE    = "Physical Science"
#--------------------------------------------------#

# NPC Stats
#--------------------------------------------------#
def gen_npc_stats():
  npcStatDict = {STRENGTH       : roll_dice(2),
                 DEXTERITY      : roll_dice(2),
                 ENDURANCE      : roll_dice(2),
                 INTELLIGENCE   : roll_dice(2),
                 EDUCATION      : roll_dice(2),
                 SOCIAL_STANDING: roll_dice(2)}
  return npcStatDict

def handle_npc_stats_gen(funcArgs):
  statString   = "NPC Stats Info\n" + SEPARATOR_STRING
  npcStatDict  = gen_npc_stats()
  for stat in npcStatDict.keys():
    statString += stat + ": " + str(npcStatDict[stat]) + NEW_LINE
  statString += SEPARATOR_STRING
  return statString, npcStatDict
#--------------------------------------------------#

# NPC Career
#--------------------------------------------------#
AGENT_DICT = {LAW_ENFORCEMENT: {INVESTIGATE, RECON, STREETWISE, STEALTH, MELEE, ADVOCATE},
              INTELLIGENCE   : {INVESTIGATE, RECON, COMMS, STEALTH, PERSUADE, DECEPTION},
              CORPORATE      : {INVESTIGATE, COMPUTERS, STEALTH, GUN_COMBAT, DECEPTION, STREETWISE},
              GENERAL        : {STREETWISE, DRIVE, INVESTIGATE, COMPUTERS, RECON, GUN_COMBAT, ADVOCATE, COMMS, COMPUTERS, STEALTH, REMOTE_OPERATIONS}}

ARMY_DICT = {SUPPORT : {MECHANIC, DRIVE, FLYER, EXPLOSIVES, COMMS, MEDIC},
             INFANTRY: {GUN_COMBAT, MELEE, HEAVY_WEAPONS, STEALTH, ATHLETICS, RECON},
             CALVALRY: {MECHANIC, DRIVE, FLYER, RECON, GUNNER, SENSORS},
             GENERAL : {DRIVE, ATHLETICS, GUN_COMBAT, RECON, MELEE, HEAVY_WEAPONS, MEDIC, TACTICS, LEADERSHIP, ADVOCATE, ADMIN, GAMBLER}}

CITIZEN_DICT = {CORPORATE: {ADVOCATE, ADMIN, BROKER, COMPUTERS, DIPLOMAT, LEADERSHIP},
                WORKER   : {DRIVE, MECHANIC, TRADE, ENGINEER, SCIENCE},
                COLONIST : {ANIMALS, ATHLETICS, JACK_OF_ALL_TRADES, DRIVE, SURVIVAL, RECON},
                GENERAL  : {GAMBLER, DRIVE, JACK_OF_ALL_TRADES, FLYER, STREETWISE, MELEE, STEWARD, TRADE, ART, ADVOCATE, DIPLOMAT, LANGUAGE, COMPUTERS, MEDIC}}

DRIFTER_DICT = {BARBARIAN: {ANIMALS, CAROUSE, MELEE, STEALTH, SEAFARER, SURVIVAL, LEADERSHIP, NAVIGATION},
                WANDERER : {ATHLETICS, DECEPTION, RECON, STEALTH, STREETWISE, SURVIVAL, DRIVE, NAVIGATION, TRADE, CAROUSE},
                SCAVENGER: {PILOT, MECHANIC, ASTROGATION, VACC_SUIT, ZERO_G, GUN_COMBAT},
                GENERAL  : {JACK_OF_ALL_TRADES, ATHLETICS, MELEE, RECON, STREETWISE, STEALTH, SURVIVAL}}

ENTERTAINER_DICT = {ARTIST    : {ART, CAROUSE, COMPUTERS, GAMBLER, PERSUADE, TRADE},
                    JOURNALIST: {ART, COMMS, COMPUTERS, INVESTIGATE, RECON, STREETWISE},
                    PERFORMER : {ART, ATHLETICS, CAROUSE, DECEPTION, STEALTH, STREETWISE, LEADERSHIP},
                    GENERAL   : {CAROUSE, STEALTH, ART, DECEPTION, PERSUADE, STEWARD, ADVOCATE, SCIENCE, STREETWISE, DIPLOMAT}}

MARINES_DICT = {SUPPORT       : {COMMS, MECHANIC, DRIVE, MEDIC, HEAVY_WEAPONS, GUN_COMBAT},
                STAR_MARINE   : {BATTLE_DRESS, ZERO_G, GUNNER, MELEE, SENSORS, GUN_COMBAT},
                GROUND_ASSUALT: {BATTLE_DRESS, HEAVY_WEAPONS, RECON, MELEE, GUN_COMBAT},
                GENERAL       : {GAMBLER, MELEE, ATHLETICS, BATTLE_DRESS, TACTICS, HEAVY_WEAPONS, GUN_COMBAT, STEALTH, MEDIC, SURVIVAL, EXPLOSIVES, ENGINEER, PILOT, LEADERSHIP, ADMIN, ADVOCATE}}

MERCHANTS_DICT = {MERCHANT_MARINE: {PILOT, VACC_SUIT, ZERO_G, MECHANIC, ENGINEER, GUNNER},
                  FREE_TRADER    : {PILOT, VACC_SUIT, ZERO_G, MECHANIC, ENGINEER, SENSORS},
                  BROKER         : {ADMIN, ADVOCATE, BROKER, STREETWISE, DECEPTION, PERSUADE},
                  GENERAL        : {MELEE, STREETWISE, DRIVE, VACC_SUIT, BROKER, STEWARD, COMMS, PERSUADE, SOCIAL_SCIENCE, ASTROGATION, COMPUTERS, PILOT, ADMIN, ADVOCATE}}

NAVY_DICT = {LINE_CREW          : {COMMS, MECHANIC, GUN_COMBAT, SENSORS, MELEE, VACC_SUIT},
             ENGINEERING_GUNNERY: {ENGINEER, MECHANIC, SENSORS, GUNNER, COMPUTERS}, 
             FLIGHT             : {PILOT, FLYER, GUNNER, PILOT, ASTROGATION, ZERO_G},
             GENERAL            : {PILOT, VACC_SUIT, ZERO_G, GUNNER, MECHANIC, GUN_COMBAT, REMOTE_OPERATIONS, ASTROGATION, ENGINEER, COMPUTERS, NAVIGATION, ADMIN, LEADERSHIP, TACTICS, MELEE}}

NOBILITY_DICT = {ADMINISTRATOR: {ADMIN, ADVOCATE, BROKER, DIPLOMAT, LEADERSHIP, PERSUADE},
                 DIPLOMAT     : {ADVOCATE, CAROUSE, COMMS, STEWARD, DIPLOMAT, DECEPTION},
                 DILETTANTE   : {CAROUSE, DECEPTION, FLYER, STREETWISE, GAMBLER, JACK_OF_ALL_TRADES},
                 GENERAL      : {CAROUSE, DECEPTION, MELEE, ADMIN, ADVOCATE, COMMS, DIPLOMAT, INVESTIGATE, PERSUADE, LANGUAGE, LEADERSHIP, COMPUTERS}}

ROGUE_DICT = {THIEF    : {STEALTH, COMPUTERS, REMOTE_OPERATIONS, STREETWISE, DECEPTION, ATHLETICS},
              ENFORCER : {GUN_COMBAT, MELEE, STREETWISE, PERSUADE, ATHLETICS, DRIVE},
              PIRATE   : {PILOT, ASTROGATION, GUNNER, ENGINEER, VACC_SUIT, MELEE},
              GENERAL  : {CAROUSE, GAMBLER, MELEE, GUN_COMBAT, DECEPTION, RECON, ATHLETICS, GUN_COMBAT, STEALTH, STREETWISE, COMPUTERS, COMMS, MEDIC, INVESTIGATE, PERSUADE, ADVOCATE}}

SCHOLAR_DICT = {FIELD_RESEARCHER: {SENSORS, DIPLOMAT, LANGUAGE, SURVIVAL, INVESTIGATE, SCIENCE, SOCIAL_SCIENCE},
                SCIENTIST       : {ADMIN, ENGINEER, SCIENCE, SENSORS, COMPUTERS},
                PHYSICIAN       : {MEDIC, COMMS, INVESTIGATE, PERSUADE, SCIENCE, PHYSICAL_SCIENCE, LIFE_SCIENCE},
                GENERAL         : {COMPUTERS, COMMS, DIPLOMAT, MEDIC, INVESTIGATE, SCIENCE, ART, ADVOCATE, LANGUAGE}}

SCOUT_DICT = {COURIER    : {COMMS, SENSORS, PILOT, VACC_SUIT, ZERO_G, ASTROGATION},
              SURVEY     : {SENSORS, PERSUADE, PILOT, NAVIGATION, DIPLOMAT, STREETWISE},
              EXPLORATION: {SENSORS, PILOT, LIFE_SCIENCE, STEALTH, RECON},
              GENERAL    : {JACK_OF_ALL_TRADES, PILOT, SURVIVAL, MECHANIC, ASTROGATION, COMMS, GUN_COMBAT, MEDIC, NAVIGATION, ENGINEER, COMPUTERS, SPACE_SCIENCE}}

CAREER_DICT = {AGENT      : AGENT_DICT,
               ARMY       : ARMY_DICT,
               CITIZEN    : CITIZEN_DICT,
               DRIFTER    : DRIFTER_DICT,
               ENTERTAINER: ENTERTAINER_DICT,
               MARINES    : MARINES_DICT,
               MERCHANTS  : MERCHANTS_DICT,
               NAVY       : NAVY_DICT,
               NOBILITY   : NOBILITY_DICT,
               ROGUE      : ROGUE_DICT,
               SCHOLAR    : SCHOLAR_DICT,
               SCOUT      : SCOUT_DICT}

def gen_npc_career():
  careerList   = list(CAREER_DICT.keys())
  chosenCareer = careerList[roll_dice(1,0,len(careerList)-1)]

  specList   = list(CAREER_DICT[chosenCareer].keys())
  chosenSpec = specList[roll_dice(1,0,2)]

  careerRanks = roll_dice()
  return (chosenCareer, chosenSpec, careerRanks)

def handle_npc_career_gen(funcArgs):
  npcCareer     = gen_npc_career()
  careerString  = "NPC Career Info\n" + SEPARATOR_STRING
  careerString += "Career: " + npcCareer[0] + " (" + npcCareer[1] + ")" + NEW_LINE
  careerString += "Rank: " + str(npcCareer[2]) + NEW_LINE + SEPARATOR_STRING
  return careerString, npcCareer
#--------------------------------------------------#

# NPC Skills
#--------------------------------------------------#
def gen_npc_skills(careerInfo):
  chosenCareer = careerInfo[0]
  chosenSpec   = careerInfo[1]
  careerRank   = careerInfo[2]

  careerSkills = CAREER_DICT[chosenCareer][GENERAL]
  specSkills   = CAREER_DICT[chosenCareer][chosenSpec]

  availSkills    = list(careerSkills.union(specSkills))
  numAvailSkills = len(availSkills) - 1
  numNpcSkills   = careerRank + 5

  i = 0
  skillDict = dict({})
  while i < numNpcSkills:
    chosenSkill = availSkills[roll_dice(1,0,numAvailSkills)]
    skillDict[chosenSkill] = 0
    availSkills.remove(chosenSkill)
    numAvailSkills -= 1
    i += 1

  maxSkillRank = careerRank if careerRank < 4 else 3

  npcSkillList = list(skillDict.keys())
  for skill in npcSkillList:
    skillDict[skill] = roll_dice(1,0,maxSkillRank)

  return skillDict

def handle_npc_skills_gen(funcArgs):
  npcSkills    = gen_npc_skills(funcArgs[0])
  skillString  = "NPC Skills Info\n" + SEPARATOR_STRING
  listOfSkills = list(npcSkills.keys())
  for skill in listOfSkills:
    skillString += skill + ": " + str(npcSkills[skill]) + NEW_LINE
  skillString += SEPARATOR_STRING
  return skillString, npcSkills
#--------------------------------------------------#

# NPC Trait
#--------------------------------------------------#
NPC_TRAIT_TABLE_HEADER = ["Trait"]

NPC_TRAIT_TABLE = (["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"], ["None"],
  ["Loyal"                                       ],
  ["Distracted by other worries"                 ],
  ["In debt to criminals"                        ],
  ["Makes very bad jokes"                        ],
  ["Will betray characters"                      ],
  ["Aggressive"                                  ],
  ["None"], ["None"], ["None"], ["None"],
  ["Has secret allies"                           ],
  ["Secret anagathic user"                       ],
  ["Looking for something"                       ],
  ["Helpful"                                     ],
  ["Forgetful"                                   ],
  ["Wants to hire the chracters"                 ],
  ["None"], ["None"], ["None"], ["None"],
  ["Has useful contacts"                         ],
  ["Artistic"                                    ],
  ["Easily confused"                             ],
  ["Unusually ugly"                              ],
  ["Worried about current situation"             ],
  ["Shows pictures of his children"              ],
  ["None"], ["None"], ["None"], ["None"],
  ["Rumour-monger"                               ],
  ["Unusually provincial"                        ],
  ["Drunkard or drug addict"                     ],
  ["Government informant"                        ],
  ["Mistakes a player character for someone else"],
  ["Possesses unusually advanced technology"     ],
  ["None"], ["None"], ["None"], ["None"],
  ["Unusually handsome or beautiful"             ],
  ["Spying on the characters"                    ],
  ["Possesses TAS membership"                    ],
  ["Is secretly hostile towards the characters"  ],
  ["Wants to borrow money"                       ],
  ["Is convinced the characters are dangerous"   ],
  ["None"], ["None"], ["None"], ["None"],
  ["Involved in political intrigue"              ],
  ["Has a dangerous secret"                      ],
  ["Wants to get offplanet as soon as possible"  ],
  ["Attracted to a player character"             ],
  ["From offworld"                               ],
  ["Possesses telepathy or other unusual quality"])

def handle_npc_trait_gen(funcArgs):
  npcTrait     = roll_d_six_six()
  traitString  = "NPC Trait Info\n" + SEPARATOR_STRING
  traitString += get_table_entry(NPC_TRAIT_TABLE_HEADER, NPC_TRAIT_TABLE, npcTrait) + SEPARATOR_STRING
  return traitString, npcTrait
#--------------------------------------------------#

# Generate a new npc
#--------------------------------------------------#
def generate_npc(npcGenOption):
  try:
    # Stats
    noArgs = []
    npcGenOption, statString, npcStats = do_interactive_gen_loop(npcGenOption, handle_npc_stats_gen, noArgs)
    printString = statString + NEW_LINE

    # Career
    npcGenOption, careerString, npcCareer = do_interactive_gen_loop(npcGenOption, handle_npc_career_gen, noArgs)
    printString += careerString + NEW_LINE

    # Skills
    npcGenOption, skillString, npcSkills = do_interactive_gen_loop(npcGenOption, handle_npc_skills_gen, [npcCareer])
    printString += skillString + NEW_LINE

    # Trait
    npcGenOption, traitString, npcTrait = do_interactive_gen_loop(npcGenOption, handle_npc_trait_gen, noArgs)
    printString += traitString + NEW_LINE

    clear_screen()
    print(printString)

  except KeyboardInterrupt:
    clear_screen()
    print("Failed to generate NPC\n")
    printString = ""

  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_npc, "NPC")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
