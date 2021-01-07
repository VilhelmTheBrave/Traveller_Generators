#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

# Global Enums
#--------------------------------------------------#
class TERRAIN_OPTIONS(Enum):
  Random          = 0
  Clear           = 1
  Plain_Prairie   = 2
  Desert          = 3
  Hills_Foothills = 4
  Mountain        = 5
  Forest          = 6
  Woods           = 7
  Jungle          = 8
  Rainforest      = 9
  Rough_Broken    = 10
  Swamp_Marsh     = 11
  Beach_Shore     = 12
  Riverbank       = 13
  Ocean_Shallows  = 14
  Open_Ocean      = 15
  Deep_Ocean      = 16

class CREATURE_TYPES(Enum):
  Scavenger = (2,4,10)
  Omnivore  = (3,5)
  Herbivore = (6,7,8)
  Carnivore = (9,11,12)

class CREATURE_BEHAVIORS(Enum):
  Carrion_Eater = "Scavengers which wait for all other threats to disperse before beginning."
  Chaser        = "Animals which kill their prey by attacking and exhausting it after a chase."
  Eater         = "Eaters will eat anything they encounter, including characters."
  Filter        = "Herbivores which pass their environment through their bodies are termed filters. Unlike grazers, which move to food, filters move a flow of matter through themselves and filter out the food."
  Gatherer      = "Gatherers are omnivores that collect and store food."
  Grazer        = "Grazers move from food source to food source, often in large packs. Their primary form of defence tends to be fleeing danger."
  Hunter        = "Opportunistic predators that stalk easy prey."
  Hijacker      = "Scavengers which steal the kills of others through brute force or weight of numbers are hijackers."
  Intimidator   = "Scavengers which establish their claim to food by frightening or intimidating other creatures."
  Killer        = "Carnivores that possess a raw killing instinct, attacking in a frenzied manner"
  Intermittent  = "Herbivores that do not devote their entire time to searching for food."
  Pouncer       = "Pouncers kill by stalking and ambushing their prey."
  Reducer       = "Reducers are scavengers that act constantly on all available food, devouring even the remains left by other scavengers."
  Siren         = "Sirens create a lure to attract prey. Usually, this lure will be specific to the species the siren preys on, but some rare lures are universal."
  Trapper       = "An animal which allows its prey to enter a trap. Generally, any creature surprised by a trapper is caught in its trap."
#--------------------------------------------------#

# Creature Movement
#--------------------------------------------------#
CREATURE_MOVEMENT_TABLE_HEADER = ["Movement"]

