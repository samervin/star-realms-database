# Fields
NAME = 'name'
FLAVOR = 'flavor'
FACTION = 'faction'
TYPE = 'type'
SHIELD = 'shield'
COST = 'cost'
SET = 'set'
QUANTITY = 'quantity'

ABILITIES = 'abilities'
ALLY_ABILITIES = 'ally-abilities'
SCRAP_ABILITIES = 'scrap-abilities'

TRADE = 'trade'
COMBAT = 'combat'
AUTHORITY = 'authority'
DRAW = 'draw'
OPPONENT_DISCARD = 'opponent-discard'
TRADE_ROW_SCRAP = 'trade-row-scrap'
SCRAP = 'scrap'
OTHER_ABILITY = 'other-ability'

# Other ability fields
DESTROY_BASE = 'destroy-base'

# For cards that have 'or' text
OR = 'or'

# Faction values
MACHINE_CULT = 'Machine Cult'
STAR_EMPIRE = 'Star Empire'
BLOB = 'Blob'
TRADE_FEDERATION = 'Trade Federation'
UNALIGNED = 'Unaligned'

# Type values
SHIP = 'ship'
OUTPOST = 'outpost'
BASE = 'base'

# Scrap values
SCRAP_HAND = 'scrap-hand'
SCRAP_DISCARD = 'scrap-discard'
SCRAP_HAND_DISCARD = 'scrap-hand-discard'

# Set values
STAR_REALMS = 'Star Realms'
CRISIS_BASES_BATTLESHIPS = 'Crisis: Bases and Battleships'
CRISIS_EVENTS = 'Crisis: Events'
CRISIS_HEROES = 'Crisis: Heroes'
CRISIS_FLEETS_FORTRESSES = 'Crisis: Fleets and Fortresses'
GAMBIT_EXP = 'Gambit Expansion'
PROMOTIONAL = 'Promotional Set'
COLONY_WARS = 'Colony Wars'


