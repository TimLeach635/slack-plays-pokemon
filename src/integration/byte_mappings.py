STATUS_BIT_FIELD = {
    0x4: "Asleep",
    0x8: "Poisoned",
    0x10: "Burned",
    0x20: "Frozen",
    0x40: "Paralyzed",
}

TYPE_MAP = {
    0x00: "Normal",
    0x01: "Fighting",
    0x02: "Flying",
    0x03: "Poison",
    0x04: "Ground",
    0x05: "Rock",
    0x07: "Bug",
    0x08: "Ghost",
    0x14: "Fire",
    0x15: "Water",
    0x16: "Grass",
    0x17: "Electric",
    0x18: "Psychic",
    0x19: "Ice",
    0x1A: "Dragon",
}


GEN_1_SPECIES = [
    "",
    "Rhydon",
    "Kangaskhan",
    "Nidoran♂",
    "Clefairy",
    "Spearow",
    "Voltorb",
    "Nidoking",
    "Slowbro",
    "Ivysaur",
    "Exeggutor",
    "Lickitung",
    "Exeggcute",
    "Grimer",
    "Gengar",
    "Nidoran♀",
    "Nidoqueen",
    "Cubone",
    "Rhyhorn",
    "Lapras",
    "Arcanine",
    "Mew",
    "Gyarados",
    "Shellder",
    "Tentacool",
    "Gastly",
    "Scyther",
    "Staryu",
    "Blastoise",
    "Pinsir",
    "Tangela",
    "MissingNo.",
    "MissingNo.",
    "Growlithe",
    "Onix",
    "Fearow",
    "Pidgey",
    "Slowpoke",
    "Kadabra",
    "Graveler",
    "Chansey",
    "Machoke",
    "Mr. Mime",
    "Hitmonlee",
    "Hitmonchan",
    "Arbok",
    "Parasect",
    "Psyduck",
    "Drowzee",
    "Golem",
    "MissingNo.",
    "Magmar",
    "MissingNo.",
    "Electabuzz",
    "Magneton",
    "Koffing",
    "MissingNo.",
    "Mankey",
    "Seel",
    "Diglett",
    "Tauros",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "Farfetch'd",
    "Venonat",
    "Dragonite",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "Doduo",
    "Poliwag",
    "Jynx",
    "Moltres",
    "Articuno",
    "Zapdos",
    "Ditto",
    "Meowth",
    "Krabby",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "Vulpix",
    "Ninetales",
    "Pikachu",
    "Raichu",
    "MissingNo.",
    "MissingNo.",
    "Dratini",
    "Dragonair",
    "Kabuto",
    "Kabutops",
    "Horsea",
    "Seadra",
    "MissingNo.",
    "MissingNo.",
    "Sandshrew",
    "Sandslash",
    "Omanyte",
    "Omastar",
    "Jigglypuff",
    "Wigglytuff",
    "Eevee",
    "Flareon",
    "Jolteon",
    "Vaporeon",
    "Machop",
    "Zubat",
    "Ekans",
    "Paras",
    "Poliwhirl",
    "Poliwrath",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "MissingNo.",
    "Dodrio",
    "Primeape",
    "Dugtrio",
    "Venomoth",
    "Dewgong",
    "MissingNo.",
    "MissingNo.",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Machamp",
    "MissingNo.",
    "Golduck",
    "Hypno",
    "Golbat",
    "Mewtwo",
    "Snorlax",
    "Magikarp",
    "MissingNo.",
    "MissingNo.",
    "Muk",
    "MissingNo.",
    "Kingler",
    "Cloyster",
    "MissingNo.",
    "Electrode",
    "Clefable",
    "Weezing",
    "Persian",
    "Marowak",
    "MissingNo.",
    "Haunter",
    "Abra",
    "Alakazam",
    "Pidgeotto",
    "Pidgeot",
    "Starmie",
    "Bulbasaur",
    "Venusaur",
    "Tentacruel",
    "MissingNo.",
    "Goldeen",
    "Seaking",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "Ponyta",
    "Rapidash",
    "Rattata",
    "Raticate",
    "Nidorino",
    "Nidorina",
    "Geodude",
    "Porygon",
    "Aerodactyl",
    "MissingNo.",
    "Magnemite",
    "MissingNo.",
    "MissingNo.",
    "Charmander",
    "Squirtle",
    "Charmeleon",
    "Wartortle",
    "Charizard",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "MissingNo.",
    "Oddish",
    "Gloom",
    "Vileplume",
    "Bellsprout",
    "Weepinbell",
    "Victreebel",
]

