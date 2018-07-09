import random

class Creature:
    # level
    # name
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # this method will cause the class to represent itself in whatever friendly format
    # you so desire, e.g. if you print the class
    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # you don't have to init because the init is in the base class
    #def __init__(self, name, level):
        # more wizard stuff goes here
        #super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}".format(my_roll))
        print("{} rolls {}".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been defeated!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        #fire_modifier = None
        #if self.breathes_fire:
        #    fire_modifier = 5
        #else:
        #    fire_modifier = 1
        # more efficient if statement
        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier
