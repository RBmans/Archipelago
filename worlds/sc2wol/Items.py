from BaseClasses import Item, ItemClassification, MultiWorld
import typing

from .Options import get_option_value
from .MissionTables import SC2Mission, SC2Race, SC2Campaign, campaign_mission_table


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    type: typing.Optional[str]
    number: typing.Optional[int]
    race: SC2Race
    classification: ItemClassification = ItemClassification.useful
    quantity: int = 1
    parent_item: str = None
    origin: typing.Set[str] = {"wol"}


class StarcraftWoLItem(Item):
    game: str = "Starcraft 2 Wings of Liberty"


def get_full_item_list():
    return item_table


SC2WOL_ITEM_ID_OFFSET = 1000
SC2HOTS_ITEM_ID_OFFSET = SC2WOL_ITEM_ID_OFFSET + 900

item_table = {
    # WoL
    "Marine": ItemData(0 + SC2WOL_ITEM_ID_OFFSET, "Unit", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Medic": ItemData(1 + SC2WOL_ITEM_ID_OFFSET, "Unit", 1, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Firebat": ItemData(2 + SC2WOL_ITEM_ID_OFFSET, "Unit", 2, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Marauder": ItemData(3 + SC2WOL_ITEM_ID_OFFSET, "Unit", 3, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Reaper": ItemData(4 + SC2WOL_ITEM_ID_OFFSET, "Unit", 4, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Hellion": ItemData(5 + SC2WOL_ITEM_ID_OFFSET, "Unit", 5, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Vulture": ItemData(6 + SC2WOL_ITEM_ID_OFFSET, "Unit", 6, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Goliath": ItemData(7 + SC2WOL_ITEM_ID_OFFSET, "Unit", 7, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Diamondback": ItemData(8 + SC2WOL_ITEM_ID_OFFSET, "Unit", 8, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Siege Tank": ItemData(9 + SC2WOL_ITEM_ID_OFFSET, "Unit", 9, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Medivac": ItemData(10 + SC2WOL_ITEM_ID_OFFSET, "Unit", 10, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Wraith": ItemData(11 + SC2WOL_ITEM_ID_OFFSET, "Unit", 11, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Viking": ItemData(12 + SC2WOL_ITEM_ID_OFFSET, "Unit", 12, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Banshee": ItemData(13 + SC2WOL_ITEM_ID_OFFSET, "Unit", 13, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Battlecruiser": ItemData(14 + SC2WOL_ITEM_ID_OFFSET, "Unit", 14, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Ghost": ItemData(15 + SC2WOL_ITEM_ID_OFFSET, "Unit", 15, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Spectre": ItemData(16 + SC2WOL_ITEM_ID_OFFSET, "Unit", 16, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Thor": ItemData(17 + SC2WOL_ITEM_ID_OFFSET, "Unit", 17, SC2Race.TERRAN, classification=ItemClassification.progression),
    # EE units
    "Liberator": ItemData(18 + SC2WOL_ITEM_ID_OFFSET, "Unit", 18, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"nco", "ext"}),
    "Valkyrie": ItemData(19 + SC2WOL_ITEM_ID_OFFSET, "Unit", 19, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"bw"}),
    "Widow Mine": ItemData(20 + SC2WOL_ITEM_ID_OFFSET, "Unit", 20, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"ext"}),
    "Cyclone": ItemData(21 + SC2WOL_ITEM_ID_OFFSET, "Unit", 21, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"ext"}),

    # Some other items are moved to Upgrade group because of the way how the bot message is parsed
    "Progressive Terran Infantry Weapon": ItemData(100 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Infantry Armor": ItemData(102 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Vehicle Weapon": ItemData(103 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Vehicle Armor": ItemData(104 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Ship Weapon": ItemData(105 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Ship Armor": ItemData(106 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 10, SC2Race.TERRAN, quantity=3),
    # Upgrade bundle 'number' values are used as indices to get affected 'number's
    "Progressive Terran Weapon Upgrade": ItemData(107 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Armor Upgrade": ItemData(108 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 1, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Infantry Upgrade": ItemData(109 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Vehicle Upgrade": ItemData(110 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 3, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Ship Upgrade": ItemData(111 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.TERRAN, quantity=3),
    "Progressive Terran Weapon/Armor Upgrade": ItemData(112 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 5, SC2Race.TERRAN, quantity=3),

    "Projectile Accelerator (Bunker)": ItemData(200 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 0, SC2Race.TERRAN, parent_item="Bunker"),
    "Neosteel Bunker (Bunker)": ItemData(201 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 1, SC2Race.TERRAN, parent_item="Bunker"),
    "Titanium Housing (Missile Turret)": ItemData(202 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Missile Turret"),
    "Hellstorm Batteries (Missile Turret)": ItemData(203 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 3, SC2Race.TERRAN, parent_item="Missile Turret"),
    "Advanced Construction (SCV)": ItemData(204 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 4, SC2Race.TERRAN),
    "Dual-Fusion Welders (SCV)": ItemData(205 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 5, SC2Race.TERRAN),
    "Fire-Suppression System (Building)": ItemData(206 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 6, SC2Race.TERRAN),
    "Orbital Command (Building)": ItemData(207 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 7, SC2Race.TERRAN),
    "Progressive Stimpack (Marine)": ItemData(208 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 0, SC2Race.TERRAN, parent_item="Marine", quantity=2),
    "Combat Shield (Marine)": ItemData(209 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 9, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Marine"),
    "Advanced Medic Facilities (Medic)": ItemData(210 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 10, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic"),
    "Stabilizer Medpacks (Medic)": ItemData(211 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 11, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Medic"),
    "Incinerator Gauntlets (Firebat)": ItemData(212 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Firebat"),
    "Juggernaut Plating (Firebat)": ItemData(213 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 13, SC2Race.TERRAN, parent_item="Firebat"),
    "Concussive Shells (Marauder)": ItemData(214 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 14, SC2Race.TERRAN, parent_item="Marauder"),
    "Kinetic Foam (Marauder)": ItemData(215 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 15, SC2Race.TERRAN, parent_item="Marauder"),
    "U-238 Rounds (Reaper)": ItemData(216 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 16, SC2Race.TERRAN, parent_item="Reaper"),
    "G-4 Clusterbomb (Reaper)": ItemData(217 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 17, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Reaper"),
    # Items from EE
    "Mag-Field Accelerators (Cyclone)": ItemData(218 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 18, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    "Mag-Field Launchers (Cyclone)": ItemData(219 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 19, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    # Items from new mod
    "Laser Targeting System (Marine)": ItemData(220 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 8, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marine", origin={"nco"}), # Freed slot from Stimpack
    "Magrail Munitions (Marine)": ItemData(221 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 20, SC2Race.TERRAN, parent_item="Marine", origin={"nco"}),
    "Optimized Logistics (Marine)": ItemData(222 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 21, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marine", origin={"nco"}),
    "Restoration (Medic)": ItemData(223 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    "Optical Flare (Medic)": ItemData(224 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 23, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    "Optimized Logistics (Medic)": ItemData(225 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    "Progressive Stimpack (Firebat)": ItemData(226 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 6, SC2Race.TERRAN, parent_item="Firebat", quantity=2, origin={"bw"}),
    "Optimized Logistics (Firebat)": ItemData(227 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 25, SC2Race.TERRAN, parent_item="Firebat", origin={"bw"}),
    "Progressive Stimpack (Marauder)": ItemData(228 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 8, SC2Race.TERRAN, parent_item="Marauder", quantity=2, origin={"nco"}),
    "Laser Targeting System (Marauder)": ItemData(229 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 26, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),
    "Magrail Munitions (Marauder)": ItemData(230 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 27, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),
    "Internal Tech Module (Marauder)": ItemData(231 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 28, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),

    # Items from new mod
    "Progressive Stimpack (Reaper)": ItemData(250 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 10, SC2Race.TERRAN, parent_item="Reaper", quantity=2, origin={"nco"}),
    "Laser Targeting System (Reaper)": ItemData(251 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"nco"}),
    "Advanced Cloaking Field (Reaper)": ItemData(252 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 1, SC2Race.TERRAN, parent_item="Reaper", origin={"nco"}),
    "Spider Mines (Reaper)": ItemData(253 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"nco"}),
    "Combat Drugs (Reaper)": ItemData(254 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 3, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"ext"}),
    "Hellbat Aspect (Hellion)": ItemData(255 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 4, SC2Race.TERRAN, parent_item="Hellion", origin={"nco"}),
    "Smart Servos (Hellion)": ItemData(256 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 5, SC2Race.TERRAN, parent_item="Hellion", origin={"nco"}),
    "Optimized Logistics (Hellion)": ItemData(257 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion", origin={"nco"}),
    "Jump Jets (Hellion)": ItemData(258 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion", origin={"nco"}),
    "Progressive Stimpack (Hellion)": ItemData(259 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 12, SC2Race.TERRAN, parent_item="Hellion", quantity=2, origin={"nco"}),
    "Ion Thrusters (Vulture)": ItemData(260 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 8, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Vulture", origin={"bw"}),
    "Auto Launchers (Vulture)": ItemData(261 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 9, SC2Race.TERRAN, parent_item="Vulture", origin={"bw"}),
    "High Explosive Munition (Spider Mine)": ItemData(262 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 10, SC2Race.TERRAN, origin={"bw"}),
    "Jump Jets (Goliath)": ItemData(263 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 11, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Goliath", origin={"nco"}),
    "Optimized Logistics (Goliath)": ItemData(264 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Goliath", origin={"nco"}),
    "Hyperfluxor (Diamondback)": ItemData(265 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 13, SC2Race.TERRAN, parent_item="Diamondback", origin={"ext"}),
    "Burst Capacitors (Diamondback)": ItemData(266 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 14, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback", origin={"ext"}),
    "Optimized Logistics (Diamondback)": ItemData(267 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 15, SC2Race.TERRAN, parent_item="Diamondback", origin={"ext"}),
    "Jump Jets (Siege Tank)": ItemData(268 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 16, SC2Race.TERRAN, parent_item="Siege Tank", origin={"nco"}),
    "Spider Mines (Siege Tank)": ItemData(269 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 17, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    "Smart Servos (Siege Tank)": ItemData(270 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    "Graduating Range (Siege Tank)": ItemData(271 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 19, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Siege Tank", origin={"ext"}),
    "Laser Targeting System (Siege Tank)": ItemData(272 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 20, SC2Race.TERRAN, parent_item="Siege Tank", origin={"nco"}),
    "Advanced Siege Tech (Siege Tank)": ItemData(273 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 21, SC2Race.TERRAN, parent_item="Siege Tank", origin={"ext"}),
    "Internal Tech Module (Siege Tank)": ItemData(274 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    "Optimized Logistics (Predator)": ItemData(275 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 23, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Predator", origin={"ext"}),
    "Expanded Hull (Medivac)": ItemData(276 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac", origin={"ext"}),
    "Afterburners (Medivac)": ItemData(277 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac", origin={"ext"}),
    "Advanced Laser Technology (Wraith)": ItemData(278 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 26, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Wraith", origin={"ext"}),
    "Smart Servos (Viking)": ItemData(279 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 27, SC2Race.TERRAN, parent_item="Viking", origin={"ext"}),
    "Magrail Munitions (Viking)": ItemData(280 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 28, SC2Race.TERRAN, parent_item="Viking", origin={"ext"}),

    "Twin-Linked Flamethrower (Hellion)": ItemData(300 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion"),
    "Thermite Filaments (Hellion)": ItemData(301 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 1, SC2Race.TERRAN, parent_item="Hellion"),
    "Cerberus Mine (Spider Mine)": ItemData(302 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 2, SC2Race.TERRAN, classification=ItemClassification.filler),
    "Replenishable Magazine (Vulture)": ItemData(303 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 3, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Vulture"),
    "Multi-Lock Weapons System (Goliath)": ItemData(304 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 4, SC2Race.TERRAN, parent_item="Goliath"),
    "Ares-Class Targeting System (Goliath)": ItemData(305 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 5, SC2Race.TERRAN, parent_item="Goliath"),
    "Tri-Lithium Power Cell (Diamondback)": ItemData(306 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback"),
    "Shaped Hull (Diamondback)": ItemData(307 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback"),
    "Maelstrom Rounds (Siege Tank)": ItemData(308 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 8, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Siege Tank"),
    "Shaped Blast (Siege Tank)": ItemData(309 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 9, SC2Race.TERRAN, parent_item="Siege Tank"),
    "Rapid Deployment Tube (Medivac)": ItemData(310 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 10, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac"),
    "Advanced Healing AI (Medivac)": ItemData(311 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 11, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac"),
    "Tomahawk Power Cells (Wraith)": ItemData(312 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Wraith"),
    "Displacement Field (Wraith)": ItemData(313 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 13, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Wraith"),
    "Ripwave Missiles (Viking)": ItemData(314 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 14, SC2Race.TERRAN, parent_item="Viking"),
    "Phobos-Class Weapons System (Viking)": ItemData(315 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 15, SC2Race.TERRAN, parent_item="Viking"),
    "Progressive Cross-Spectrum Dampeners (Banshee)": ItemData(316 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", quantity=2),
    "Shockwave Missile Battery (Banshee)": ItemData(317 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 17, SC2Race.TERRAN, parent_item="Banshee"),
    "Missile Pods (Battlecruiser)": ItemData(318 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser"),
    "Defensive Matrix (Battlecruiser)": ItemData(319 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 19, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser"),
    "Ocular Implants (Ghost)": ItemData(320 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 20, SC2Race.TERRAN, parent_item="Ghost"),
    "Crius Suit (Ghost)": ItemData(321 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 21, SC2Race.TERRAN, parent_item="Ghost"),
    "Psionic Lash (Spectre)": ItemData(322 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 22, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Spectre"),
    "Nyx-Class Cloaking Module (Spectre)": ItemData(323 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 23, SC2Race.TERRAN, parent_item="Spectre"),
    "330mm Barrage Cannon (Thor)": ItemData(324 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Thor"),
    "Immortality Protocol (Thor)": ItemData(325 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Thor"),
    # Items from EE
    "Advanced Ballistics (Liberator)": ItemData(326 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 26, SC2Race.TERRAN, parent_item="Liberator", origin={"ext"}),
    "Raid Artillery (Liberator)": ItemData(327 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 27, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Liberator", origin={"nco"}),
    "Drilling Claws (Widow Mine)": ItemData(328 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 28, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Widow Mine", origin={"ext"}),
    "Concealment (Widow Mine)": ItemData(329 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 29, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Widow Mine", origin={"ext"}),

    #Items from new mod
    "Hyperflight Rotors (Banshee)": ItemData(350 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"ext"}),
    "Laser Targeting System (Banshee)": ItemData(351 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 1, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"nco"}),
    "Internal Tech Module (Banshee)": ItemData(352 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"nco"}),
    "Tactical Jump (Battlecruiser)": ItemData(353 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 3, SC2Race.TERRAN, parent_item="Battlecruiser", origin={"nco", "ext"}),
    "Cloak (Battlecruiser)": ItemData(354 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 4, SC2Race.TERRAN, parent_item="Battlecruiser", origin={"nco"}),
    "ATX Laser Battery (Battlecruiser)": ItemData(355 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 5, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Battlecruiser", origin={"nco"}),
    "Optimized Logistics (Battlecruiser)": ItemData(356 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser", origin={"ext"}),
    "Internal Tech Module (Battlecruiser)": ItemData(357 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser", origin={"nco"}),
    "EMP Rounds (Ghost)": ItemData(358 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 8, SC2Race.TERRAN, parent_item="Ghost", origin={"ext"}),
    "Lockdown (Ghost)": ItemData(359 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 9, SC2Race.TERRAN, parent_item="Ghost", origin={"bw"}),
    "Impaler Rounds (Spectre)": ItemData(360 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 10, SC2Race.TERRAN, parent_item="Spectre", origin={"ext"}),
    "Progressive High Impact Payload (Thor)": ItemData(361 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 14, SC2Race.TERRAN, parent_item="Thor", quantity=2, origin={"ext"}),  # L2 is Smart Servos
    "Bio Mechanical Repair Drone (Raven)": ItemData(363 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 13, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    "Spider Mines (Raven)": ItemData(364 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 14, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    "Railgun Turret (Raven)": ItemData(365 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 15, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    "Hunter-Seeker Weapon (Raven)": ItemData(366 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 16, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    "Interference Matrix (Raven)": ItemData(367 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 17, SC2Race.TERRAN, parent_item="Raven", origin={"ext"}),
    "Anti-Armor Missile (Raven)": ItemData(368 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Raven", origin={"ext"}),
    "Internal Tech Module (Raven)": ItemData(369 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 19, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Raven", origin={"nco"}),
    "EMP Shockwave (Science Vessel)": ItemData(370 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 20, SC2Race.TERRAN, parent_item="Science Vessel", origin={"bw"}),
    "Defensive Matrix (Science Vessel)": ItemData(371 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 21, SC2Race.TERRAN, parent_item="Science Vessel", origin={"bw"}),
    "Targeting Optics (Cyclone)": ItemData(372 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 22, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    "Rapid Fire Launchers (Cyclone)": ItemData(373 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 23, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    "Cloak (Liberator)": ItemData(374 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"nco"}),
    "Laser Targeting System (Liberator)": ItemData(375 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"ext"}),
    "Optimized Logistics (Liberator)": ItemData(376 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 26, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"nco"}),
    "Black Market Launchers (Widow Mine)": ItemData(377 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 27, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Widow Mine", origin={"ext"}),
    "Executioner Missiles (Widow Mine)": ItemData(378 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 28, SC2Race.TERRAN, parent_item="Widow Mine", origin={"ext"}),

    # Just lazy to create a new group for one unit
    "Enhanced Cluster Launchers (Valkyrie)": ItemData(379 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 17, SC2Race.TERRAN, parent_item="Valkyrie", origin={"ext"}),
    "Shaped Hull (Valkyrie)": ItemData(380 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 20, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Valkyrie", origin={"ext"}),
    "Burst Lasers (Valkyrie)": ItemData(381 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 21, SC2Race.TERRAN, parent_item="Valkyrie", origin={"ext"}),
    "Afterburners (Valkyrie)": ItemData(382 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Valkyrie", origin={"ext"}),

    "Bunker": ItemData(400 + SC2WOL_ITEM_ID_OFFSET, "Building", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Missile Turret": ItemData(401 + SC2WOL_ITEM_ID_OFFSET, "Building", 1, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Sensor Tower": ItemData(402 + SC2WOL_ITEM_ID_OFFSET, "Building", 2, SC2Race.TERRAN),

    "War Pigs": ItemData(500 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Devil Dogs": ItemData(501 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 1, SC2Race.TERRAN, classification=ItemClassification.filler),
    "Hammer Securities": ItemData(502 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 2, SC2Race.TERRAN),
    "Spartan Company": ItemData(503 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 3, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Siege Breakers": ItemData(504 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 4, SC2Race.TERRAN),
    "Hel's Angel": ItemData(505 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 5, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Dusk Wings": ItemData(506 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 6, SC2Race.TERRAN),
    "Jackson's Revenge": ItemData(507 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 7, SC2Race.TERRAN),

    "Ultra-Capacitors": ItemData(600 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 0, SC2Race.TERRAN),
    "Vanadium Plating": ItemData(601 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 1, SC2Race.TERRAN),
    "Orbital Depots": ItemData(602 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 2, SC2Race.TERRAN),
    "Micro-Filtering": ItemData(603 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 3, SC2Race.TERRAN),
    "Automated Refinery": ItemData(604 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 4, SC2Race.TERRAN),
    "Command Center Reactor": ItemData(605 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 5, SC2Race.TERRAN),
    "Raven": ItemData(606 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 6, SC2Race.TERRAN),
    "Science Vessel": ItemData(607 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 7, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Tech Reactor": ItemData(608 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 8, SC2Race.TERRAN),
    "Orbital Strike": ItemData(609 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 9, SC2Race.TERRAN),
    "Shrike Turret (Bunker)": ItemData(610 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 10, SC2Race.TERRAN, parent_item="Bunker"),
    "Fortified Bunker (Bunker)": ItemData(611 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 11, SC2Race.TERRAN, parent_item="Bunker"),
    "Planetary Fortress": ItemData(612 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 12, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Perdition Turret": ItemData(613 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 13, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Predator": ItemData(614 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 14, SC2Race.TERRAN, classification=ItemClassification.filler),
    "Hercules": ItemData(615 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 15, SC2Race.TERRAN, classification=ItemClassification.progression),
    "Cellular Reactor": ItemData(616 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 16, SC2Race.TERRAN),
    "Progressive Regenerative Bio-Steel": ItemData(617 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 4, SC2Race.TERRAN, quantity=2),
    "Hive Mind Emulator": ItemData(618 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 18, SC2Race.TERRAN, ItemClassification.progression),
    "Psi Disrupter": ItemData(619 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 19, SC2Race.TERRAN, classification=ItemClassification.progression),

    "Zealot": ItemData(700 + SC2WOL_ITEM_ID_OFFSET, "Unit", 0, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "Stalker": ItemData(701 + SC2WOL_ITEM_ID_OFFSET, "Unit", 1, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "High Templar": ItemData(702 + SC2WOL_ITEM_ID_OFFSET, "Unit", 2, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "Dark Templar": ItemData(703 + SC2WOL_ITEM_ID_OFFSET, "Unit", 3, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "Immortal": ItemData(704 + SC2WOL_ITEM_ID_OFFSET, "Unit", 4, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "Colossus": ItemData(705 + SC2WOL_ITEM_ID_OFFSET, "Unit", 5, SC2Race.PROTOSS),
    "Phoenix": ItemData(706 + SC2WOL_ITEM_ID_OFFSET, "Unit", 6, SC2Race.PROTOSS, classification=ItemClassification.filler),
    "Void Ray": ItemData(707 + SC2WOL_ITEM_ID_OFFSET, "Unit", 7, SC2Race.PROTOSS, classification=ItemClassification.progression),
    "Carrier": ItemData(708 + SC2WOL_ITEM_ID_OFFSET, "Unit", 8, SC2Race.PROTOSS, classification=ItemClassification.progression),

    # Filler items to fill remaining spots
    "+15 Starting Minerals": ItemData(800 + SC2WOL_ITEM_ID_OFFSET, "Minerals", 15, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    "+15 Starting Vespene": ItemData(801 + SC2WOL_ITEM_ID_OFFSET, "Vespene", 15, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    # This Filler item isn't placed by the generator yet unless plando'd
    "+2 Starting Supply": ItemData(802 + SC2WOL_ITEM_ID_OFFSET, "Supply", 2, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    # This item is used to "remove" location from the game. Never placed unless plando'd
    "Nothing": ItemData(803 + SC2WOL_ITEM_ID_OFFSET, "Nothing Group", 2, SC2Race.ANY, quantity=0, classification=ItemClassification.trap),

    # "Keystone Piece": ItemData(850 + SC2WOL_ITEM_ID_OFFSET, "Goal", 0, quantity=0, classification=ItemClassification.progression_skip_balancing)

    # HotS
    "Zergling": ItemData(0 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 0, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Swarm Queen": ItemData(1 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 1, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Roach": ItemData(2 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 2, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Hydralisk": ItemData(3 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 3, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Baneling": ItemData(4 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 4, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Aberration": ItemData(5 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 5, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Mutalisk": ItemData(6 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 6, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Swarm Host": ItemData(7 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 7, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Infestor": ItemData(8 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 8, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Ultralisk": ItemData(9 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 9, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Spore Crawler": ItemData(10 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 10, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    "Spine Crawler": ItemData(11 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 11, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    
    "Progressive Zerg Melee Attack": ItemData(100 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Missile Attack": ItemData(101 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Ground Carapace": ItemData(102 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Flyer Attack": ItemData(103 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Flyer Carapace": ItemData(104 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.ZERG, quantity=3, origin={"hots"}),
    # Upgrade bundle 'number' values are used as indices to get affected 'number's
    "Progressive Zerg Weapon Upgrade": ItemData(105 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Armor Upgrade": ItemData(106 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 7, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Ground Upgrade": ItemData(107 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Flyer Upgrade": ItemData(108 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 9, SC2Race.ZERG, quantity=3, origin={"hots"}),
    "Progressive Zerg Weapon/Armor Upgrade": ItemData(109 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 10, SC2Race.ZERG, quantity=3, origin={"hots"}),

    "Hardened Carapace (Zergling)": ItemData(200 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 0, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    "Adrenal Overload (Zergling)": ItemData(201 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 1, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    "Metabolic Boost (Zergling)": ItemData(202 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 2, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}, classification=ItemClassification.filler),
    "Hydriodic Bile (Roach)": ItemData(203 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 3, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    "Adaptive Plating (Roach)": ItemData(204 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 4, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    "Tunneling Claws (Roach)": ItemData(205 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 5, SC2Race.ZERG, parent_item="Roach", origin={"hots"}, classification=ItemClassification.filler),
    "Frenzy (Hydralisk)": ItemData(206 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 6, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}),
    "Ancillary Carapace (Hydralisk)": ItemData(207 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 7, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.filler),
    "Grooved Spines (Hydralisk)": ItemData(208 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 8, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}),
    "Corrosive Acid (Baneling)": ItemData(209 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 9, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    "Rupture (Baneling)": ItemData(210 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 10, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}, classification=ItemClassification.filler),
    "Regenerative Acid (Baneling)": ItemData(211 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 11, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}, classification=ItemClassification.filler),
    "Vicious Glave (Mutalisk)": ItemData(212 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 12, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    "Rapid Regeneration (Mutalisk)": ItemData(213 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 13, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    "Sundering Glave (Mutalisk)": ItemData(214 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 14, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    "Burrow (Swarm Host)": ItemData(215 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 15, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.filler),
    "Rapid Incubation (Swarm Host)": ItemData(216 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 16, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}),
    "Pressurized Glands (Swarm Host)": ItemData(217 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 17, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.progression),
    "Burrow Charge (Ultralisk)": ItemData(218 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 18, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    "Tissue Animation (Ultralisk)": ItemData(219 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 19, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    "Monarch Blades (Ultralisk)": ItemData(220 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 20, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    
    "Raptor Strain (Zergling)": ItemData(300 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 0, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    "Swarmling Strain (Zergling)": ItemData(301 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 1, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    "Vile Strain (Roach)": ItemData(302 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 2, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    "Corpser Strain (Roach)": ItemData(303 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 3, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    "Impaler Strain (Hydralisk)": ItemData(304 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 4, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.progression),
    "Lurker Strain (Hydralisk)": ItemData(305 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 5, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.progression),
    "Splitter Strain (Baneling)": ItemData(306 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 6, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    "Hunter Strain (Baneling)": ItemData(307 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 7, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    "Brood Lord Strain (Mutalisk)": ItemData(308 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 8, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}, classification=ItemClassification.progression),
    "Viper Strain (Mutalisk)": ItemData(309 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 9, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}, classification=ItemClassification.progression),
    "Carrion Strain (Swarm Host)": ItemData(310 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 10, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}),
    "Creeper Strain (Swarm Host)": ItemData(311 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 11, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.filler),
    "Noxious Strain (Ultralisk)": ItemData(312 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 12, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}, classification=ItemClassification.filler),
    "Torrasque Strain (Ultralisk)": ItemData(313 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 13, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    
    "Kinetic Blast (Kerrigan Tier 1)": ItemData(400 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 0, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Heroic Fortitude (Kerrigan Tier 1)": ItemData(401 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 1, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Leaping Strike (Kerrigan Tier 1)": ItemData(402 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 2, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Crushing Grip (Kerrigan Tier 2)": ItemData(403 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 3, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Chain Reaction (Kerrigan Tier 2)": ItemData(404 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 4, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Psionic Shift (Kerrigan Tier 2)": ItemData(405 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 5, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Zergling Reconstitution (Kerrigan Tier 3)": ItemData(406 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 6, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.filler),
    "Improved Overlords (Kerrigan Tier 3)": ItemData(407 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 7, SC2Race.ZERG, origin={"hots"}),
    "Automated Extractors (Kerrigan Tier 3)": ItemData(408 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 8, SC2Race.ZERG, origin={"hots"}),
    "Wild Mutation (Kerrigan Tier 4)": ItemData(409 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 9, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Spawn Banelings (Kerrigan Tier 4)": ItemData(410 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 10, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Mend (Kerrigan Tier 4)": ItemData(411 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 11, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Twin Drones (Kerrigan Tier 5)": ItemData(412 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 12, SC2Race.ZERG, origin={"hots"}),
    "Malignant Creep (Kerrigan Tier 5)": ItemData(413 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 13, SC2Race.ZERG, origin={"hots"}),
    "Vespene Efficiency (Kerrigan Tier 5)": ItemData(414 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 14, SC2Race.ZERG, origin={"hots"}),
    "Infest Broodlings (Kerrigan Tier 6)": ItemData(415 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 15, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Fury (Kerrigan Tier 6)": ItemData(416 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 16, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Ability Efficiency (Kerrigan Tier 6)": ItemData(417 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 17, SC2Race.ZERG, origin={"hots"}),
    "Apocalypse (Kerrigan Tier 7)": ItemData(418 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 18, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Spawn Leviathan (Kerrigan Tier 7)": ItemData(419 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 19, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    "Drop-Pods (Kerrigan Tier 7)": ItemData(420 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 20, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    # Handled separately from other abilities
    "Primal Form (Kerrigan)": ItemData(421 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 0, SC2Race.ZERG, origin={"hots"}),
    
    "10 Kerrigan Levels": ItemData(500 + SC2HOTS_ITEM_ID_OFFSET, "Level", 10, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "9 Kerrigan Levels": ItemData(501 + SC2HOTS_ITEM_ID_OFFSET, "Level", 9, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "8 Kerrigan Levels": ItemData(502 + SC2HOTS_ITEM_ID_OFFSET, "Level", 8, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "7 Kerrigan Levels": ItemData(503 + SC2HOTS_ITEM_ID_OFFSET, "Level", 7, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "6 Kerrigan Levels": ItemData(504 + SC2HOTS_ITEM_ID_OFFSET, "Level", 6, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "5 Kerrigan Levels": ItemData(505 + SC2HOTS_ITEM_ID_OFFSET, "Level", 5, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "4 Kerrigan Levels": ItemData(506 + SC2HOTS_ITEM_ID_OFFSET, "Level", 4, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    "3 Kerrigan Levels": ItemData(507 + SC2HOTS_ITEM_ID_OFFSET, "Level", 3, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    "2 Kerrigan Levels": ItemData(508 + SC2HOTS_ITEM_ID_OFFSET, "Level", 2, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    "1 Kerrigan Level": ItemData(509 + SC2HOTS_ITEM_ID_OFFSET, "Level", 1, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    "14 Kerrigan Levels": ItemData(510 + SC2HOTS_ITEM_ID_OFFSET, "Level", 14, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "35 Kerrigan Levels": ItemData(511 + SC2HOTS_ITEM_ID_OFFSET, "Level", 35, SC2Race.ZERG, origin={"hots"}, quantity=0),
    "70 Kerrigan Levels": ItemData(512 + SC2HOTS_ITEM_ID_OFFSET, "Level", 70, SC2Race.ZERG, origin={"hots"}, quantity=0),
}

def get_item_table(multiworld: MultiWorld, player: int):
    return item_table

basic_units = {
    SC2Race.TERRAN: {
        'Marine',
        'Marauder',
        'Goliath',
        'Hellion',
        'Vulture'
    },
    SC2Race.ZERG: {
        'Zergling',
        'Swarm Queen',
        'Roach',
        'Hydralisk'
    },
    # TODO Placeholder for Prophecy
    SC2Race.PROTOSS: {
        'Zealot',
        'Stalker'
    }
}

advanced_basic_units = {
    SC2Race.TERRAN: basic_units[SC2Race.TERRAN].union({
        'Reaper',
        'Diamondback',
        'Viking'
    }),
    SC2Race.ZERG: basic_units[SC2Race.ZERG].union({
        'Infestor',
        'Aberration'
    }),
    SC2Race.PROTOSS: basic_units[SC2Race.PROTOSS].union({
        'Dark Templar',
    })
}


def get_basic_units(multiworld: MultiWorld, player: int, race: SC2Race) -> typing.Set[str]:
    if get_option_value(multiworld, player, 'required_tactics') > 0:
        return advanced_basic_units[race]
    else:
        return basic_units[race]


item_name_groups = {}
for item, data in get_full_item_list().items():
    item_name_groups.setdefault(data.type, []).append(item)
    if data.type in ("Armory 1", "Armory 2", "Armory 3", "Armory 4", "Laboratory", "Progressive Upgrade") and '(' in item:
        short_name = item[:item.find(' (')]
        item_name_groups[short_name] = [item]
item_name_groups["Missions"] = ["Beat " + mission.mission_name for mission in SC2Mission]
item_name_groups["WoL Missions"] = ["Beat " + mission.mission_name for mission in campaign_mission_table[SC2Campaign.WOL]]


# Items that can be placed before resources if not already in
# General upgrades and Mercs
# TODO needs zerg items
second_pass_placeable_items: typing.Tuple[str, ...] = (
    # Buildings without upgrades
    "Sensor Tower",
    "Hive Mind Emulator",
    "Psi Disrupter",
    "Perdition Turret",
    # General upgrades without any dependencies
    "Advanced Construction (SCV)",
    "Dual-Fusion Welders (SCV)",
    "Fire-Suppression System (Building)",
    "Orbital Command (Building)",
    "Ultra-Capacitors",
    "Vanadium Plating",
    "Orbital Depots",
    "Micro-Filtering",
    "Automated Refinery",
    "Command Center Reactor",
    "Tech Reactor",
    "Planetary Fortress",
    "Cellular Reactor",
    "Progressive Regenerative Bio-Steel",  # Place only L1
    # Mercenaries
    "War Pigs",
    "Devil Dogs",
    "Hammer Securities",
    "Spartan Company",
    "Siege Breakers",
    "Hel's Angel",
    "Dusk Wings",
    "Jackson's Revenge"
)


filler_items: typing.Tuple[str, ...] = (
    '+15 Starting Minerals',
    '+15 Starting Vespene'
)

# Defense rating table
# Commented defense ratings are handled in LogicMixin
defense_ratings = {
    "Siege Tank": 5,
    # "Maelstrom Rounds": 2,
    "Planetary Fortress": 3,
    # Bunker w/ Marine/Marauder: 3,
    "Perdition Turret": 2,
    "Missile Turret": 2,
    "Vulture": 2,
    "Liberator": 2,
    "Widow Mine": 2
    # "Concealment (Widow Mine)": 1
}
zerg_defense_ratings = {
    "Perdition Turret": 2,
    # Bunker w/ Firebat: 2,
    "Hive Mind Emulator": 3,
    "Psi Disruptor": 3
}

spider_mine_sources = {
    "Vulture",
    "Spider Mines (Reaper)",
    "Spider Mines (Siege Tank)",
    "Spider Mines (Raven)"
}

progressive_if_nco = {
    "Progressive Stimpack (Marine)",
    "Progressive Stimpack (Firebat)",
    "Progressive Cross-Spectrum Dampeners (Banshee)",
    "Progressive Regenerative Bio-Steel"
}

kerrigan_actives = [
    {'Kinetic Blast (Kerrigan Tier 1)', 'Leaping Strike (Kerrigan Tier 1)'},
    {'Crushing Grip (Kerrigan Tier 2)', 'Psionic Shift (Kerrigan Tier 2)'},
    set(),
    {'Wild Mutation (Kerrigan Tier 4)', 'Spawn Banelings (Kerrigan Tier 4)', 'Mend (Kerrigan Tier 4)'},
    set(),
    set(),
    {'Apocalypse (Kerrigan Tier 7)', 'Spawn Leviathan (Kerrigan Tier 7)', 'Drop-Pods (Kerrigan Tier 7)'},
]

kerrigan_passives = [
    {"Heroic Fortitude (Kerrigan Tier 1)"},
    {"Chain Reaction (Kerrigan Tier 2)"},
    {"Zergling Reconstitution (Kerrigan Tier 3)", "Improved Overlords (Kerrigan Tier 3)", "Automated Extractors (Kerrigan Tier 3)"},
    set(),
    {"Twin Drones (Kerrigan Tier 5)", "Malignant Creep (Kerrigan Tier 5)", "Vespene Efficiency (Kerrigan Tier 5)"},
    {"Infest Broodlings (Kerrigan Tier 6)", "Fury (Kerrigan Tier 6)", "Ability Efficiency (Kerrigan Tier 6)"},
    set(),
]

kerrigan_only_passives = {
    "Heroic Fortitude (Kerrigan Tier 1)", "Chain Reaction (Kerrigan Tier 2)",
    "Infest Broodlings (Kerrigan Tier 6)", "Fury (Kerrigan Tier 6)", "Ability Efficiency (Kerrigan Tier 6)"
}

# 'number' values of upgrades for upgrade bundle items
upgrade_numbers = [
    # Terran
    {0, 4, 8}, # Weapon
    {2, 6, 10}, # Armor
    {0, 2}, # Infantry
    {4, 6}, # Vehicle
    {8, 10}, # Starship
    {0, 2, 4, 6, 8, 10}, # All
    # Zerg
    {0, 2, 6}, # Weapon
    {4, 8}, # Armor
    {0, 2, 4}, # Ground
    {6, 8}, # Flyer
    {0, 2, 4, 6, 8}, # All
]
# 'upgrade_numbers' indices for all upgrades
upgrade_numbers_all = {
    SC2Race.TERRAN: 5,
    SC2Race.ZERG: 10,
}

# Names of upgrades to be included for different options
upgrade_included_names = [
    { # Individual Items
        "Progressive Terran Infantry Weapon",
        "Progressive Terran Infantry Armor",
        "Progressive Terran Vehicle Weapon",
        "Progressive Terran Vehicle Armor",
        "Progressive Terran Ship Weapon",
        "Progressive Terran Ship Armor",
        "Progressive Zerg Melee Attack",
        "Progressive Zerg Missile Attack",
        "Progressive Zerg Ground Carapace",
        "Progressive Zerg Flyer Attack",
        "Progressive Zerg Flyer Carapace"
    },
    { # Bundle Weapon And Armor
        "Progressive Terran Weapon Upgrade",
        "Progressive Terran Armor Upgrade",
        "Progressive Zerg Weapon Upgrade",
        "Progressive Zerg Armor Upgrade"
    },
    { # Bundle Unit Class
        "Progressive Terran Infantry Upgrade",
        "Progressive Terran Vehicle Upgrade",
        "Progressive Terran Starship Upgrade",
        "Progressive Zerg Ground Upgrade",
        "Progressive Zerg Flyer Upgrade"
    },
    { # Bundle All
        "Progressive Terran Weapon/Armor Upgrade",
        "Progressive Zerg Weapon/Armor Upgrade"
    }
]

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in get_full_item_list().items() if
                                            data.code}

# Map type to expected int
type_flaggroups: typing.Dict[SC2Race, typing.Dict[str, int]] = {
    SC2Race.ANY: {
        "Minerals": 0,
        "Vespene": 1,
        "Supply": 2,
        "Goal": 3,
        "Nothing Group": 4,
    },
    SC2Race.TERRAN: {
        "Unit": 0,
        "Upgrade": 1,  # Weapon / Armor upgrades
        "Armory 1": 2,  # Unit upgrades
        "Armory 2": 3,  # Unit upgrades
        "Building": 4,
        "Mercenary": 5,
        "Laboratory": 6,
        "Armory 3": 7,  # Unit upgrades
        "Armory 4": 8,  # Unit upgrades
        "Progressive Upgrade": 9,  # Unit upgrades that exist multiple times (Stimpack / Super Stimpack)
    },
    SC2Race.ZERG: {
        "Unit": 0,
        "Upgrade": 1,
        "Mutation": 2,
        "Strain": 3,
        "Ability": 4,
        "Level": 5,
    },
    SC2Race.PROTOSS: {
        "Unit": 0,
    }
}
