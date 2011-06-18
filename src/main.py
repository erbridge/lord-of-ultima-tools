# Copyright (c) 2011, Felix Laurie von Massenbach <fantasizer@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#        this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
# 3. Neither the names of the copyright holders nor the names of its
#        contributors may be used to endorse or promote products derived from
#        this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# www.lordofultima.com/en/wiki/view/units
# FIXME: stop calculation from using sea units for land dungeons.


import copy, Tkinter, tkMessageBox, tkFileDialog


class NotCreatedError(Exception):   pass


class TypeMismatchError(Exception): pass


class NoMonsterError(Exception):    pass


class InsufficientTroopsError(Exception):   pass


class LevelError(Exception):   pass


class Units:
    
    def __init__(self, name, type, wood, stone, iron, food, gold, space,
                 speed, loot, attack, infantry, cavalry, magic, artillery,
                 defDamage=0, damage=0, capacity=0):
        self._name = name
        self._type = type
        self._wood = wood
        self._stone = stone
        self._iron = iron
        self._food = food
        self._gold = gold
        self._unitCost = wood + stone + iron + gold
        self._space = space
        self._speed = speed
        self._loot = loot
        self._attack = attack
        self._infantry = infantry
        self._cavalry = cavalry
        self._magic = magic
        self._artillery = artillery
        self._defDamage = defDamage
        self._damage = damage
        self._capacity = capacity
        self._combatResearch = 1
        
    def create(self, number):
        unit = copy.deepcopy(self)
        unit._number = number
        return unit
    
    def setResearch(self, combatResearch=1):
        self._combatResearch = combatResearch
            
    def getName(self):
        return self._name
    
    def getNumber(self):
        try:
            return self._number
        except AttributeError:
            raise NotCreatedError
        
    def getType(self):
        return self._type
    
    def getAttack(self):
        return self._attack * self._combatResearch
    
    def getCost(self):
        return self.getNumber() * self._unitCost
    
    def getUnitLoot(self):
        return self._loot
                
        
class Guards(Units):
    
    def __init__(self):
        Units.__init__(self, "City Guard(s)", "i", 100, 0, 0, 2, 0,
                       0, 0, 0, 10, 10, 10, 10, 10)


class Berserkers(Units):
    
    def __init__(self):
        Units.__init__(self, "Berserker(s)", "i", 0, 0, 150, 6, 0,
                       1, 20, 10, 50, 15, 12, 10, 15)
        
        
class Rangers(Units):
    
    def __init__(self):
        Units.__init__(self, "Ranger(s)", "i", 160, 0, 0, 3, 0,
                       1, 20, 10, 30, 40, 10, 25, 15)
        

class Guardians(Units):
    
    def __init__(self):
        Units.__init__(self, "Guardian(s)", "i", 0, 0, 120, 3, 60,
                       1, 20, 20, 10, 30, 50, 20, 15)
        

class Scouts(Units):
    
    def __init__(self):
        Units.__init__(self, "Scout(s)", "c", 0, 0, 40, 5, 120,
                       2, 8, 0, 10, 10, 10, 10, 10)
        
    
class Crossbowmen(Units):
    
    def __init__(self):
        Units.__init__(self, "Crossbowmen", "c", 150, 0, 0, 10, 200,
                       2, 10, 15, 40, 40, 90, 30, 40)
        
    
class Knights(Units):
    
    def __init__(self):
        Units.__init__(self, "Knight(s)", "c", 0, 0, 250, 25, 100,
                       2, 10, 15, 90, 40, 30, 20, 40)
        
        
class Magi(Units):
    
    def __init__(self):
        Units.__init__(self, "Magi", "m", 0, 0, 50, 5, 150,
                       1, 20, 5, 70, 15, 10, 30, 15)
        

class Warlocks(Units):
    
    def __init__(self):
        Units.__init__(self, "Warlock(s)", "m", 0, 0, 100, 20, 350,
                       2, 10, 10, 120, 30, 20, 50, 40)
        
        
class Templars(Units):
    
    def __init__(self):
        Units.__init__(self, "Templar(s)", "i", 0, 0, 90, 3, 100,
                       1, 20, 10, 25, 20, 30, 50, 15)
        
    
class Paladins(Units):
    
    def __init__(self):
        Units.__init__(self, "Paladin(s)", "c", 0, 0, 200, 15, 160,
                       2, 10, 20, 60, 50, 20, 90, 40)
        
        