GEN_1_NORMAL_ITEMS = [
    "",
    "Master Ball",
    "Ultra Ball",
    "Great Ball",
    "Poké Ball",
    "Town Map",
    "Bicycle",
    "?????",
    "Safari Ball",
    "Pokédex",
    "Moon Stone",
    "Antidote",
    "Burn Heal",
    "Ice Heal",
    "Awakening",
    "Parlyz Heal",
    "Full Restore",
    "Max Potion",
    "Hyper Potion",
    "Super Potion",
    "Potion",
    "BoulderBadge",
    "CascadeBadge",
    "ThunderBadge",
    "RainbowBadge",
    "SoulBadge",
    "MarshBadge",
    "VolcanoBadge",
    "EarthBadge",
    "Escape Rope",
    "Repel",
    "Old Amber",
    "Fire Stone",
    "Thunderstone",
    "Water Stone",
    "HP Up",
    "Protein",
    "Iron",
    "Carbos",
    "Calcium",
    "Rare Candy",
    "Dome Fossil",
    "Helix Fossil",
    "Secret Key",
    "?????",
    "Bike Voucher",
    "X Accuracy",
    "Leaf Stone",
    "Card Key",
    "Nugget",
    "PP Up*",
    "Poké Doll",
    "Full Heal",
    "Revive",
    "Max Revive",
    "Guard Spec.",
    "Super Repel",
    "Max Repel",
    "Dire Hit",
    "Coin",
    "Fresh Water",
    "Soda Pop",
    "Lemonade",
    "S.S. Ticket",
    "Gold Teeth",
    "X Attack",
    "X Defend",
    "X Speed",
    "X Special",
    "Coin Case",
    "Oak's Parcel",
    "Itemfinder",
    "Silph Scope",
    "Poké Flute",
    "Lift Key",
    "Exp. All",
    "Old Rod",
    "Good Rod",
    "Super Rod",
    "PP Up",
    "Ether",
    "Max Ether",
    "Elixer",
    "Max Elixer",
]

GEN_1_TMS = [
    "HM01",
    "HM02",
    "HM03",
    "HM04",
    "HM05",
    "TM01",
    "TM02",
    "TM03",
    "TM04",
    "TM05",
    "TM06",
    "TM07",
    "TM08",
    "TM09",
    "TM10",
    "TM11",
    "TM12",
    "TM13",
    "TM14",
    "TM15",
    "TM16",
    "TM17",
    "TM18",
    "TM19",
    "TM20",
    "TM21",
    "TM22",
    "TM23",
    "TM24",
    "TM25",
    "TM26",
    "TM27",
    "TM28",
    "TM29",
    "TM30",
    "TM31",
    "TM32",
    "TM33",
    "TM34",
    "TM35",
    "TM36",
    "TM37",
    "TM38",
    "TM39",
    "TM40",
    "TM41",
    "TM42",
    "TM43",
    "TM44",
    "TM45",
    "TM46",
    "TM47",
    "TM48",
    "TM49",
    "TM50",
    "TM51",
    "TM52",
    "TM53",
    "TM54",
    "TM55",
]

# Create the offset between TM's and Non-TM's
GEN_1_ITEMS = GEN_1_NORMAL_ITEMS + [None] * 112 + GEN_1_TMS

