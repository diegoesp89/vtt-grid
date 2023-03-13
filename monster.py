class Monster:
    slug = ""
    name = ""
    size = ""
    type = ""
    subtype = ""
    group = ""
    alignment = ""
    armor_class = 0
    armor_desc = ""
    hit_points = 0
    max_hit_points = 0
    hit_dice = ""
    speed = {}
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
    perception = 0
    skills = {}
    damage_vulnerabilities = ""
    damage_resistances = ""
    damage_immunities = ""
    condition_immunities = ""
    senses = ""
    languages = ""
    challenge_rating = 0
    cr = 0
    actions = []
    reactions = []
    legendary_desc = ""
    legendary_actions = []
    special_abilities = []
    spell_list = []
    img_main = ""
    document__slug = ""
    document__title = ""
    document__license_url = ""

    def __init__(self, slug, name, size, type, subtype, group, alignment, armor_class, armor_desc, hit_points, max_hit_points, hit_dice, speed, strength, dexterity, constitution, intelligence, wisdom, charisma, strength_save, dexterity_save, constitution_save, intelligence_save, wisdom_save, charisma_save, perception, skills, damage_vulnerabilities, damage_resistances, damage_immunities, condition_immunities, senses, languages, challenge_rating, cr, actions, reactions, legendary_desc, legendary_actions, special_abilities, spell_list, img_main, document__slug, document__title, document__license_url):
        self.slug = slug or ""
        self.name = name or ""
        self.size = size or ""
        self.type = type or ""
        self.subtype = subtype or ""
        self.group = group or ""
        self.alignment = alignment or ""
        self.armor_class = armor_class or 0
        self.armor_desc = armor_desc or ""
        self.hit_points = hit_points or 0
        self.max_hit_points = max_hit_points or 0
        self.hit_dice = hit_dice or ""
        self.speed = speed or {} 
        self.strength = strength or 0
        self.dexterity = dexterity or 0
        self.constitution = constitution or 0
        self.intelligence = intelligence or 0
        self.wisdom = wisdom or 0
        self.charisma = charisma or 0
        self.strength_save = strength_save or 0
        self.dexterity_save = dexterity_save or 0
        self.constitution_save = constitution_save or 0
        self.intelligence_save = intelligence_save or 0
        self.wisdom_save = wisdom_save or 0
        self.charisma_save = charisma_save or 0
        self.perception = perception or 0
        self.skills = skills or {}
        self.damage_vulnerabilities = damage_vulnerabilities or ""
        self.damage_resistances = damage_resistances or ""
        self.damage_immunities = damage_immunities or ""
        self.condition_immunities = condition_immunities or ""
        self.senses = senses or ""
        self.languages = languages or ""
        self.challenge_rating = challenge_rating or 0
        self.cr = cr or 0
        self.actions = actions or []
        self.reactions = reactions or []
        self.legendary_desc = legendary_desc or ""
        self.legendary_actions = legendary_actions or []
        self.special_abilities = special_abilities or []
        self.spell_list = spell_list or []
        self.img_main = img_main or ""
        self.document__slug = document__slug or ""
        self.document__title = document__title or ""
        self.document__license_url = document__license_url or ""

    def hurt(self, damage):
        self.hit_points -= damage
    
    def heal(self, healing):
        self.hit_points += healing

    