class Room:
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.destinations = dict()
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, room, destination):
        self.destinations[destination] = room

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for destination, room in self.destinations.items():
            print(f'The {room.name} is {destination}')

    def get_character(self):
        return self.character

    def move(self, direction):
        return self.destinations[direction]


class Enemy:
    total_defeated = [0]
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.phrase = ''
        self.weakness = ''

    def set_conversation(self, phrase):
        self.phrase = phrase

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(f'{self.name} is here')
        print(self.description)

    def talk(self):
        print(f'[{self.name} says]: {self.phrase}')

    def fight(self, weapon):
        if weapon == self.weakness:
            self.total_defeated[0] += 1
            print(f'You fend {self.name} off with the {weapon}')
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False


    @classmethod
    def get_defeated(cls):
        return cls.total_defeated[0]


class Item:
    def __init__(self, name):
        self.name = name
        self.sentence = ''

    def set_description(self, sentence):
        self.sentence = sentence

    def describe(self):
        print(f'The [{self.name}] is here - {self.sentence}')

    def get_name(self):
        return f'{self.name}'




