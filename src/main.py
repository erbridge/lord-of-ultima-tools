# www.lordofultima.com/en/wiki/view/units


class Units:
    
    def __init__(self, name, number, type, wood, stone, iron, food, gold, space,
                 speed, loot, attack, infantry, cavalry, magic, artillery,
                 defDamage=0, damage=0, capacity=0):
        self._name = name
        self._type = type
        self._wood = wood
        self._stone = stone
        self._iron = iron
        self._food = food
        self._gold = gold
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
                
        
class Guards(Units):
    
    def __init__(self, number):
        Units.__init__(self, "City Guard(s)", number, "i", 100, 0, 0, 2, 0,
                       0, 0, 0, 10, 10, 10, 10, 10)


class Berserkers(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Berserker(s)", number, "i", 0, 0, 150, 6, 0,
                       1, 20, 10, 50, 15, 12, 10, 15)
        
        
class Rangers(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Ranger(s)", number, "i", 0, 0, 150, 6, 0,
                       1, 20, 10, 50, 15, 12, 10, 15)
        

class Guardians(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Guardian(s)", number, "i", 0, 0, 120, 3, 60,
                       1, 20, 20, 10, 30, 50, 20, 15)
        

class Scouts(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Scout(s)", number, "c", 0, 0, 40, 5, 120,
                       2, 8, 0, 10, 10, 10, 10, 10)
        
    
class Crossbowmen(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Crossbowmen", number, "c", 150, 0, 0, 10, 200,
                       2, 10, 15, 40, 40, 90, 30, 40)
        
    
class Knights(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Knight(s)", number, "c", 0, 0, 250, 25, 100,
                       2, 10, 15, 90, 40, 30, 20, 40)
        
        
class Magi(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Magi", number, "m", 0, 0, 50, 5, 150,
                       1, 20, 5, 70, 15, 10, 30, 15)
        

class Warlocks(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Warlock(s)", number, "m", 0, 0, 100, 20, 350,
                       2, 10, 10, 120, 30, 20, 50, 40)
        
        
class Templars(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Templar(s)", number, "i", 0, 0, 90, 3, 100,
                       1, 20, 10, 25, 20, 30, 50, 15)
        
    
class Paladins(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Paladin(s)", number, "c", 0, 0, 200, 15, 160,
                       2, 10, 20, 60, 50, 20, 90, 40)
        
        
class Barons(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Baron(s)", number, "i", 0, 0, 50000, 100, 100000,
                       1, 40, 0, 10, 100, 50, 20, 10)
        
        
class Rams(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Ram(s)", number, "a", 500, 0, 300, 50, 0,
                       10, 30, 0, 50, 20, 20, 20, 50, defDamage=250)
        
        
class Ballistae(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Ballista(e)", number, "a", 400, 0, 600, 25, 0,
                       10, 30, 0, 50, 200, 100, 200, 400)
        
        
class Catapults(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Catapult(s)", number, "a", 300, 600, 200, 50, 0,
                       10, 30, 0, 150, 100, 100, 200, 50, damage=250)
        
        
class Sloops(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Sloop(s)", number, "a", 6000, 0, 4000, 300, 2000,
                       100, 5, 1500, 1200, 4500, 4500, 2000, 6000)
        
    
class Frigates(Units):
    
    def __init__(self, number):
        Units.__init__(self, "Frigate(s)", number, "a", 15000, 0, 5000, 500,
                       5000, 100, 5, 1000, 3000, 4000, 4000, 2000, 2000,
                       capacity=500)
        
        
class Galleons(Units):
    
    def __init__(self, number):
        Units.__init__(self, "War Galleon(s)", number, "a", 30000, 0, 10000,
                       2500, 20000, 400, 5, 3000, 12000, 5000, 5000, 2500, 6000,
                       defDamage=4000, damage=4000)
        

class Monsters:
    
    def __init__(self, name, number, type, attack, infantry, cavalry, magic,
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
        
        
class Skeletons(Monsters):
    
    def __init__(self, number):
        Monsters.__init__(self, "Skeleton(s)", number, "h",
                          50, 16, 16, 10, 16, 1, 25)
        

class Ghouls(Monsters):
    
    def __init__(self, number):
        Monsters.__init__(self, "Ghoul(s)", number, "h",
                          75, 30, 30, 15, 30, 1, 33)
        
        
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
    
    def __init__(self, army, expectedMonsters=None, dungeon=None):
        self._army = army
        if dungeon:
            self._expectedMonsters = dungeon.getMonsters()
        else:
            self._expectedMonsters = expectedMonsters