GEN_1_MOVES = [
    "",  # Index 0 is no move learnt
    "Pound",
    "Karate Chop",
    "Double Slap",
    "Comet Punch",
    "Mega Punch",
    "Pay Day",
    "Fire Punch",
    "Ice Punch",
    "Thunder Punch",
    "Scratch",
    "Vise Grip",
    "Guillotine",
    "Razor Wind",
    "Swords Dance",
    "Cut",
    "Gust",
    "Wing Attack",
    "Whirlwind",
    "Fly",
    "Bind",
    "Slam",
    "Vine Whip",
    "Stomp",
    "Double Kick",
    "Mega Kick",
    "Jump Kick",
    "Rolling Kick",
    "Sand Attack",
    "Headbutt",
    "Horn Attack",
    "Fury Attack",
    "Horn Drill",
    "Tackle",
    "Body Slam",
    "Wrap",
    "Take Down",
    "Thrash",
    "Double-Edge",
    "Tail Whip",
    "Poison Sting",
    "Twineedle",
    "Pin Missile",
    "Leer",
    "Bite",
    "Growl",
    "Roar",
    "Sing",
    "Supersonic",
    "Sonic Boom",
    "Disable",
    "Acid",
    "Ember",
    "Flamethrower",
    "Mist",
    "Water Gun",
    "Hydro Pump",
    "Surf",
    "Ice Beam",
    "Blizzard",
    "Psybeam",
    "Bubble Beam",
    "Aurora Beam",
    "Hyper Beam",
    "Peck",
    "Drill Peck",
    "Submission",
    "Low Kick",
    "Counter",
    "Seismic Toss",
    "Strength",
    "Absorb",
    "Mega Drain",
    "Leech Seed",
    "Growth",
    "Razor Leaf",
    "Solar Beam",
    "Poison Powder",
    "Stun Spore",
    "Sleep Powder",
    "Petal Dance",
    "String Shot",
    "Dragon Rage",
    "Fire Spin",
    "Thunder Shock",
    "Thunderbolt",
    "Thunder Wave",
    "Thunder",
    "Rock Throw",
    "Earthquake",
    "Fissure",
    "Dig",
    "Toxic",
    "Confusion",
    "Psychic",
    "Hypnosis",
    "Meditate",
    "Agility",
    "Quick Attack",
    "Rage",
    "Teleport",
    "Night Shade",
    "Mimic",
    "Screech",
    "Double Team",
    "Recover",
    "Harden",
    "Minimize",
    "Smokescreen",
    "Confuse Ray",
    "Withdraw",
    "Defense Curl",
    "Barrier",
    "Light Screen",
    "Haze",
    "Reflect",
    "Focus Energy",
    "Bide",
    "Metronome",
    "Mirror Move",
    "Self-Destruct",
    "Egg Bomb",
    "Lick",
    "Smog",
    "Sludge",
    "Bone Club",
    "Fire Blast",
    "Waterfall",
    "Clamp",
    "Swift",
    "Skull Bash",
    "Spike Cannon",
    "Constrict",
    "Amnesia",
    "Kinesis",
    "Soft-Boiled",
    "High Jump Kick",
    "Glare",
    "Dream Eater",
    "Poison Gas",
    "Barrage",
    "Leech Life",
    "Lovely Kiss",
    "Sky Attack",
    "Transform",
    "Bubble",
    "Dizzy Punch",
    "Spore",
    "Flash",
    "Psywave",
    "Splash",
    "Acid Armor",
    "Crabhammer",
    "Explosion",
    "Fury Swipes",
    "Bonemerang",
    "Rest",
    "Rock Slide",
    "Hyper Fang",
    "Sharpen",
    "Conversion",
    "Tri Attack",
    "Super Fang",
    "Slash",
    "Substitute",
    "Struggle",
]