class Barons(Units):
    
    def __init__(self):
        Units.__init__(self, "Baron(s)", "i", 0, 0, 50000, 100, 100000,
                       1, 40, 0, 10, 100, 50, 20, 10)
        
        
class Rams(Units):
    
    def __init__(self):
        Units.__init__(self, "Ram(s)", "a", 500, 0, 300, 50, 0,
                       10, 30, 0, 50, 20, 20, 20, 50, defDamage=250)
        
        
class Ballistae(Units):
    
    def __init__(self):
        Units.__init__(self, "Ballista(e)", "a", 400, 0, 600, 25, 0,
                       10, 30, 0, 50, 200, 100, 200, 400)
        
        
class Catapults(Units):
    
    def __init__(self):
        Units.__init__(self, "Catapult(s)", "a", 300, 600, 200, 50, 0,
                       10, 30, 0, 150, 100, 100, 200, 50, damage=250)
        
        
class Sloops(Units):
    
    def __init__(self):
        Units.__init__(self, "Sloop(s)", "a", 6000, 0, 4000, 300, 2000,
                       100, 5, 1500, 1200, 4500, 4500, 2000, 6000)
        
    
class Frigates(Units):
    
    def __init__(self):
        Units.__init__(self, "Frigate(s)", "a", 15000, 0, 5000, 500,
                       5000, 100, 5, 1000, 3000, 4000, 4000, 2000, 2000,
                       capacity=500)
        
        
class Galleons(Units):
    
    def __init__(self):
        Units.__init__(self, "War Galleon(s)", "a", 30000, 0, 10000,
                       2500, 20000, 400, 5, 3000, 12000, 5000, 5000, 2500, 6000,
                       defDamage=4000, damage=4000)
        

UNITS = [Guards(), Berserkers(), Rangers(), Guardians(), Scouts(),
         Crossbowmen(), Knights(), Magi(), Warlocks(), Templars(), Paladins(),
         Barons(), Rams(), Ballistae(), Catapults(), Sloops(), Frigates(),
         Galleons()]
        

class Monsters:
    
    def __init__(self, name, type, attack, infantry, cavalry, magic,
                 artillery, heads, loot):
        self._name = name
        self._type = type
        self._attack = attack
        self._infantry = infantry
        self._cavalry = cavalry
        self._magic = magic
        self._artillery = artillery
        self._heads = heads
        self._loot = loot
        
    def create(self, number):
        monster = copy.deepcopy(self)
        monster._number = number
        return monster
            
    def getName(self):
        return self._name
    
    def getNumber(self):
        try:
            return self._number
        except AttributeError:
            raise NotCreatedError
    
    def getType(self):
        return self._type
    
    def getDefense(self, type):
        if type == "i":
            return self._infantry
        elif type == "c":
            return self._cavalry
        elif type == "m":
            return self._magic
        else:
            return self._artillery
        
    def getLoot(self):
        return self.getNumber() * self._loot
        
        
class Skeletons(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Skeleton(s)", "h",
                          50, 16, 16, 10, 16, 1, 25)
        

class Ghouls(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Ghoul(s)", "h",
                          75, 30, 30, 15, 30, 1, 33)
        

class Gargoyles(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Gargoyle(s)", "h",
                          200, 80, 80, 40, 80, 4, 135)
        

class Daemons(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Daemons(s)", "h",
                          500, 200, 200, 100, 200, 10, 340)
        

class Orcs(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Orc(s)", "m",
                          60, 12, 22, 22, 22, 1, 30)
        
        
class Troglodytes(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Troglodyte(s)", "m",
                          90, 16, 33, 33, 33, 1, 40)
        
        
class Ettins(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Ettin(s)", "m",
                          180, 37, 75, 75, 75, 3, 120)
        
        
class Minotaurs(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Minotaur(s)", "m",
                          400, 75, 150, 150, 150, 6, 250)
        
        
class Spiders(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Giant Spider(s)", "f",
                          55, 16, 6, 16, 16, 1, 25)


class Thieves(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Thieves", "f",
                          80, 28, 14, 28, 28, 1, 33)
        
        
class Centaurs(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Centaur(s)", "f",
                          110, 40, 20, 40, 40, 2, 70)
        
        
