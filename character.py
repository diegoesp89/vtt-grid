class Character:
    name = ""
    race = ""
    char_class = ""
    subclass = ""
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    strength_save = 0
    dexterity_save = 0
    constitution_save = 0
    intelligence_save = 0
    wisdom_save = 0
    charisma_save = 0
    hp = 0
    max_hp = 0
    ac = 0
    speed = 0
    conditions = []
    skills = []
    spells = []
    items = []
    feats = []
    languages = []
    proficiencies = []
    xp = 0
    level = 0
    magic_skill = ""
    pos_x = 0
    pos_y = 0

    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, hp, ac, speed, conditions, skills, spells, items, feats, languages, proficiencies, xp, level, char_class, subclass, strength_save, dexterity_save, constitution_save, intelligence_save, wisdom_save, charisma_save, magic_skill, pos_x, pos_y):
        self.name = name or "Player"
        self.strength = strength or 10
        self.dexterity = dexterity or 10
        self.constitution = constitution or 10
        self.intelligence = intelligence or 10
        self.wisdom = wisdom or 10
        self.hp = hp or 10
        self.max_hp = hp or 10
        self.ac = ac or 15
        self.speed = speed or 30
        self.conditions = conditions or []
        self.skills = skills or []
        self.spells = spells or []
        self.items = items or []
        self.feats = feats or []
        self.languages = languages or []
        self.proficiencies = proficiencies or []
        self.xp = xp or 0
        self.level = level or 1
        self.char_class = char_class or "Fighter"
        self.subclass = subclass or "Champion"
        self.strength_save = strength_save or 0
        self.dexterity_save = dexterity_save or 0
        self.constitution_save = constitution_save or 0
        self.intelligence_save = intelligence_save or 0
        self.wisdom_save = wisdom_save or 0
        self.charisma_save = charisma_save or 0
        self.magic_skill = magic_skill or "intelligence"
        self.pos_x = pos_x or 0
        self.pos_y = pos_y or 0
    