EXPERIENCE_TYPES = {
    "Bulbasaur": "Medium Slow",
    "Ivysaur": "Medium Slow",
    "Venusaur": "Medium Slow",
    "Charmander": "Medium Slow",
    "Charmeleon": "Medium Slow",
    "Charizard": "Medium Slow",
    "Squirtle": "Medium Slow",
    "Wartortle": "Medium Slow",
    "Blastoise": "Medium Slow",
    "Caterpie": "Medium Fast",
    "Metapod": "Medium Fast",
    "Butterfree": "Medium Fast",
    "Weedle": "Medium Fast",
    "Kakuna": "Medium Fast",
    "Beedrill": "Medium Fast",
    "Pidgey": "Medium Slow",
    "Pidgeotto": "Medium Slow",
    "Pidgeot": "Medium Slow",
    "Rattata": "Medium Fast",
    "Raticate": "Medium Fast",
    "Spearow": "Medium Fast",
    "Fearow": "Medium Fast",
    "Ekans": "Medium Fast",
    "Arbok": "Medium Fast",
    "Pikachu": "Medium Fast",
    "Raichu": "Medium Fast",
    "Sandshrew": "Medium Fast",
    "Sandslash": "Medium Fast",
    "Nidoran♀": "Medium Slow",
    "Nidorina": "Medium Slow",
    "Nidoqueen": "Medium Slow",
    "Nidoran♂": "Medium Slow",
    "Nidorino": "Medium Slow",
    "Nidoking": "Medium Slow",
    "Clefairy": "Fast",
    "Clefable": "Fast",
    "Vulpix": "Medium Fast",
    "Ninetales": "Medium Fast",
    "Jigglypuff": "Fast",
    "Wigglytuff": "Fast",
    "Zubat": "Medium Fast",
    "Golbat": "Medium Fast",
    "Oddish": "Medium Slow",
    "Gloom": "Medium Slow",
    "Vileplume": "Medium Slow",
    "Paras": "Medium Fast",
    "Parasect": "Medium Fast",
    "Venonat": "Medium Fast",
    "Venomoth": "Medium Fast",
    "Diglett": "Medium Fast",
    "Dugtrio": "Medium Fast",
    "Meowth": "Medium Fast",
    "Persian": "Medium Fast",
    "Psyduck": "Medium Fast",
    "Golduck": "Medium Fast",
    "Mankey": "Medium Fast",
    "Primeape": "Medium Fast",
    "Growlithe": "Slow",
    "Arcanine": "Slow",
    "Poliwag": "Medium Slow",
    "Poliwhirl": "Medium Slow",
    "Poliwrath": "Medium Slow",
    "Abra": "Medium Slow",
    "Kadabra": "Medium Slow",
    "Alakazam": "Medium Slow",
    "Machop": "Medium Slow",
    "Machoke": "Medium Slow",
    "Machamp": "Medium Slow",
    "Bellsprout": "Medium Slow",
    "Weepinbell": "Medium Slow",
    "Victreebel": "Medium Slow",
    "Tentacool": "Slow",
    "Tentacruel": "Slow",
    "Geodude": "Medium Slow",
    "Graveler": "Medium Slow",
    "Golem": "Medium Slow",
    "Ponyta": "Medium Fast",
    "Rapidash": "Medium Fast",
    "Slowpoke": "Medium Fast",
    "Slowbro": "Medium Fast",
    "Magnemite": "Medium Fast",
    "Magneton": "Medium Fast",
    "Farfetch'd": "Medium Fast",
    "Doduo": "Medium Fast",
    "Dodrio": "Medium Fast",
    "Seel": "Medium Fast",
    "Dewgong": "Medium Fast",
    "Grimer": "Medium Fast",
    "Muk": "Medium Fast",
    "Shellder": "Slow",
    "Cloyster": "Slow",
    "Gastly": "Medium Slow",
    "Haunter": "Medium Slow",
    "Gengar": "Medium Slow",
    "Onix": "Medium Fast",
    "Drowzee": "Medium Fast",
    "Hypno": "Medium Fast",
    "Krabby": "Medium Fast",
    "Kingler": "Medium Fast",
    "Voltorb": "Medium Fast",
    "Electrode": "Medium Fast",
    "Exeggcute": "Slow",
    "Exeggutor": "Slow",
    "Cubone": "Medium Fast",
    "Marowak": "Medium Fast",
    "Hitmonlee": "Medium Fast",
    "Hitmonchan": "Medium Fast",
    "Lickitung": "Medium Fast",
    "Koffing": "Medium Fast",
    "Weezing": "Medium Fast",
    "Rhyhorn": "Slow",
    "Rhydon": "Slow",
    "Chansey": "Fast",
    "Tangela": "Medium Fast",
    "Kangaskhan": "Medium Fast",
    "Horsea": "Medium Fast",
    "Seadra": "Medium Fast",
    "Goldeen": "Medium Fast",
    "Seaking": "Medium Fast",
    "Staryu": "Slow",
    "Starmie": "Slow",
    "Mr. Mime": "Medium Fast",
    "Scyther": "Medium Fast",
    "Jynx": "Medium Fast",
    "Electabuzz": "Medium Fast",
    "Magmar": "Medium Fast",
    "Pinsir": "Slow",
    "Tauros": "Slow",
    "Magikarp": "Slow",
    "Gyarados": "Slow",
    "Lapras": "Slow",
    "Ditto": "Medium Fast",
    "Eevee": "Medium Fast",
    "Vaporeon": "Medium Fast",
    "Jolteon": "Medium Fast",
    "Flareon": "Medium Fast",
    "Porygon": "Medium Fast",
    "Omanyte": "Medium Fast",
    "Omastar": "Medium Fast",
    "Kabuto": "Medium Fast",
    "Kabutops": "Medium Fast",
    "Aerodactyl": "Slow",
    "Snorlax": "Slow",
    "Articuno": "Slow",
    "Zapdos": "Slow",
    "Moltres": "Slow",
    "Dratini": "Slow",
    "Dragonair": "Slow",
    "Dragonite": "Slow",
    "Mewtwo": "Slow",
    "Mew": "Medium Slow",
}