class Trolls(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Troll(s)", "f",
                          450, 160, 80, 160, 160, 8, 290)
        

class PirateDhows(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Pirate Dhow(s)", "s",
                          150, 60, 60, 60, 30, 3, 75)
        
        
class PirateSloops(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Pirate Sloop(s)", "s",
                          500, 200, 200, 200, 100, 10, 250)
        
        
class PirateFrigates(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Pirate Frigate(s)", "s",
                          1250, 500, 500, 500, 250, 25, 650)
        
        
class PirateGalleons(Monsters):
    
    def __init__(self):
        Monsters.__init__(self, "Pirate War Galleon(s)", "s",
                          2500, 1000, 1000, 1000, 500, 50, 1400)
        
        
MONSTERS = [Skeletons(), Ghouls(), Gargoyles(), Daemons(), Orcs(),
            Troglodytes(), Ettins(), Minotaurs(), Spiders(), Thieves(),
            Centaurs(), Trolls(), PirateDhows(), PirateSloops(),
            PirateFrigates(), PirateGalleons()]


BOSS_STATS = [(1, 2500, 625, 420, 500),
              (2, 1500, 3750, 2500, 3000),
              (3, 100000, 25000, 17000, 20000),
              (4, 200000, 50000, 33000, 40000),
              (5, 500000, 125000, 83000, 100000),
              (6, 750000, 187500, 125000, 150000),
              (7, 1000000, 250000, 170000, 200000),
              (8, 1500000, 375000, 250000, 300000),
              (9, 2250000, 562500, 375000, 450000),
              (10, 3000000, 750000, 500000, 600000)]


class Boss(Monsters):   
    
    def __init__(self, name):
        self._name = name
        self._number = 1
        
        
    def create(self, level):
        if level > 10 or level <= 0:
            raise LevelError
        lvl, attack, strongDefence, weakDefence, loot = BOSS_STATS[level-1]
        
        assert lvl == level
        
        infantry, cavalry, magic, artillery = self.getDefences(strongDefence,
                                                               weakDefence)
        boss = copy.deepcopy(self)    
        Monsters.__init__(boss, boss.getName(), boss.getType(), attack,
                          infantry,  cavalry, magic, artillery, 20, loot)
        return boss
            
    def getDefences(self, strongDefence, weakDefence):
        if self._name == "Moloch":
            return strongDefence, strongDefence, weakDefence, strongDefence
        elif self._name == "Hydra":
            return weakDefence, strongDefence, strongDefence, strongDefence
        elif self._name == "Dragon":
            return strongDefence, weakDefence, strongDefence, strongDefence
        elif self._name == "Octopus":
            return strongDefence, strongDefence, strongDefence, weakDefence
        
    def getType(self):
        if self._name == "Moloch":
            return "h"
        elif self._name == "Hydra":
            return "m"
        elif self._name == "Dragon":
            return "f"
        elif self._name == "Octopus":
            return "s"


class Moloch(Boss):
    
    def __init__(self):
        Boss.__init__(self, "Moloch")


class Hydra(Boss):
    
    def __init__(self):
        Boss.__init__(self, "Hydra")
        
        
class Dragon(Boss):
    
    def __init__(self):
        Boss.__init__(self, "Dragon")        
        
        
class Octopus(Boss):
    
    def __init__(self):
        Boss.__init__(self, "Octopus")
        
        
BOSSES = [Moloch(), Hydra(), Dragon(), Octopus()]

        
class Dungeon:
    
    def __init__(self, level, progress):
        self._level = level
        self._progress = progress
        
    def getMonsters(self):
        return self._monsters
        
        
class Hill(Dungeon):
    
    def __init__(self, level, progress):
        Dungeon.__init__(self, level, progress)
        
        if level == 1:
            self._monsters = [Skeletons(10*progress)]
        
        
class Mountain(Dungeon):
    
    def __init__(self, level, progress):
        Dungeon.__init__(self, level, progress)
        
        if level == 1:
            self._monsters = []
        
        
class Forest(Dungeon):
    
    def __init__(self, level, progress):
        Dungeon.__init__(self, level, progress)
        
        if level == 1:
            self._monsters = []
        
        
class Sea(Dungeon):
    
    def __init__(self, level, progress):
        Dungeon.__init__(self, level, progress)
        
        if level == 1:
            self._monsters = []
        