class StarRealmsCards:
    BASE_SET = [
        {
            NAME: 'Scout',
            FACTION: UNALIGNED,
            TYPE: SHIP,
            SET: STAR_REALMS,
            QUANTITY: 16,
            TRADE: 1
        },
        {
            NAME: 'Viper',
            FACTION: UNALIGNED,
            TYPE: SHIP,
            SET: STAR_REALMS,
            QUANTITY: 4,
            COMBAT: 1
        },
        {
            NAME: 'Explorer',
            FACTION: UNALIGNED,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 10,
            ABILITIES: [{
                TRADE: 2
            }],
            SCRAP_ABILITIES: [{
                COMBAT: 2
            }]
        },
        {
            NAME: 'Trade Bot',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 1,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                TRADE: 1,
                SCRAP: SCRAP_HAND_DISCARD
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Missile Bot',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                COMBAT: 2,
                SCRAP: SCRAP_HAND_DISCARD
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Supply Bot',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                TRADE: 2,
                SCRAP: SCRAP_HAND_DISCARD
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Patrol Mech',
            FLAVOR: 'With the Blobs an ever present danger, '
                    'even the Cult\'s cargo carrying mechs bristle with firepower.',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                OR: {
                    TRADE: 3,
                    COMBAT: 5
                }
            },
            ALLY_ABILITIES: {
                SCRAP: SCRAP_HAND_DISCARD
            }
        },
        {
            NAME: 'Stealth Needle',
            FLAVOR: 'The Needle\'s ability to mimic other ships represents the pinnacle of Cult technology.',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OTHER_ABILITY: 'Copy another ship you\'ve played this turn. '
                               'Stealth Needle has that ship\'s faction in addition to Machine Cult.'
            }
        },
        {
            NAME: 'Battle Mech',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 4,
                SCRAP: SCRAP_HAND_DISCARD
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Missile Mech',
            FACTION: MACHINE_CULT,
            TYPE: SHIP,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 6,
                OTHER_ABILITY: DESTROY_BASE
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Battle Station',
            FLAVOR: 'A Battle Station fusion core can double as a devastating weapon... once.',
            FACTION: MACHINE_CULT,
            TYPE: OUTPOST,
            SHIELD: 5,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 2,
            SCRAP_ABILITIES: {
                COMBAT: 5
            }
        },
        {
            NAME: 'Mech World',
            FLAVOR: 'This man-made planet is a galactic center for open source tech.',
            FACTION: MACHINE_CULT,
            TYPE: OUTPOST,
            SHIELD: 6,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OTHER_ABILITY: 'Mech World counts as an ally for all factions.'
            }
        },
        {
            NAME: 'Junkyard',
            FLAVOR: 'The Machine Cult\'s first commandment: "Thou shalt not waste tech."',
            FACTION: MACHINE_CULT,
            TYPE: OUTPOST,
            SHIELD: 5,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                SCRAP: SCRAP_HAND_DISCARD
            }
        },
        {
            NAME: 'Machine Base',
            FLAVOR: 'This high-tech city is like a beehive: '
                    'it looks chaotic but vital work is being done efficiently at a frenetic pace.',
            FACTION: MACHINE_CULT,
            TYPE: OUTPOST,
            SHIELD: 6,
            COST: 7,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OTHER_ABILITY: 'Draw a card, then scrap a card from your hand.'
            }
        },
        {
            NAME: 'Brain World',
            FLAVOR: 'The Machine Cult built these supercomputing space stations to run every aspect of their society. '
                    'Now they worship them as gods.',
            FACTION: MACHINE_CULT,
            TYPE: OUTPOST,
            SHIELD: 6,
            COST: 8,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OTHER_ABILITY: 'Scrap up to two cards from your hand and/or discard pile. '
                               'Draw a card for each card scrapped this way.'
            }
        },
        {
            NAME: 'Imperial Fighter',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 1,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                COMBAT: 2,
                OPPONENT_DISCARD: 1
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Corvette',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                COMBAT: 1,
                DRAW: 1
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Survey Ship',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                TRADE: 1,
                DRAW: 1
            },
            SCRAP_ABILITIES: {
                OPPONENT_DISCARD: 1
            }
        },
        {
            NAME: 'Imperial Frigate',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                COMBAT: 4,
                OPPONENT_DISCARD: 1
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            },
            SCRAP_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Battlecruiser',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 5,
                DRAW: 1
            },
            ALLY_ABILITIES: {
                OPPONENT_DISCARD: 1
            },
            SCRAP_ABILITIES: {
                DRAW: 1,
                DESTROY_BASE: 1
            }
        },
        {
            NAME: 'Dreadnaught',
            FACTION: STAR_EMPIRE,
            TYPE: SHIP,
            COST: 7,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 7,
                DRAW: 1
            },
            SCRAP_ABILITIES: {
                COMBAT: 5
            }
        },
        {
            NAME: 'Space Station',
            FACTION: STAR_EMPIRE,
            TYPE: OUTPOST,
            SHIELD: 4,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                COMBAT: 2
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            },
            SCRAP_ABILITIES: {
                TRADE: 4
            }
        },
        {
            NAME: 'Recycling Station',
            FACTION: STAR_EMPIRE,
            TYPE: OUTPOST,
            SHIELD: 4,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                OR: {
                    TRADE: 1,
                    OTHER_ABILITY: 'Discard up to two cards, then draw that many cards.'
                }
            }
        },
        {
            NAME: 'War World',
            FACTION: STAR_EMPIRE,
            TYPE: OUTPOST,
            SHIELD: 4,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 3
            },
            ALLY_ABILITIES: {
                COMBAT: 4
            }
        },
        {
            NAME: 'Royal Redoubt',
            FACTION: STAR_EMPIRE,
            TYPE: OUTPOST,
            SHIELD: 6,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 3
            },
            ALLY_ABILITIES: {
                OPPONENT_DISCARD: 1
            }
        },
        {
            NAME: 'Fleet HQ',
            FLAVOR: 'When an Imperial Fleet goes into battle, '
                    'it\'s usually coordinated from afar by one of these mobile command centers.',
            FACTION: STAR_EMPIRE,
            TYPE: BASE,
            SHIELD: 8,
            COST: 8,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OTHER_ABILITY: 'All of your ships get +1 Combat.'
            }
        },
        {
            NAME: 'Blob Fighter',
            FLAVOR: 'Either kill it before it signals the hive or run. '
                    'There are other choices, but none you\'ll live through.',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 1,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                COMBAT: 3
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Trade Pod',
            FLAVOR: 'The loading and offloading process is efficient, but disgusting.',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                TRADE: 3
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Battle Pod',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                COMBAT: 4,
                TRADE_ROW_SCRAP: 1
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Ram',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                COMBAT: 5
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            },
            SCRAP_ABILITIES: {
                TRADE: 3
            }
        },
        {
            NAME: 'Blob Destroyer',
            FLAVOR: 'When this monstrous ship shows up on a colony\'s sensors, they know the end is near...',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                COMBAT: 6
            },
            ALLY_ABILITIES: {
                DESTROY_BASE: 1,
                TRADE_ROW_SCRAP: 1
            }
        },
        {
            NAME: 'Battle Blob',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 8
            },
            ALLY_ABILITIES: {
                DRAW: 1
            },
            SCRAP_ABILITIES: {
                COMBAT: 4
            }
        },
        {
            NAME: 'Blob Carrier',
            FLAVOR: '"Is that... a whale?" - HMS Defender, final transmission.',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 7
            },
            ALLY_ABILITIES: {
                OTHER_ABILITY: 'Acquire any ship without paying its cost and put it on top of your deck.'
            }
        },
        {
            NAME: 'Mothership',
            FACTION: BLOB,
            TYPE: SHIP,
            COST: 7,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 6,
                DRAW: 1
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Blob Wheel',
            FACTION: BLOB,
            TYPE: BASE,
            SHIELD: 5,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                COMBAT: 1
            },
            SCRAP_ABILITIES: {
                TRADE: 3
            }
        },
        {
            NAME: 'The Hive',
            FACTION: BLOB,
            TYPE: BASE,
            SHIELD: 5,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 3
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Blob World',
            FACTION: BLOB,
            TYPE: BASE,
            SHIELD: 7,
            COST: 8,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OR: {
                    COMBAT: 5,
                    OTHER_ABILITY: 'Draw a card for each Blob card that you\'ve played this turn.'
                }
            }
        },
        {
            NAME: 'Federation Shuttle',
            FLAVOR: '"Fast? This baby doesn\'t just haul cargo. She hauls..."',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 1,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                TRADE: 2
            },
            ALLY_ABILITIES: {
                AUTHORITY: 4
            }
        },
        {
            NAME: 'Cutter',
            FLAVOR: '"Built for cargo, armed for conflict. Versatility for an unpredictable universe."'
                    ' - Premier Aerospace Cargo Enterprises',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 2,
            SET: STAR_REALMS,
            QUANTITY: 3,
            ABILITIES: {
                AUTHORITY: 4,
                TRADE: 2
            },
            ALLY_ABILITIES: {
                COMBAT: 4
            }
        },
        {
            NAME: 'Embassy Yacht',
            FLAVOR: 'War should always be a last resort, it\'s bad for the bottom line.',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                AUTHORITY: 3,
                TRADE: 2,
                OTHER_ABILITY: 'If you have two or more bases in play, draw two cards.'
            }
        },
        {
            NAME: 'Freighter',
            FLAVOR: 'This class of mammoth cargo ships is one of the keys '
                    'to the Federation\'s vast trade-based wealth.',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                TRADE: 4
            },
            ALLY_ABILITIES: {
                # TODO: Should putting things on top of your deck be standardized?
                OTHER_ABILITY: 'You may put the next ship you acquire this turn on top of your deck.'
            }
        },
        {
            NAME: 'Trade Escort',
            FLAVOR: 'The heavily-armored Escort class was the Federation\'s first response to the Blob threat.',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                AUTHORITY: 4,
                COMBAT: 4
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        },
        {
            NAME: 'Flagship',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                COMBAT: 5,
                DRAW: 1
            },
            ALLY_ABILITIES: {
                AUTHORITY: 5
            }
        },
        {
            NAME: 'Command Ship',
            FACTION: TRADE_FEDERATION,
            TYPE: SHIP,
            COST: 8,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                AUTHORITY: 4,
                COMBAT: 5,
                DRAW: 2
            },
            ALLY_ABILITIES: {
                OTHER_ABILITY: DESTROY_BASE
            }
        },
        {
            NAME: 'Trading Post',
            FACTION: TRADE_FEDERATION,
            TYPE: OUTPOST,
            SHIELD: 4,
            COST: 3,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                OR: {
                    AUTHORITY: 1,
                    TRADE: 1
                }
            },
            SCRAP_ABILITIES: {
                COMBAT: 3
            }
        },
        {
            NAME: 'Barter World',
            FACTION: TRADE_FEDERATION,
            TYPE: BASE,
            SHIELD: 4,
            COST: 4,
            SET: STAR_REALMS,
            QUANTITY: 2,
            ABILITIES: {
                OR: {
                    AUTHORITY: 2,
                    TRADE: 2
                }
            },
            SCRAP_ABILITIES: {
                COMBAT: 5
            }
        },
        {
            NAME: 'Defense Center',
            FACTION: TRADE_FEDERATION,
            TYPE: OUTPOST,
            SHIELD: 5,
            COST: 5,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                OR: {
                    AUTHORITY: 3,
                    COMBAT: 2
                }
            },
            ALLY_ABILITIES: {
                COMBAT: 2
            }
        },
        {
            NAME: 'Port of Call',
            FACTION: TRADE_FEDERATION,
            TYPE: OUTPOST,
            SHIELD: 6,
            COST: 6,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                TRADE: 3
            },
            SCRAP_ABILITIES: {
                DRAW: 1,
                OTHER_ABILITY: DESTROY_BASE
            }
        },
        {
            NAME: 'Central Office',
            FACTION: TRADE_FEDERATION,
            TYPE: BASE,
            SHIELD: 6,
            COST: 7,
            SET: STAR_REALMS,
            QUANTITY: 1,
            ABILITIES: {
                TRADE: 2,
                OTHER_ABILITY: 'You may put the next ship you acquire this turn on top of your deck.'
            },
            ALLY_ABILITIES: {
                DRAW: 1
            }
        }
    ]