MOVE_BASE_PP = {
    "": 0,
    "Absorb": 25,
    "Acid": 30,
    "Acid Armor": 20,
    "Agility": 30,
    "Amnesia": 20,
    "Aurora Beam": 20,
    "Barrage": 20,
    "Barrier": 20,
    "Bide": 10,
    "Bind": 20,
    "Bite": 25,
    "Blizzard": 5,
    "Body Slam": 15,
    "Bone Club": 20,
    "Bonemerang": 10,
    "Bubble": 30,
    "Bubble Beam": 20,
    "Clamp": 15,
    "Comet Punch": 15,
    "Confuse Ray": 10,
    "Confusion": 25,
    "Constrict": 35,
    "Conversion": 30,
    "Counter": 20,
    "Crabhammer": 10,
    "Cut": 30,
    "Defense Curl": 40,
    "Dig": 10,
    "Disable": 20,
    "Dizzy Punch": 10,
    "Double Kick": 30,
    "Double Slap": 10,
    "Double Team": 15,
    "Double-Edge": 15,
    "Dragon Rage": 10,
    "Dream Eater": 15,
    "Drill Peck": 20,
    "Earthquake": 10,
    "Egg Bomb": 10,
    "Ember": 25,
    "Explosion": 5,
    "Fire Blast": 5,
    "Fire Punch": 15,
    "Fire Spin": 15,
    "Fissure": 5,
    "Flamethrower": 15,
    "Flash": 20,
    "Fly": 15,
    "Focus Energy": 30,
    "Fury Attack": 20,
    "Fury Swipes": 15,
    "Glare": 30,
    "Growl": 40,
    "Growth": 20,
    "Guillotine": 5,
    "Gust": 35,
    "Harden": 30,
    "Haze": 30,
    "Headbutt": 15,
    "High Jump Kick": 10,
    "Horn Attack": 25,
    "Horn Drill": 5,
    "Hydro Pump": 5,
    "Hyper Beam": 5,
    "Hyper Fang": 15,
    "Hypnosis": 20,
    "Ice Beam": 10,
    "Ice Punch": 15,
    "Jump Kick": 10,
    "Karate Chop": 25,
    "Kinesis": 15,
    "Leech Life": 10,
    "Leech Seed": 10,
    "Leer": 30,
    "Lick": 30,
    "Light Screen": 30,
    "Lovely Kiss": 10,
    "Low Kick": 20,
    "Meditate": 40,
    "Mega Drain": 15,
    "Mega Kick": 5,
    "Mega Punch": 20,
    "Metronome": 10,
    "Mimic": 10,
    "Minimize": 10,
    "Mirror Move": 20,
    "Mist": 30,
    "Night Shade": 15,
    "Pay Day": 20,
    "Peck": 35,
    "Petal Dance": 10,
    "Pin Missile": 20,
    "Poison Gas": 40,
    "Poison Powder": 35,
    "Poison Sting": 35,
    "Pound": 35,
    "Psybeam": 20,
    "Psychic": 10,
    "Psywave": 15,
    "Quick Attack": 30,
    "Rage": 20,
    "Razor Leaf": 25,
    "Razor Wind": 10,
    "Recover": 5,
    "Reflect": 20,
    "Rest": 5,
    "Roar": 20,
    "Rock Slide": 10,
    "Rock Throw": 15,
    "Rolling Kick": 15,
    "Sand Attack": 15,
    "Scratch": 35,
    "Screech": 40,
    "Seismic Toss": 20,
    "Self-Destruct": 5,
    "Sharpen": 30,
    "Sing": 15,
    "Skull Bash": 10,
    "Sky Attack": 5,
    "Slam": 20,
    "Slash": 20,
    "Sleep Powder": 15,
    "Sludge": 20,
    "Smog": 20,
    "Smokescreen": 20,
    "Soft-Boiled": 5,
    "Solar Beam": 10,
    "Sonic Boom": 20,
    "Spike Cannon": 15,
    "Splash": 40,
    "Spore": 15,
    "Stomp": 20,
    "Strength": 15,
    "String Shot": 40,
    "Struggle": 1,
    "Stun Spore": 30,
    "Submission": 20,
    "Substitute": 10,
    "Super Fang": 10,
    "Supersonic": 20,
    "Surf": 15,
    "Swift": 20,
    "Swords Dance": 20,
    "Tackle": 35,
    "Tail Whip": 30,
    "Take Down": 20,
    "Teleport": 20,
    "Thrash": 10,
    "Thunder": 10,
    "Thunder Punch": 15,
    "Thunder Shock": 30,
    "Thunder Wave": 20,
    "Thunderbolt": 15,
    "Toxic": 10,
    "Transform": 10,
    "Tri Attack": 10,
    "Twineedle": 20,
    "Vine Whip": 25,
    "Vise Grip": 30,
    "Water Gun": 25,
    "Waterfall": 15,
    "Whirlwind": 20,
    "Wing Attack": 35,
    "Withdraw": 40,
    "Wrap": 20,
}