class Raid:
    
    def __init__(self, army, expectedMonsters, intensity):
        self._army = army
        self._expectedMonsters = expectedMonsters
        self._intensity = intensity
            
    def getRecommended(self):
        try:
            dungeonType = self._expectedMonsters[0].getType()
        except IndexError:
            raise NoMonsterError
        for monster in self._expectedMonsters:
            if monster.getType() != dungeonType:
                raise TypeMismatchError
        
        priorities = sorted(self.getCasualties(), key=lambda x: x.getCost())
        maxima = self.getMaxima()
        army = copy.deepcopy(UNITS)
        armyComplete = False
        proportion = 1
        for priorityUnit in priorities:
            if armyComplete:
                break
            for unit in self._army:
                if priorityUnit.getName() == unit.getName():
                    for maxUnit in maxima:
                        if maxUnit.getName() == unit.getName():
                            number = maxUnit.getNumber()\
                                + priorityUnit.getNumber()
                            weightedNumber = number * proportion
                            if weightedNumber <= unit.getNumber():
                                for id in xrange(len(UNITS)):
                                    if UNITS[id].getName() == unit.getName():
                                        army[id] = UNITS[id].create(
                                            int(weightedNumber))
                                        break
                                armyComplete = True
                            else:
                                # TODO: Is this right?
                                proportion -= float(unit.getNumber()) / number
                                for id in xrange(len(UNITS)):
                                    if UNITS[id].getName() == unit.getName():
                                        army[id] = unit
                                        break
                            break
                    break
        if not armyComplete:
            raise InsufficientTroopsError
        return army
        
    def getCasualties(self):
        casualties = []
        for unit in UNITS:
            type = unit.getType()
            attack = unit.getAttack()
            number = 0
            for monster in self._expectedMonsters:
                number += round(float(monster.getNumber()\
                                      * monster.getDefense(type))\
                                * self._intensity / float(attack))
            casualties.append(unit.create(number))
        return casualties
    
    def getMaxima(self):
        maxima = []
        loot = self.getLoot()
        for unit in UNITS:
            try:
                maxima.append(
                    unit.create(round(float(loot) / float(unit.getUnitLoot()))))
            except ZeroDivisionError:
                continue
        return maxima
    
    def getLoot(self):
        loot = 0
        for monster in self._expectedMonsters:
            loot += monster.getLoot()
        return loot
    
    
class DungeonRaid(Raid):
    
    def __init__(self, army, expectedMonsters=None, dungeon=None):
        if dungeon is not None:
            expectedMonsters = dungeon.getMonsters()
        
        if expectedMonsters is None:
            raise NoMonsterError
        
        Raid.__init__(self, army, expectedMonsters, 0.1)
            
            
class BossRaid(Raid):
    
    def __init__(self, army, boss):
        Raid.__init__(self, army, boss, 0.5*0.2) # Assume the boss is killed.
        