CLEAR_JUNGLE_MOVEMENT_TABLE  = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Walk +2"], ["Fly -6" ])
PLAIN_MOVEMENT_TABLE         = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk +2"], ["Walk +4"], ["Fly -6" ])
DESERT_FOREST_MOVEMENT_TABLE = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
HILLS_ROUGH_MOVEMENT_TABLE   = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk +2"], ["Fly -4" ], ["Fly -6" ])
WOODS_MOVEMENT_TABLE         = (["Walk"   ], ["Walk"         ], ["Walk"   ], ["Walk"   ], ["Walk"   ], ["Fly -6" ])
SWAMP_MOVEMENT_TABLE         = (["Swim -6"], ["Amphibious +2"], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
BEACH_MOVEMENT_TABLE         = (["Swim +1"], ["Amphibious +2"], ["Walk"   ], ["Walk"   ], ["Fly -4" ], ["Fly -6" ])
RIVERBANK_MOVEMENT_TABLE     = (["Swim -4"], ["Amphibious"   ], ["Walk"   ], ["Walk"   ], ["Walk"   ], ["Fly -6" ])
SHALLOWS_MOVEMENT_TABLE      = (["Swim +4"], ["Swim +2"      ], ["Swim"   ], ["Swim"   ], ["Fly -4" ], ["Fly -6" ])
OPEN_MOVEMENT_TABLE          = (["Swim +6"], ["Swim +4"      ], ["Swim +2"], ["Swim"   ], ["Fly -4" ], ["Fly -6" ])
DEEP_MOVEMENT_TABLE          = (["Swim +8"], ["Swim +6"      ], ["Swim +4"], ["Swim +2"], ["Swim"   ], ["Swim -2"])

def gen_creature_movement():
  return roll_dice() - 1

def handle_creature_movement_gen(funcArgs):
  chosenTerrain = funcArgs[0]
  creatureMovement = gen_creature_movement()
  if chosenTerrain in (TERRAIN_OPTIONS.Clear, TERRAIN_OPTIONS.Jungle):
    movementTable = CLEAR_JUNGLE_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Plain_Prairie:
    movementTable = PLAIN_MOVEMENT_TABLE
  elif chosenTerrain in (TERRAIN_OPTIONS.Desert, TERRAIN_OPTIONS.Forest):
    movementTable = DESERT_FOREST_MOVEMENT_TABLE
  elif chosenTerrain in (TERRAIN_OPTIONS.Hills_Foothills, TERRAIN_OPTIONS.Rough_Broken):
    movementTable = HILLS_ROUGH_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Woods:
    movementTable = WOODS_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Swamp_Marsh:
    movementTable = SWAMP_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Beach_Shore:
    movementTable = BEACH_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Riverbank:
    movementTable = RIVERBANK_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Ocean_Shallows:
    movementTable = SHALLOWS_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Open_Ocean:
    movementTable = OPEN_MOVEMENT_TABLE
  else:
    movementTable = DEEP_MOVEMENT_TABLE
  
  movementString  = "Creature Movement Info\n" + SEPARATOR_STRING
  movementString += "Terrain: " + chosenTerrain.name + NEW_LINE
  movementString += get_table_entry(CREATURE_MOVEMENT_TABLE_HEADER, movementTable, creatureMovement) + SEPARATOR_STRING
  return movementString, creatureMovement
#--------------------------------------------------#

# Creature Type
#--------------------------------------------------#
def gen_creature_type():
  creatureTypeRoll = roll_dice(2)
  for creatureTypeEntry in CREATURE_TYPES:
    if creatureTypeRoll in creatureTypeEntry.value:
      creatureType = creatureTypeEntry
      break
  return creatureType

def handle_creature_type_gen(funcArgs):
  creatureType = gen_creature_type()
  typeString   = "Creature Type Info\n" + SEPARATOR_STRING
  typeString  += "Type: " + creatureType.name + NEW_LINE + SEPARATOR_STRING
  return typeString, creatureType
#--------------------------------------------------#

# Creature Behavior
#--------------------------------------------------#
def gen_creature_behavior(chosenTerrain, creatureType):
  if chosenTerrain in (TERRAIN_OPTIONS.Clear, TERRAIN_OPTIONS.Desert, TERRAIN_OPTIONS.Rough_Broken):
    terrainMod = 3
  elif chosenTerrain in (TERRAIN_OPTIONS.Plain_Prairie, TERRAIN_OPTIONS.Ocean_Shallows, TERRAIN_OPTIONS.Open_Ocean, TERRAIN_OPTIONS.Deep_Ocean):
    terrainMod = 4
  elif chosenTerrain in (TERRAIN_OPTIONS.Forest, TERRAIN_OPTIONS.Jungle):
    terrainMod = -4
  elif chosenTerrain in (TERRAIN_OPTIONS.Woods, TERRAIN_OPTIONS.Rainforest, TERRAIN_OPTIONS.Swamp_Marsh):
    terrainMod = -2
  elif chosenTerrain == TERRAIN_OPTIONS.Rough_Broken:
    terrainMod = -3
  elif chosenTerrain == TERRAIN_OPTIONS.Riverbank:
    terrainMod = 1
  else:
    terrainMod = 0

  creatureBehaviorRoll = roll_dice(2) + terrainMod
  if creatureType == CREATURE_TYPES.Herbivore:
    if creatureBehaviorRoll <= 2:
      creatureBehavior = CREATURE_BEHAVIORS.Filter
    elif creatureBehaviorRoll in (3,4,5,6):
      creatureBehavior = CREATURE_BEHAVIORS.Intermittent
    else:
      creatureBehavior = CREATURE_BEHAVIORS.Grazer
  elif creatureType == CREATURE_TYPES.Omnivore:
    if creatureBehaviorRoll <= 1 or creatureBehaviorRoll in (3,5,9) or creatureBehaviorRoll >= 12:
      creatureBehavior = CREATURE_BEHAVIORS.Gatherer
    elif creatureBehaviorRoll in (2,4,10):
      creatureBehavior = CREATURE_BEHAVIORS.Eater
    else:
      creatureBehavior = CREATURE_BEHAVIORS.Hunter
  elif creatureType == CREATURE_TYPES.Carnivore:
    if creatureBehaviorRoll <= 1 or creatureBehaviorRoll in (3,6):
      creatureBehavior = CREATURE_BEHAVIORS.Pouncer
    elif creatureBehaviorRoll in (2,12):
      creatureBehavior = CREATURE_BEHAVIORS.Siren
    elif creatureBehaviorRoll in (4,10):
      creatureBehavior = CREATURE_BEHAVIORS.Killer
    elif creatureBehaviorRoll == 5:
      creatureBehavior = CREATURE_BEHAVIORS.Trapper
    else:
      creatureBehavior = CREATURE_BEHAVIORS.Chaser
  else:
    if creatureBehaviorRoll <= 1 or creatureBehaviorRoll in (4,7):
      creatureBehavior = CREATURE_BEHAVIORS.Carrion_Eater
    elif creatureBehaviorRoll in (2,6,8):
      creatureBehavior = CREATURE_BEHAVIORS.Reducer
    elif creatureBehaviorRoll in (3,9,12):
      creatureBehavior = CREATURE_BEHAVIORS.Hijacker
    else:
      creatureBehavior = CREATURE_BEHAVIORS.Intimidator

  return creatureBehavior

def handle_creature_behavior_gen(funcArgs):
  creatureBehavior = gen_creature_behavior(funcArgs[0], funcArgs[1])
  behaviorString   = "Creature Behavior Info\n" + SEPARATOR_STRING
  behaviorString  += "Behavior: " + creatureBehavior.name + NEW_LINE
  behaviorString  += "Description: " + creatureBehavior.value + NEW_LINE + SEPARATOR_STRING
  return behaviorString, creatureBehavior
#--------------------------------------------------#

# Creature characteristics
#--------------------------------------------------#
CREATURE_CHARACTERISTICS_TABLE_HEADER = ("Weight (kg)", "Strength", "Dexterity", "Endurance", "Intelligence", "Instinct")

def get_creature_instinct(creatureBehavior):
  if creatureBehavior in (CREATURE_BEHAVIORS.Carrion_Eater, CREATURE_BEHAVIORS.Chaser, CREATURE_BEHAVIORS.Grazer, CREATURE_BEHAVIORS.Hunter):
    instinctMod = 2
  elif creatureBehavior in (CREATURE_BEHAVIORS.Killer, CREATURE_BEHAVIORS.Pouncer):
    instinctMod = 4
  else:
    instinctMod = 0
  
  return roll_dice(2) + instinctMod

def gen_creature_characteristics_info(creatureCharNum, creatureBehaviorNum, strengthMod, dexterityMod, enduranceMod):
  if creatureCharNum == 1:
    dexerity  = str(roll_dice() + dexterityMod)
    endurance = str(1 + enduranceMod)
    strength  = 1 + strengthMod
    weight    = "1"
  elif creatureCharNum == 2:
    dexerity  = str(roll_dice() + dexterityMod)
    endurance = str(2 + enduranceMod)
    strength  = 2 + strengthMod
    weight    = "3"
  elif creatureCharNum == 3:
    dexerity  = str(roll_dice(2) + dexterityMod)
    endurance = str(roll_dice() + enduranceMod)
    strength  = roll_dice() + strengthMod
    weight    = "6"
  elif creatureCharNum == 4:
    dexerity  = str(roll_dice(2) + dexterityMod)
    endurance = str(roll_dice() + enduranceMod)
    strength  = roll_dice() + strengthMod
    weight    = "12"
  elif creatureCharNum == 5:
    dexerity  = str(roll_dice(3) + dexterityMod)
    endurance = str(roll_dice(2) + enduranceMod)
    strength  = roll_dice(2) + strengthMod
    weight    = "25"
  elif creatureCharNum == 6:
    dexerity  = str(roll_dice(4) + dexterityMod)
    endurance = str(roll_dice(2) + enduranceMod)
    strength  = roll_dice(2) + strengthMod
    weight    = "50"
  elif creatureCharNum == 7:
    dexerity  = str(roll_dice(3) + dexterityMod)
    endurance = str(roll_dice(3) + enduranceMod)
    strength  = roll_dice(3) + strengthMod
    weight    = "100"
  elif creatureCharNum == 8:
    dexerity  = str(roll_dice(3) + dexterityMod)
    endurance = str(roll_dice(3) + enduranceMod)
    strength  = roll_dice(3) + strengthMod
    weight    = "200"
  elif creatureCharNum == 9:
    dexerity  = str(roll_dice(2) + dexterityMod)
    endurance = str(roll_dice(4) + enduranceMod)
    strength  = roll_dice(4) + strengthMod
    weight    = "400"
  elif creatureCharNum == 10:
    dexerity  = str(roll_dice(2) + dexterityMod)
    endurance = str(roll_dice(4) + enduranceMod)
    strength  = roll_dice(4) + strengthMod
    weight    = "800"
  elif creatureCharNum == 11:
    dexerity  = str(roll_dice(2) + dexterityMod)
    endurance = str(roll_dice(5) + enduranceMod)
    strength  = roll_dice(5) + strengthMod
    weight    = "1600"
  elif creatureCharNum == 12:
    dexerity  = str(roll_dice() + dexterityMod)
    endurance = str(roll_dice(6) + enduranceMod)
    strength  = roll_dice(6) + strengthMod
    weight    = "3200"
  else:
    dexerity  = str(roll_dice() + dexterityMod)
    endurance = str(roll_dice(7) + enduranceMod)
    strength  = roll_dice(7) + strengthMod
    weight    = "5000"

  intelligence = str(roll_dice(1, 0, 1))
  instinct = str(get_creature_instinct(creatureBehaviorNum))
  return [(weight, str(strength), dexerity, endurance, intelligence, instinct)], strength

def gen_creature_characteristics(chosenTerrain):
  if chosenTerrain in (TERRAIN_OPTIONS.Desert, TERRAIN_OPTIONS.Rough_Broken, TERRAIN_OPTIONS.Jungle):
    terrainMod = -3
  elif chosenTerrain in (TERRAIN_OPTIONS.Forest, TERRAIN_OPTIONS.Open_Ocean):
    terrainMod = -4
  elif chosenTerrain == TERRAIN_OPTIONS.Woods:
    terrainMod = -1
  elif chosenTerrain == TERRAIN_OPTIONS.Rainforest:
    terrainMod = -2
  elif chosenTerrain == TERRAIN_OPTIONS.Swamp_Marsh:
    terrainMod = 4
  elif chosenTerrain in (TERRAIN_OPTIONS.Beach_Shore, TERRAIN_OPTIONS.Deep_Ocean):
    terrainMod = 2
  elif chosenTerrain in (TERRAIN_OPTIONS.Riverbank, TERRAIN_OPTIONS.Ocean_Shallows):
    terrainMod = 1
  else:
    terrainMod = 0

  creatureCharRoll = roll_dice(2) + terrainMod
  creatureCharRoll = creatureCharRoll if creatureCharRoll >= 1 else 1
  creatureCharRoll = creatureCharRoll if creatureCharRoll <= 13 else 13

  return creatureCharRoll

def handle_creature_characteristics_gen(funcArgs):
  chosenTerrain    = funcArgs[0]
  creatureBehavior = funcArgs[1]

  strengthMod  = 0
  dexterityMod = 0
  enduranceMod = 0
  if creatureBehavior in (CREATURE_BEHAVIORS.Chaser, CREATURE_BEHAVIORS.Pouncer):
    dexterityMod = 4
  elif creatureBehavior in (CREATURE_BEHAVIORS.Eater, CREATURE_BEHAVIORS.Filter):
    enduranceMod = 4
  elif creatureBehavior == CREATURE_BEHAVIORS.Killer:
    coinFlip = roll_dice(1, 0, 1)
    if coinFlip == 0:
      strengthMod = 4
    else:
      dexterityMod = 4
  elif creatureBehavior == CREATURE_BEHAVIORS.Hijacker:
    strengthMod = 2
  else:
    0 # Do nothing

  creatureCharacteristics = gen_creature_characteristics(chosenTerrain)
  characteristicsTable, creatureStrength = gen_creature_characteristics_info(creatureCharacteristics, creatureBehavior, strengthMod, dexterityMod, enduranceMod)

  characteristicsString  = "Creature Characteristics Info\n" + SEPARATOR_STRING
  characteristicsString += get_table_entry(CREATURE_CHARACTERISTICS_TABLE_HEADER, characteristicsTable, 0) + SEPARATOR_STRING

  return characteristicsString, creatureStrength
#--------------------------------------------------#

# Creature weapons
#--------------------------------------------------#
def get_creature_damage(strength):
  if strength <= 10:
    return "1d6"
  elif strength <= 20:
    return "2d6"
  elif strength <= 30:
    return "3d6"
  elif strength <= 40:
    return "4d6"
  elif strength <= 50:
    return "5d6"
  else:
    return "6d6"

def gen_creature_weapons(creatureType):
  isScavengerType = False
  if creatureType == CREATURE_TYPES.Carnivore:
    creatureTypeMod = 8
  elif creatureType == CREATURE_TYPES.Omnivore:
    creatureTypeMod = 4
  elif creatureType == CREATURE_TYPES.Herbivore:
    creatureTypeMod = -6
  else:
    creatureTypeMod = 0
    isScavengerType = True
  
  creatureWeaponRoll = roll_dice(2) + creatureTypeMod
  return creatureWeaponRoll, isScavengerType

def handle_creature_weapons_gen(funcArgs):
  creatureWeapons, isScavengerType = gen_creature_weapons(funcArgs[0])
  weaponString  = "Creature Weapon Info\n" + SEPARATOR_STRING
  weaponString += "Weapons: "

  damageMod = ""
  if creatureWeapons <= 1:
    weaponString += "Teeth" if isScavengerType else "None"
  elif creatureWeapons in (2,6):
    weaponString += "Teeth"
  elif creatureWeapons == 3:
    weaponString += "Horns"
    weaponString += " and Teeth" if isScavengerType else ""
  elif creatureWeapons == 4:
    weaponString += "Hooves"
    weaponString += " and Teeth" if isScavengerType else ""
  elif creatureWeapons == 5:
    weaponString += "Hooves and Teeth"
  elif creatureWeapons == 7:
    weaponString += "Claws"
    weaponString += " and Teeth" if isScavengerType else ""
    damageMod    += "+1"
  elif creatureWeapons == 8:
    weaponString += "Stinger"
    weaponString += " and Teeth" if isScavengerType else ""
    damageMod    += "+1"
  elif creatureWeapons == 9:
    weaponString += "Thrasher"
    weaponString += " and Teeth" if isScavengerType else ""
    damageMod    += "+1"
  elif creatureWeapons == 10:
    weaponString += "Claws and Teeth"
    damageMod    += "+2"
  elif creatureWeapons == 11:
    weaponString += "Claws"
    weaponString += " and Teeth" if isScavengerType else ""
    damageMod    += "+2"
  elif creatureWeapons == 12:
    weaponString += "Teeth"
    damageMod    += "+2"
  else:
    weaponString += "Thrasher"
    weaponString += " and Teeth" if isScavengerType else ""
    damageMod    += "+2"

  if creatureWeapons > 1 or isScavengerType:
    weaponString += NEW_LINE + "Damage: " + get_creature_damage(funcArgs[1]) + damageMod

  weaponString += NEW_LINE + SEPARATOR_STRING
  return weaponString, creatureWeapons
#--------------------------------------------------#

# Creature armour
#--------------------------------------------------#
CREATURE_ARMOUR_TABLE_HEADER = ["Armour Value"]

CREATURE_ARMOUR_TABLE  = (["0"],["0"],["0"],["0"],["1"],["1"],["2"],["2"],["3"],["3"],["4"],["4"],["5"])

def gen_creature_armour():
  return roll_dice(2)

def handle_creature_armour_gen(funcArgs):
  creatureArmour = gen_creature_armour()
  armourString = "Creature Armour Info\n" + SEPARATOR_STRING
  armourString += get_table_entry(CREATURE_ARMOUR_TABLE_HEADER, CREATURE_ARMOUR_TABLE, creatureArmour) + SEPARATOR_STRING
  return armourString, creatureArmour
#--------------------------------------------------#

# Creature skills
#--------------------------------------------------#
def gen_creature_skills(creatureBehavior):
  survival  = [0, "Survival"]
  athletics = [0, "Athletics"]
  recon     = [0, "Recon"]
  melee     = [1, "Melee"]
  stealth   = [-1, "Stealth"]
  persuade  = [-1, "Persuade"]
  deception = [-1, "Deception"]

  if creatureBehavior == CREATURE_BEHAVIORS.Carrion_Eater:
    recon[0] += 1
  elif creatureBehavior == CREATURE_BEHAVIORS.Chaser:
    athletics[0] += 1
  elif creatureBehavior == CREATURE_BEHAVIORS.Gatherer:
    stealth[0] += 2
  elif creatureBehavior == CREATURE_BEHAVIORS.Hunter:
    survival[0] += 1
  elif creatureBehavior == CREATURE_BEHAVIORS.Intimidator:
    persuade[0] += 2
  elif creatureBehavior == CREATURE_BEHAVIORS.Killer:
    melee[0] += 1
  elif creatureBehavior == CREATURE_BEHAVIORS.Pouncer:
    stealth[0]   += 1
    recon[0]     += 1
    athletics[0] += 1
  elif creatureBehavior == CREATURE_BEHAVIORS.Siren:
    deception[0] += 2
  else:
    0 # Do Nothing

  fullSkillsList = [survival, athletics, recon, melee, stealth, persuade, deception]
  creatureSkillsList = []
  for skill in fullSkillsList:
    if skill[0] >= 0:
      creatureSkillsList.append(skill)

  numRandomRanks = roll_dice()
  creatureSkillsListLen = len(creatureSkillsList) - 1
  i = 0
  while i < numRandomRanks:
    creatureSkillsList[roll_dice(1,0,creatureSkillsListLen)][0] += 1
    i += 1
  
  skillString = ""
  for creatureSkill in creatureSkillsList:
    skillString += creatureSkill[1] + ": " + str(creatureSkill[0]) + NEW_LINE
  
  skillString += SEPARATOR_STRING
  return skillString

def handle_creature_skills_gen(funcArgs):
  skillString   = "Creature Skills Info\n" + SEPARATOR_STRING
  skillString  += gen_creature_skills(funcArgs[0])
  return skillString, 0
#--------------------------------------------------#

# Creature pack
#--------------------------------------------------#
def gen_creature_pack(creatureBehavior):
  if creatureBehavior in (CREATURE_BEHAVIORS.Chaser, CREATURE_BEHAVIORS.Eater, CREATURE_BEHAVIORS.Hijacker, CREATURE_BEHAVIORS.Chaser):
    packMod = 2
  elif creatureBehavior in (CREATURE_BEHAVIORS.Grazer, CREATURE_BEHAVIORS.Intermittent, CREATURE_BEHAVIORS.Reducer):
    packMod = 4
  elif creatureBehavior in (CREATURE_BEHAVIORS.Killer, CREATURE_BEHAVIORS.Trapper):
    packMod = -2
  elif creatureBehavior == CREATURE_BEHAVIORS.Siren:
    packMod = -4
  else:
    packMod = 0
  
  packRoll = roll_dice(2) + packMod
  packRoll = packRoll if packMod >= 0 else 0
  return packRoll

def get_number_encountered(creaturePackNum):
  if creaturePackNum == 0:
    return "1"
  elif creaturePackNum in (1,2):
    return str(roll_dice(1,1,3))
  elif creaturePackNum in (3,4,5):
    return str(roll_dice())
  elif creaturePackNum in (6,7,8):
    return str(roll_dice(2))
  elif creaturePackNum in (9,10,11):
    return str(roll_dice(3))
  elif creaturePackNum in (12,13,14):
    return str(roll_dice(4))
  else:
    return str(roll_dice(5))

def handle_creature_pack_gen(funcArgs):
  creaturePack = gen_creature_pack(funcArgs[0])
  packString   = "Creature Pack Info\n" + SEPARATOR_STRING
  packString  += "Pack Value: " + str(creaturePack) + NEW_LINE
  packString  += "Number Encountered: " + get_number_encountered(creaturePack) + NEW_LINE + SEPARATOR_STRING
  return packString, creaturePack
#--------------------------------------------------#

# Generate a new creature
#--------------------------------------------------#
def generate_creature(creatureGenOption):
  try:
    # Terrain
    if creatureGenOption == INTERACTIVE_GEN_OPTIONS.ReRoll:
      selectedTerrain = user_input_dialog(TERRAIN_OPTIONS, "Decide which terrain this creature resides in.\n")
    else:
      selectedTerrain = TERRAIN_OPTIONS.Random
    
    if selectedTerrain == TERRAIN_OPTIONS.Random:
      selectedTerrain = get_option_by_value(TERRAIN_OPTIONS, roll_dice(1,1,16))

    # Movement
    creatureGenOption, movementString, creatureMovement = do_interactive_gen_loop(creatureGenOption, handle_creature_movement_gen, [selectedTerrain])
    printString = movementString + NEW_LINE

    # Type
    noArgs = []
    creatureGenOption, typeString, creatureType = do_interactive_gen_loop(creatureGenOption, handle_creature_type_gen, noArgs)
    printString += typeString + NEW_LINE

    # Behavior
    creatureGenOption, behaviorString, creatureBehavior = do_interactive_gen_loop(creatureGenOption, handle_creature_behavior_gen, [selectedTerrain, creatureType])
    printString += behaviorString + NEW_LINE

    # Characteristics
    creatureGenOption, characteristicsString, creatureStrength = do_interactive_gen_loop(creatureGenOption, handle_creature_characteristics_gen, [selectedTerrain, creatureBehavior])
    printString += characteristicsString + NEW_LINE

    # Weapons
    creatureGenOption, weaponString, creatureWeapons = do_interactive_gen_loop(creatureGenOption, handle_creature_weapons_gen, [creatureType, creatureStrength])
    printString += weaponString + NEW_LINE

    # Armour
    creatureGenOption, armourString, creatureArmour = do_interactive_gen_loop(creatureGenOption, handle_creature_armour_gen, noArgs)
    printString += armourString + NEW_LINE

    # Behavior
    behaviorArg = [creatureBehavior]
    creatureGenOption, skillString, creatureSkills = do_interactive_gen_loop(creatureGenOption, handle_creature_skills_gen, behaviorArg)
    printString += skillString + NEW_LINE

    # Pack
    creatureGenOption, packString, creaturePack = do_interactive_gen_loop(creatureGenOption, handle_creature_pack_gen, behaviorArg)
    printString += packString + NEW_LINE

    clear_screen()
    print(printString)

  except KeyboardInterrupt:
    clear_screen()
    print("Failed to generate Creature\n")
    printString = ""

  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_creature, "Creature")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
