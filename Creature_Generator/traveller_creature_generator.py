#!/usr/bin/env python3

from enum import Enum
from sys import path

path.append("..")
from support_functions import *

# Creature Movement
#--------------------------------------------------#
CREATURE_MOVEMENT_TABLE_HEADER = ["Creature Movement"]

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
#--------------------------------------------------#

# Creature Type
#--------------------------------------------------#
class CREATURE_TYPES(Enum):
  Scavenger = (2,4,10)
  Omnivore  = (3,5)
  Herbivore = (6,7,8)
  Carnivore = (9,11,12)

def gen_creature_type():
  creatureTypeRoll = roll_dice(2)
  for creatureTypeEntry in CREATURE_TYPES:
    if creatureTypeRoll in creatureTypeEntry.value:
      creatureType = creatureTypeEntry
      break
  return creatureType
#--------------------------------------------------#

# Creature Behavior
#--------------------------------------------------#
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
#--------------------------------------------------#

# Creature characteristics
#--------------------------------------------------#
CREATURE_CHARACTERISTICS_TABLE_HEADER = ("Weight (kg)", "Strength", "Dexterity", "Endurance", "Intellegence", "Damage")

def gen_creature_characteristics(chosenTerrain, creatureBehavior):
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

  if chosenTerrain in (TERRAIN_OPTIONS.Desert, TERRAIN_OPTIONS.Jungle):
    terrainMod = -3
  else:
    terrainMod = 0

#--------------------------------------------------#

# Creature movement generation
#--------------------------------------------------#
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
    movementTable == RIVERBANK_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Ocean_Shallows:
    movementTable = SHALLOWS_MOVEMENT_TABLE
  elif chosenTerrain == TERRAIN_OPTIONS.Open_Ocean:
    movementTable = OPEN_MOVEMENT_TABLE
  else:
    movementTable = DEEP_MOVEMENT_TABLE
  
  movementString  = "Creature Movement Info\n" + SEPARATOR_STRING
  movementString += get_table_entry(CREATURE_MOVEMENT_TABLE_HEADER, movementTable, creatureMovement) + SEPARATOR_STRING
  return movementString, creatureMovement
#--------------------------------------------------#

# Creature type generation
#--------------------------------------------------#
def handle_creature_type_gen(funcArgs):
  creatureType = gen_creature_type()
  typeString   = "Creature Type Info\n" + SEPARATOR_STRING
  typeString  += "Creature Type: " + creatureType.name + NEW_LINE + SEPARATOR_STRING
  return typeString, creatureType
#--------------------------------------------------#

# Creature behavior generation
#--------------------------------------------------#
def handle_creature_behavior_gen(funcArgs):
  creatureBehavior = gen_creature_behavior(funcArgs[0], funcArgs[1])
  behaviorString   = "Creature Behavior Info\n" + SEPARATOR_STRING
  behaviorString  += "Creature Behavior: " + creatureBehavior.name + NEW_LINE + \
                     "Description: " + creatureBehavior.value + NEW_LINE + SEPARATOR_STRING
  return behaviorString, creatureBehavior
#--------------------------------------------------#

# Generate a new creature
#--------------------------------------------------#
class TERRAIN_OPTIONS(Enum):
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

def generate_creature(creatureGenOption):
  selectedTerrain = user_input_dialog(TERRAIN_OPTIONS, "Decide which terrain this creature resides in.\n")

  creatureGenOption, movementString, creatureMovement = do_interactive_gen_loop(creatureGenOption, handle_creature_movement_gen, [selectedTerrain])
  printString = movementString + NEW_LINE

  creatureGenOption, typeString, creatureType = do_interactive_gen_loop(creatureGenOption, handle_creature_type_gen, [])
  printString += typeString + NEW_LINE

  creatureGenOption, behaviorString, creatureBehavior = do_interactive_gen_loop(creatureGenOption, handle_creature_behavior_gen, [selectedTerrain, creatureType])
  printString += behaviorString + NEW_LINE

  clear_screen()
  print(printString)
  return printString
#--------------------------------------------------#

# Main
#--------------------------------------------------#
def main():
  do_main_loop(__file__, generate_creature, "Creature")

if __name__ == "__main__":
  main()
#--------------------------------------------------#