class App:
    
    def __init__(self, master):
        self._master = master
        self._frame = Tkinter.Frame(master)
        self._frame.pack()
        
        self._views = []
        self._enemyInput = []
        self._output = []
                
        self._createUnitInputBoxes()
        self._createMonsterInputBoxes()
        self._createBossInputBoxes()
        self._createRecommendationBoxes()
        self._createButtons()
        
        self._createMenus()
        
        self._views[0].grid(row=0, column=1, sticky=Tkinter.N)
        self._oldView = Tkinter.IntVar()
        self._oldView.set(self._view.get())
        
    def _createUnitInputBoxes(self):
        unitFrame = Tkinter.Frame(self._frame)
        Tkinter.Label(
            unitFrame, text="Available Units and Combat Research:").pack()
        frame = Tkinter.Frame(unitFrame)
        self._unitInput = [None]*len(UNITS)
        self._combatResearchInput = [None]*len(UNITS)
        for id in xrange(len(UNITS)):
            self._unitInput[id] = Tkinter.Entry(frame)
            self._unitInput[id].grid(row=id, column=0)
            Tkinter.Label(frame, text=" (").grid(row=id, column=1)
            self._combatResearchInput[id] = Tkinter.Entry(frame, width=3)
            self._combatResearchInput[id].grid(row=id, column=2)
            Tkinter.Label(
                frame, text="%)  "+UNITS[id].getName()).grid(
                    row=id, column=3, sticky=Tkinter.W)
        frame.pack()
        unitFrame.grid(row=0, column=0, sticky=Tkinter.N)
                
    def _createMonsterInputBoxes(self):
        self._monsterFrame = Tkinter.Frame(self._frame)
        
        Tkinter.Label(self._monsterFrame, text="Expected Monsters:").pack()
        
        frame = Tkinter.Frame(self._monsterFrame)
        self._monsterInput = [None]*len(MONSTERS)
        for id in xrange(len(MONSTERS)):
            self._monsterInput[id] = Tkinter.Entry(frame)
            self._monsterInput[id].grid(row=id, column=0)
            Tkinter.Label(
                frame, text=MONSTERS[id].getName()).grid(
                    row=id, column=1, sticky=Tkinter.W)
        frame.pack()
        
        self._views.append(self._monsterFrame)
        
        self._enemyInput.extend(self._monsterInput)
        
    def _createBossInputBoxes(self):
        self._bossFrame = Tkinter.Frame(self._frame)
        
        Tkinter.Label(self._bossFrame, text="Boss Level:").pack()
        
        frame = Tkinter.Frame(self._bossFrame)
        self._bossInput = [None]*len(BOSSES)
        for id in xrange(len(BOSSES)):
            self._bossInput[id] = Tkinter.Entry(frame, width=2)
            self._bossInput[id].grid(row=id, column=0)
            Tkinter.Label(
                frame, text=BOSSES[id].getName()).grid(
                    row=id, column=1, sticky=Tkinter.W)
        frame.pack()
        
        self._views.append(self._bossFrame)
        
        self._enemyInput.extend(self._bossInput)
                
    def _createRecommendationBoxes(self):
        recFrame = Tkinter.Frame(self._frame)
        Tkinter.Label(recFrame, text="Recommended Units:").pack()
        frame = Tkinter.Frame(recFrame)
        self._unitOutput = [None]*len(UNITS)
        for id in xrange(len(UNITS)):
            self._unitOutput[id] = Tkinter.Label(frame, width=16)
            self._unitOutput[id].grid(row=id, column=0)
            Tkinter.Label(
                frame, text=UNITS[id].getName()).grid(
                    row=id, column=1, sticky=Tkinter.W)
        frame.pack()
        recFrame.grid(row=0, column=2, sticky=Tkinter.N)
        
        self._output.extend(self._unitOutput)
        
    def _createButtons(self):
        frame = Tkinter.Frame(self._frame)
        Tkinter.Button(
            frame, text="Calculate", command=self._onCalculate).grid(
                row=0, column=0)
        Tkinter.Button(
            frame, text="Send Units", command=self._onSend).grid(
                row=0, column=1)
        Tkinter.Button(
            frame, text="Save Army", command=self._onSave).grid(
                row=0, column=2)
        Tkinter.Button(
            frame, text="Load Army", command=self._onLoad).grid(
                row=0, column=3)
        frame.grid(row=1, columnspan=3)#, sticky=Tkinter.E)
        
    def _onCalculate(self, sent=False):
        units = []#[None]*len(UNITS)
        for id in xrange(len(UNITS)):
            combatResearch = self._combatResearchInput[id].get()
            try:
                combatResearch = float(combatResearch) / 100. + 1.
                if combatResearch > 1:
                    UNITS[id].setResearch(combatResearch)
                elif combatResearch < 0:
                    self._popupDialog(
                        "You need a positive research percentage.")
                    return None
            except ValueError:
                UNITS[id].setResearch()
            
            unitNumber = self._unitInput[id].get()
            try:
                unitNumber = int(unitNumber)
                if unitNumber > 0:
                    units.append(UNITS[id].create(unitNumber))
                elif unitNumber < 0:
                    self._popupDialog("You need a positive number of units.")
                    return None
            except ValueError:
                pass
                
        monsters = []
        for id in xrange(len(MONSTERS)):
            monsterNumber = self._monsterInput[id].get()
            try:
                monsterNumber = int(monsterNumber)
                if monsterNumber:
                    monsters.append(MONSTERS[id].create(monsterNumber))
            except ValueError:
                pass
        
        boss = []
        for id in xrange(len(BOSSES)):
            bossLevel = self._bossInput[id].get()
            try:
                bossLevel = int(bossLevel)
                if bossLevel:
                    boss.append(BOSSES[id].create(bossLevel))
            except ValueError:
                pass
            except LevelError:
                self._popupDialog(
                    "A boss' maximum level must be between 1 and 10!")
                return None
        
        if monsters and boss:
            self._popupDialog("You can't mix monsters with bosses!")
            return None
        elif boss:
            raid = BossRaid(units, boss)
        else:
            raid = DungeonRaid(units, expectedMonsters=monsters)
            
        try:
            recommendations = raid.getRecommended()
        except InsufficientTroopsError:
            if not sent:
                msg = "Insufficient troops, but you may be able "\
                    "to get away with sending them all!"
            else:
                msg = "Insufficient troops for another raid."
            self._popupDialog(msg)
            return None
        except NoMonsterError:
            self._popupDialog(
                "What? No monsters?")
            return None
        except TypeMismatchError:
            if boss:
                msg = "You can only raid one boss at a time!"
            else:
                "Monsters need to come from the same dungeon type!"
            self._popupDialog(msg)
            return None
        
        for id in xrange(len(UNITS)):
            try:
                number = recommendations[id].getNumber()
                if number:
                    self._unitOutput[id]["text"] = number
                else:
                    self._unitOutput[id]["text"] = ""
            except NotCreatedError:
                self._unitOutput[id]["text"] = ""
            except AttributeError:
                self._unitOutput[id]["text"] = ""
                
    def _popupDialog(self, message):
        tkMessageBox.showwarning("", message)
        
    def _onSend(self):
        for id in xrange(len(UNITS)):
            try:
                remaining = int(self._unitInput[id].get())\
                    - int(self._unitOutput[id]["text"])
                self._unitInput[id].delete(0, Tkinter.END)
                self._unitInput[id].insert(Tkinter.END, remaining)
            except ValueError:
                continue
        self._onCalculate(sent=True)
        
    def _onSave(self):
        try:
            with tkFileDialog.asksaveasfile(
                mode="w", defaultextension=".arm",
                filetypes=[("Army save files", ".arm")]) as file:
                    file.write("Units\n")
                    for id in xrange(len(UNITS)):
                        file.write(self._unitInput[id].get()+"\n")
                    file.write("\nCombat Research\n")
                    for id in xrange(len(UNITS)):
                        file.write(self._combatResearchInput[id].get()+"\n")
        except AttributeError:
            pass
                
    def _onLoad(self):
        filename = tkFileDialog.askopenfilename(
            filetypes=[("Army save files", ".arm"),
                       ("Old raid save files", ".sav")])
        if not filename:
            return None
        with open(filename, "rU") as file:
            file.readline()
            for id in xrange(len(UNITS)):
                self._unitInput[id].delete(0, Tkinter.END)
                self._unitInput[id].insert(Tkinter.END,
                                           file.readline().strip())
                self._unitOutput[id]["text"] = ""
            file.readline()
            file.readline()
            for id in xrange(len(UNITS)):
                self._combatResearchInput[id].delete(0, Tkinter.END)
                self._combatResearchInput[id].insert(
                    Tkinter.END, file.readline().strip())
            if filename[-4:] != ".sav":
                return None
            file.readline()
            file.readline()
            for id in xrange(len(MONSTERS)):
                self._monsterInput[id].delete(0, Tkinter.END)
                self._monsterInput[id].insert(Tkinter.END,
                                              file.readline().strip())
                
    def _createMenus(self):
        menubar = Tkinter.Menu(self._master)
                
        self._view = Tkinter.IntVar()
        self._view.set(0)
        
        view = Tkinter.Menu(menubar, tearoff=0)
        view.add_radiobutton(label="Monsters", command=self._changeView,
                             variable=self._view, value=0)
        view.add_radiobutton(label="Boss", command=self._changeView,
                             variable=self._view, value=1)
        menubar.add_cascade(label="Type", menu=view)
        
        self._master.config(menu=menubar)
        
    def _changeView(self):
        self._views[self._oldView.get()].grid_forget()
        self._views[self._view.get()].grid(row=0, column=1, sticky=Tkinter.N)
        self._oldView.set(self._view.get())
        
        for input in self._enemyInput:
            input.delete(0, Tkinter.END)
        
        for output in self._output:
            output["text"] = ""
        
            
if __name__ == "__main__":
    main = Tkinter.Tk()
    main.title("Lord of Ultima: Raid Calculator")
    
    app = App(main)
    
    main.mainloop()