CHARACTER_ENCODING = {
    96: "A",
    97: "B",
    98: "C",
    99: "D",
    100: "E",
    101: "F",
    102: "G",
    103: "H",
    104: "I",
    105: "V",
    106: "S",
    107: "L",
    108: "M",
    109: ":",
    110: "ぃ",
    111: "ぅ",
    112: "‘",
    113: "’",
    114: "“",
    115: "”",
    116: "・",
    117: "…",
    118: "ぁ",
    119: "ぇ",
    120: "ぉ",
    121: "╔",
    122: "═",
    123: "╗",
    124: "║",
    125: "╚",
    126: "╝",
    127: "␠",
    128: "A",
    129: "B",
    130: "C",
    131: "D",
    132: "E",
    133: "F",
    134: "G",
    135: "H",
    136: "I",
    137: "J",
    138: "K",
    139: "L",
    140: "M",
    141: "N",
    142: "O",
    143: "P",
    144: "Q",
    145: "R",
    146: "S",
    147: "T",
    148: "U",
    149: "V",
    150: "W",
    151: "X",
    152: "Y",
    153: "Z",
    154: "(",
    155: ")",
    156: ":",
    157: ";",
    158: "[",
    159: "]",
    160: "a",
    161: "b",
    162: "c",
    163: "d",
    164: "e",
    165: "f",
    166: "g",
    167: "h",
    168: "i",
    169: "j",
    170: "k",
    171: "l",
    172: "m",
    173: "n",
    174: "o",
    175: "p",
    176: "q",
    177: "r",
    178: "s",
    179: "t",
    180: "u",
    181: "v",
    182: "w",
    183: "x",
    184: "y",
    185: "z",
    186: "é",
    187: "'d",
    188: "'l",
    189: "'s",
    190: "'t",
    191: "'v",
    224: "'",
    225: "Pk",
    226: "Mn",
    227: "-",
    228: "'r",
    229: "'m",
    230: "?",
    231: "!",
    232: ".",
    233: "ァ",
    234: "ゥ",
    236: "▷",
    237: "▶",
    238: "▼",
    239: "♂",
    240: "₽",
    241: "×",
    242: ".",
    243: "/",
    244: ",",
    245: "♀",
    246: "0",
    247: "1",
    248: "2",
    249: "3",
    250: "4",
    251: "5",
    252: "6",
    253: "7",
    254: "8",
    255: "9",
}
