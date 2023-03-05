from ..generic.Rules import add_rule, set_rule
from .Regions import connect_regions, sm64courses, sm64paintings, sm64secrets, sm64entrances

def fix_reg(entrance_ids, reg, invalidspot, swaplist, world):
    if entrance_ids.index(reg) == invalidspot: # Unlucky :C
            swaplist.remove(invalidspot)
            rand = world.random.choice(swaplist)
            entrance_ids[invalidspot], entrance_ids[rand] = entrance_ids[rand], entrance_ids[invalidspot]
            swaplist.append(invalidspot)
            swaplist.remove(rand)

def set_rules(world, player: int, area_connections):
    destination_regions = list(range(13)) + [12,13,14] + list(range(15,15+len(sm64secrets))) # Two instances of Destination Course THI. Past normal course idx are secret regions
    secret_entrance_ids = list(range(len(sm64paintings), len(sm64paintings) + len(sm64secrets)))
    course_entrance_ids = list(range(len(sm64paintings)))
    valid_move_randomizer_start_courses = [0, 2, 3, 4, 6, 7, 8, 9]  # Excluding WF, HMC, WDW, TTM, THI, TTC, and RR
    if world.AreaRandomizer[player].value >= 1:  # Some randomization is happening, randomize Courses
        world.random.shuffle(course_entrance_ids)
        if world.AreaRandomizer[player].value < 3 and world.RandomizeMoves[player]:
            first_course = world.random.choice(valid_move_randomizer_start_courses)
            original_position = course_entrance_ids.index(first_course)
            swap_course = course_entrance_ids[0]
            course_entrance_ids[0] = first_course
            course_entrance_ids[original_position] = swap_course

    if world.AreaRandomizer[player].value == 2:  # Randomize Secrets as well
        world.random.shuffle(secret_entrance_ids)
    entrance_ids = course_entrance_ids + secret_entrance_ids
    if world.AreaRandomizer[player].value == 3:  # Randomize Courses and Secrets in one pool
        world.random.shuffle(entrance_ids)
        # Guarantee first entrance is a course
        swaplist = list(range(len(entrance_ids)))
        valid_first_courses = valid_move_randomizer_start_courses if world.RandomizeMoves[player] else list(range(15))
        if entrance_ids.index(0) not in valid_first_courses:  # Unlucky :C
            rand = world.random.choice(valid_first_courses)
            entrance_ids[entrance_ids.index(0)], entrance_ids[rand] = entrance_ids[rand], entrance_ids[entrance_ids.index(0)]
            swaplist.remove(entrance_ids.index(0))
        # Guarantee COTMC is not mapped to HMC, cuz thats impossible
        fix_reg(entrance_ids, 20, 5, swaplist, world)
        # Guarantee BITFS is not mapped to DDD
        fix_reg(entrance_ids, 22, 8, swaplist, world)
    temp_assign = dict(zip(entrance_ids,destination_regions)) # Used for Rules only

    # Destination Format: LVL | AREA with LVL = LEVEL_x, AREA = Area as used in sm64 code
    area_connections.update({sm64entrances[entrance]: destination for entrance, destination in zip(entrance_ids,sm64entrances)})

    connect_regions(world, player, "Menu", sm64courses[temp_assign[0]]) # BOB
    connect_regions(world, player, "Menu", sm64courses[temp_assign[1]], lambda state: state.has("Power Star", player, 1)) # WF
    connect_regions(world, player, "Menu", sm64courses[temp_assign[2]], lambda state: state.has("Power Star", player, 3)) # JRB
    connect_regions(world, player, "Menu", sm64courses[temp_assign[3]], lambda state: state.has("Power Star", player, 3)) # CCM
    connect_regions(world, player, "Menu", sm64courses[temp_assign[4]], lambda state: state.has("Power Star", player, 12)) # BBH
    connect_regions(world, player, "Menu", sm64courses[temp_assign[16]], lambda state: state.has("Power Star", player, 1)) # PSS
    connect_regions(world, player, "Menu", sm64courses[temp_assign[17]], lambda state: state.has("Power Star", player, 3)) # SA
    connect_regions(world, player, "Menu", sm64courses[temp_assign[19]], lambda state: state.has("Power Star", player, 10)) # TOTWC
    connect_regions(world, player, "Menu", sm64courses[temp_assign[18]], lambda state: state.has("Power Star", player, world.FirstBowserStarDoorCost[player].value)) # BITDW

    connect_regions(world, player, "Menu", "Basement", lambda state: state.has("Basement Key", player) or state.has("Progressive Key", player, 1))

    connect_regions(world, player, "Basement", sm64courses[temp_assign[5]]) # HMC
    connect_regions(world, player, "Basement", sm64courses[temp_assign[6]]) # LLL
    connect_regions(world, player, "Basement", sm64courses[temp_assign[7]]) # SSL
    connect_regions(world, player, "Basement", sm64courses[temp_assign[8]], lambda state: state.has("Power Star", player, world.BasementStarDoorCost[player].value)) # DDD
    connect_regions(world, player, "Hazy Maze Cave", sm64courses[temp_assign[20]]) # COTMC
    if world.RandomizeMoves[player]:
        connect_regions(world, player, "Basement", sm64courses[temp_assign[21]], lambda state: state.has("Ground Pound", player))  # VCUTM
    else:
        connect_regions(world, player, "Basement", sm64courses[temp_assign[21]]) # VCUTM
    connect_regions(world, player, "Basement", sm64courses[temp_assign[22]], lambda state: state.has("Power Star", player, world.BasementStarDoorCost[player].value) and
                                                                                       state.can_reach("DDD: Board Bowser's Sub", 'Location', player)) # BITFS

    connect_regions(world, player, "Menu", "Second Floor", lambda state: state.has("Second Floor Key", player) or state.has("Progressive Key", player, 2))

    connect_regions(world, player, "Second Floor", sm64courses[temp_assign[9]]) # SL
    connect_regions(world, player, "Second Floor", sm64courses[temp_assign[10]]) # WDW
    connect_regions(world, player, "Second Floor", sm64courses[temp_assign[11]]) # TTM
    connect_regions(world, player, "Second Floor", sm64courses[temp_assign[12]]) # THI Tiny
    connect_regions(world, player, "Second Floor", sm64courses[temp_assign[13]]) # THI Huge

    connect_regions(world, player, "Second Floor", "Third Floor", lambda state: state.has("Power Star", player, world.SecondFloorStarDoorCost[player].value))
    if world.RandomizeMoves[player]:
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[14]],
                        lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Backflip", "Side Flip"}, player)) # TTC
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[15]],
                        lambda state: state.has_any({"Triple Jump", "Backflip", "Side Flip"}, player))  # RR
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[23]],
                        lambda state: state.has_any({"Triple Jump", "Backflip", "Side Flip"}, player))  # WMOTR
    else:
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[14]]) # TTC
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[15]]) # RR
        connect_regions(world, player, "Third Floor", sm64courses[temp_assign[23]]) # WMOTR
    connect_regions(world, player, "Third Floor", "Bowser in the Sky", lambda state: state.has("Power Star", player, world.StarsToFinish[player].value)) # BITS

    #Special Rules for some Locations
    add_rule(world.get_location("BoB: Mario Wings to the Sky", player), lambda state: state.has("Cannon Unlock BoB", player))
    add_rule(world.get_location("BBH: Eye to Eye in the Secret Room", player), lambda state: state.has("Vanish Cap", player))
    add_rule(world.get_location("DDD: Collect the Caps...", player), lambda state: state.has("Vanish Cap", player))
    add_rule(world.get_location("DDD: Pole-Jumping for Red Coins", player), lambda state: state.can_reach("Bowser in the Fire Sea", 'Region', player))
    if world.EnableCoinStars[player]:
        add_rule(world.get_location("DDD: 100 Coins", player), lambda state: state.can_reach("Bowser in the Fire Sea", 'Region', player))
    add_rule(world.get_location("SL: Into the Igloo", player), lambda state: state.has("Vanish Cap", player))
    add_rule(world.get_location("WDW: Quick Race Through Downtown!", player), lambda state: state.has("Vanish Cap", player))
    add_rule(world.get_location("RR: Somewhere Over the Rainbow", player), lambda state: state.has("Cannon Unlock RR", player))

    if world.AreaRandomizer[player] or world.StrictCannonRequirements[player]:
        # If area rando is on, it may not be possible to modify WDW's starting water level,
        # which would make it impossible to reach downtown area without the cannon.
        add_rule(world.get_location("WDW: Quick Race Through Downtown!", player), lambda state: state.has("Cannon Unlock WDW", player))
        add_rule(world.get_location("WDW: Go to Town for Red Coins", player), lambda state: state.has("Cannon Unlock WDW", player))
        add_rule(world.get_location("WDW: 1Up Block in Downtown", player), lambda state: state.has("Cannon Unlock WDW", player))

    if world.StrictCapRequirements[player]:
        add_rule(world.get_location("BoB: Mario Wings to the Sky", player), lambda state: state.has("Wing Cap", player))
        add_rule(world.get_location("HMC: Metal-Head Mario Can Move!", player), lambda state: state.has("Metal Cap", player))
        add_rule(world.get_location("JRB: Through the Jet Stream", player), lambda state: state.has("Metal Cap", player))
        add_rule(world.get_location("SSL: Free Flying for 8 Red Coins", player), lambda state: state.has("Wing Cap", player))
        add_rule(world.get_location("DDD: Through the Jet Stream", player), lambda state: state.has("Metal Cap", player))
        add_rule(world.get_location("DDD: Collect the Caps...", player), lambda state: state.has("Metal Cap", player))
        add_rule(world.get_location("Vanish Cap Under the Moat Red Coins", player), lambda state: state.has("Vanish Cap", player))
        add_rule(world.get_location("Cavern of the Metal Cap Red Coins", player), lambda state: state.has("Metal Cap", player))
    if world.StrictCannonRequirements[player]:
        add_rule(world.get_location("WF: Blast Away the Wall", player), lambda state: state.has("Cannon Unlock WF", player))
        add_rule(world.get_location("JRB: Blast to the Stone Pillar", player), lambda state: state.has("Cannon Unlock JRB", player))
        add_rule(world.get_location("CCM: Wall Kicks Will Work", player), lambda state: state.has("Cannon Unlock CCM", player))
        add_rule(world.get_location("TTM: Blast to the Lonely Mushroom", player), lambda state: state.has("Cannon Unlock TTM", player))
    if world.StrictCapRequirements[player] and world.StrictCannonRequirements[player]:
        # Ability to reach the floating island. Need some of those coins to get 100 coin star as well.
        add_rule(world.get_location("BoB: Find the 8 Red Coins", player), lambda state: state.has("Cannon Unlock BoB", player) or state.has("Wing Cap", player))
        add_rule(world.get_location("BoB: Shoot to the Island in the Sky", player), lambda state: state.has("Cannon Unlock BoB", player) or state.has("Wing Cap", player))
        if world.EnableCoinStars[player]:
            add_rule(world.get_location("BoB: 100 Coins", player), lambda state: state.has("Cannon Unlock BoB", player) or state.has("Wing Cap", player))
    if world.RandomizeMoves[player]:
        # Bob-omb Battlefield
        def can_reach_bob_island(state):
            # Either flying to the island, or long jumping to it
            return state.has("Wing Cap", player) and state.has_any({"Triple Jump", "Cannon Unlock BoB"}, player) \
                or not world.StrictCannonRequirements[player] and not world.StrictCapRequirements[player] and state.has("Long Jump")
        set_rule(world.get_location("BoB: Shoot to the Island in the Sky", player), lambda state: can_reach_bob_island(state))
        set_rule(world.get_location("BoB: Find the 8 Red Coins", player), lambda state: can_reach_bob_island(state))
        # Whomp's Fortress
        add_rule(world.get_location("WF: Chip Off Whomp's Block", player), lambda state: state.has("Ground Pound", player))
        add_rule(world.get_location("WF: To the Top of the Fortress", player), lambda state: state.has("Ground Pound", player))  # Requires King Whomp to be defeated first
        add_rule(world.get_location("WF: Shoot into the Wild Blue", player),
                 lambda state: state.has("Wall Kick", player) and state.has_any({"Triple Jump", "Side Flip", "Kick"}, player) or state.has_all({"Cannon Unlock WF", "Climb"}, player))
        add_rule(world.get_location("WF: Fall onto the Caged Island", player), lambda state: state.has("Climb", player))
        # Jolly Roger Bay
        add_rule(world.get_location("JRB: Red Coins on the Ship Afloat", player),
                 lambda state: state.has("Climb", player) and state.has_any({"Triple Jump", "Backflip", "Side Flip"}, player))
        # Big Boo's Haunt
        add_rule(world.get_location("BBH: Secret of the Haunted Books", player),
                 lambda state: state.has("Triple Jump", player) or state.has_all({"Side Flip", "Dive"}, player)
                               or state.has_all({"Long Jump", "Wall Kick"}, player))
        add_rule(world.get_location("BBH: Seek the 8 Red Coins", player), lambda state: state.has_any({"Backflip", "Wall Kick"}, player))
        add_rule(world.get_location("BBH: Big Boo's Balcony", player), lambda state: state.has("Wall Jump", player) or state.has_all({"Triple Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("BBH: Eye to Eye in the Secret Room", player), lambda state: state.has("Wall Jump", player) or state.has_all({"Triple Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("BBH: 1Up Block Top of Mansion", player), lambda state: state.has("Wall Jump", player) or state.has_all({"Triple Jump", "Ledge Grab"}, player))
        # Hazy Maze Cave
        add_rule(world.get_location("HMC: Elevate for 8 Red Coins", player), lambda state: state.has("Climb", player))
        set_rule(world.get_location("HMC: Metal-Head Mario Can Move!", player),
                 lambda state: state.has("Long Jump", player) and (state.has("Metal Cap", player) or not world.StrictCapRequirements[player] and state.has("Triple Jump", player)))
        add_rule(world.get_location("HMC: Navigating the Toxic Maze", player),
                 lambda state: state.has_all({"Wall Kick", "Ledge Grab"}, player) or state.has_any({"Side Flip", "Backflip", "Triple Jump"}, player))
        add_rule(world.get_location("HMC: A-Maze-Ing Emergency Exit", player),
                 lambda state: state.has_all({"Triple Jump", "Climb"}, player) or (state.has("Long Jump", player) and state.has_any({"Side Flip", "Wall Kick", "Backflip"}, player)))
        add_rule(world.get_location("HMC: Watch for Rolling Rocks", player), lambda state: state.has("Wall Kick", player))
        add_rule(world.get_location("HMC: 1Up Block above Pit", player),
                 lambda state: state.has_all({"Triple Jump", "Climb"}, player))
        # Lethal Lava Land
        add_rule(world.get_location("LLL: Hot-Foot-It into the Volcano", player), lambda state: state.has("Climb", player))
        add_rule(world.get_location("LLL: Elevator Tour in the Volcano", player), lambda state: state.has("Climb", player))
        # Dire, Dire Docks
        add_rule(world.get_location("DDD: Pole-Jumping for Red Coins", player), lambda state: state.has("Climb", player))
        # Snowman's Land
        add_rule(world.get_location("SL: Snowman's Big Head", player),
                 lambda state: state.has_any({"Backflip", "Side Flip", "Cannon Unlock SL"}, player) or state.has_all({"Triple Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("SL: In the Deep Freeze", player), lambda state: state.has_any({"Backflip", "Side Flip", "Wall Kick"}, player))
        add_rule(world.get_location("SL: Into the Igloo", player), lambda state: state.has_any({"Triple Jump", "Backflip", "Side Flip", "Wall Kick"}, player))
        # Wet-Dry World
        def can_reach_wdw_downtown(state):
            return state.has("Cannon Unlock WDW", player) or not world.AreaRandomizer[player] and state.has("Ledge Grab", player) and state.has_any({"Backflip", "Side Flip", "Triple Jump"}, player)
        set_rule(world.get_location("WDW: Shocking Arrow Lifts!", player), lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Side Flip", "Backflip"}, player))
        set_rule(world.get_location("WDW: Top o' the Town", player),
                 lambda state: state.has_any({"Wall Kick", "Triple Jump", "Backflip", "Side Flip"}, player))
        add_rule(world.get_location("WDW: Secrets in the Shallows & Sky", player), lambda state: state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
        # Area randomizer dramatically affects rules for reaching downtown in Wet-Dry World
        set_rule(world.get_location("WDW: Go to Town for Red Coins", player),
                 lambda state: can_reach_wdw_downtown(state) and state.has_all({"Ledge Grab", "Wall Kick"}, player))
        set_rule(world.get_location("WDW: Quick Race Through Downtown!", player),
                 lambda state: can_reach_wdw_downtown(state) and state.has_all({"Ledge Grab", "Wall Kick"}, player))
        add_rule(world.get_location("WDW: Bob-omb Buddy", player),
                 lambda state: state.has("Triple Jump", player) or state.has_all({"Side Flip", "Ledge Grab"}, player))
        add_rule(world.get_location("WDW: 1Up Block in Downtown", player), lambda state: can_reach_wdw_downtown(state))
        # Tall, Tall Mountain
        add_rule(world.get_location("TTM: Scale the Mountain", player), lambda state: state.has_any({"Long Jump", "Dive"}, player))
        add_rule(world.get_location("TTM: Mystery of the Monkey Cage", player), lambda state: state.has_any({"Long Jump", "Dive"}, player))
        add_rule(world.get_location("TTM: Scary 'Shrooms, Red Coins", player), lambda state: state.has_any({"Long Jump", "Dive", "Ledge Grab", "Triple Jump"}, player))
        add_rule(world.get_location("TTM: Mysterious Mountainside", player), lambda state: state.has_any({"Long Jump", "Dive"}, player))
        add_rule(world.get_location("TTM: Breathtaking View from Bridge", player), lambda state: state.has_any({"Long Jump", "Dive"}, player))
        add_rule(world.get_location("TTM: Blast to the Lonely Mushroom", player), lambda state: state.has("Long Jump", player))
        add_rule(world.get_location("TTM: Bob-omb Buddy", player), lambda state: state.has_any({"Long Jump", "Dive", "Ledge Grab", "Triple Jump"}, player))
        add_rule(world.get_location("TTM: 1Up Block on Red Mushroom", player), lambda state: state.has_any({"Long Jump", "Dive", "Ledge Grab", "Triple Jump"}, player))
        # Tiny-Huge Island
        add_rule(world.get_location("THI: Pluck the Piranha Flower", player), lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("THI: The Tip Top of the Huge Island", player),
                 lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player) and state.has_any({"Backflip", "Side Flip", "Triple Jump"}, player))
        add_rule(world.get_location("THI: Rematch with Koopa the Quick", player), lambda state: state.has("Long Jump", player))
        add_rule(world.get_location("THI: Five Itty Bitty Secrets", player), lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("THI: Wiggler's Red Coins", player),
                 lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player) and state.has("Wall Kick", player))
        add_rule(world.get_location("THI: Make Wiggler Squirm", player),
                 lambda state: (state.has_all({"Ledge Grab", "Wall Kick"}, player)
                                or state.has_any({"Long Jump", "Ledge Grab"}, player)and state.has_any({"Backflip", "Side Flip", "Triple Jump"}, player))
                                and state.has("Ground Pound", player))
        add_rule(world.get_location("THI: Bob-omb Buddy", player), lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("THI: 1Up Block THI Large near Start", player), lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player))
        add_rule(world.get_location("THI: 1Up Block Windy Area", player), lambda state: state.has_any({"Long Jump", "Ledge Grab"}, player))
        # Tick Tock Clock
        add_rule(world.get_location("TTC: Roll into the Cage", player),
                 lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Side Flip", "Backflip", "Wall Kick"}, player))
        add_rule(world.get_location("TTC: The Pit and the Pendulums", player),
                 lambda state: state.has_all({"Ledge Grab", "Climb"}, player))
        add_rule(world.get_location("TTC: Get a Hand", player),
                 lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Side Flip", "Backflip", "Wall Kick"}, player))
        add_rule(world.get_location("TTC: Stomp on the Thwomp", player),
                 lambda state: state.has("Ledge Grab", player) and state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
        add_rule(world.get_location("TTC: Timed Jumps on Moving Bars", player),
                 lambda state: state.has("Ledge Grab", player) and state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
        add_rule(world.get_location("TTC: 1Up Block Midway Up", player),
                 lambda state: state.has("Ledge Grab", player) and state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
        add_rule(world.get_location("TTC: 1Up Block at the Top", player),
                 lambda state: state.has("Ledge Grab", player) and state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
        # Rainbow Ride
        add_rule(world.get_location("RR: Cruiser Crossing the Rainbow", player), lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Side Flip", "Backflip"}, player))
        add_rule(world.get_location("RR: The Big House in the Sky", player), lambda state: state.has_any({"Side Flip", "Backflip", "Ledge Grab"}, player))
        add_rule(world.get_location("RR: Coins Amassed in a Maze", player), lambda state: state.has("Wall Kick", player))
        add_rule(world.get_location("RR: Somewhere Over the Rainbow", player),
                 lambda state: state.has_any({"Ledge Grab", "Triple Jump", "Side Flip", "Backflip"}, player) and state.has("Climb", player))
        add_rule(world.get_location("RR: Bob-omb Buddy", player), lambda state: state.has("Wall Kick", player))
        add_rule(world.get_location("RR: 1Up Block On House in the Sky", player), lambda state: state.has_any({"Side Flip", "Backflip", "Ledge Grab"}, player))
        # Bowser
        add_rule(world.get_location("Bowser in the Fire Sea Red Coins", player),
                 lambda state: state.has("Climb", player) and state.has_any({"Triple Jump", "Wall Kick", "Backflip", "Side Flip", "Kick"}, player))
        add_rule(world.get_location("Bowser in the Fire Sea Key", player), lambda state: state.has("Climb", player))
        add_rule(world.get_location("Bowser in the Fire Sea 1Up Block Swaying Stairs", player), lambda state: state.has("Climb", player))
        add_rule(world.get_location("Bowser in the Fire Sea 1Up Block Near Poles", player),
                 lambda state: state.has("Climb", player) and state.has_any({"Ledge Grab", "Wall Kick"}, player))
        add_rule(world.get_location("Bowser in the Sky Red Coins", player),
                 lambda state: state.has("Climb", player) and (state.has("Triple Jump", player) or state.has_all({"Side Flip", "Ledge Grab"}, player)))

        # Others
        add_rule(world.get_location("Vanish Cap Under the Moat Red Coins", player),
                 lambda state: state.has_any({"Triple Jump", "Side Flip", "Backflip", "Ledge Grab"}, player) and (
                     state.has("Vanish Cap", player) or
                     not world.StrictCapRequirements[player] and state.has("Wall Kick"), player))
        if world.EnableCoinStars[player]:
            add_rule(world.get_location("BoB: 100 Coins", player), lambda state: can_reach_bob_island(state))
            add_rule(world.get_location("JRB: 100 Coins", player),
                     lambda state: state.has("Ground Pound", player) and state.has_any({"Triple Jump", "Backflip", "Side Flip"}, player))
            add_rule(world.get_location("BBH: 100 Coins", player),
                     lambda state: state.has_any({"Ground Pound", "Kick"}, player) and (state.has("Wall Kick", player) or state.has_all({"Triple Jump", "Ledge Grab"}, player)))
            add_rule(world.get_location("HMC: 100 Coins", player), lambda state: state.has_all({"Climb", "Triple Jump", "Ground Pound"}, player))
            add_rule(world.get_location("DDD: 100 Coins", player), lambda state: state.has_all({"Climb", "Ground Pound"}, player))
            add_rule(world.get_location("WDW: 100 Coins", player),
                     lambda state: state.has("Ground Pound", player) and state.has_any({"Wall Kick", "Triple Jump", "Side Flip", "Backflip"}, player))
            add_rule(world.get_location("TTM: 100 Coins", player), lambda state: state.has_any({"Long Jump", "Dive"}, player))
            add_rule(world.get_location("TTC: 100 Coins", player),
                     lambda state: state.has("Ledge Grab", player) and state.has_any({"Triple Jump", "Side Flip", "Backflip"}, player))
            add_rule(world.get_location("RR: 100 Coins", player),
                     lambda state: state.has_all({"Wall Kick", "Ground Pound"}, player) and state.has_any({"Ledge Grab", "Side Flip", "Backflip"}, player))

        if world.StrictMoveRequirements[player]:
            # Techniques used to ignore requirement are provided by comment
            add_rule(world.get_location("BoB: Behind Chain Chomp's Gate", player), lambda state: state.has("Ground Pound", player))  # Bomb Clip
            set_rule(world.get_location("WF: Shoot into the Wild Blue", player),
                     lambda state: state.has("Wall Kick", player) and state.has_any({"Triple Jump", "Side Flip"}, player) or state.has_all({"Cannon Unlock WF", "Climb"}, player)) # Backwards air kick
            add_rule(world.get_location("CCM: Wall Kicks Will Work", player),
                     lambda state: state.has("Triple Jump", player) or state.has("Wall Kick", player) and state.has_any(
                         {"Backflip", "Long Jump", "Side Flip", "Dive"}, player))
            add_rule(world.get_location("BBH: Big Boo's Balcony", player), lambda state: state.has("Long Jump", player))  # Can get on manor roof with specific jumps
            add_rule(world.get_location("BBH: 1Up Block Top of Mansion", player), lambda state: state.has("Long Jump", player))  # Can get on manor roof with specific jumps
            add_rule(world.get_location("HMC: Swimming Beast in the Cavern", player), lambda state: state.has("Ground Pound", player))  # Jump up Nessie's neck
            set_rule(world.get_location("HMC: A-Maze-Ing Emergency Exit", player), lambda state: state.has_all({"Triple Jump", "Climb"}, player))
            add_rule(world.get_location("SSL: Inside the Ancient Pyramid", player),
                     lambda state: state.has("Climb", player) and state.has_any({"Triple Jump", "Backflip", "Side Flip", "Ledge Grab"}, player))  # Enter from top of pyramid
            add_rule(world.get_location("SSL: Pyramid Puzzle", player),
                     lambda state: state.has("Climb", player) and state.has_any({"Triple Jump", "Backflip", "Side Flip", "Ledge Grab"}, player))  # Enter from top of pyramid
            set_rule(world.get_location("SL: In the Deep Freeze", player), lambda state: state.has_any({"Backflip", "Side Flip", "Wall Kick"}, player))
            add_rule(world.get_location("Vanish Cap Under the Moat Switch", player),
                     lambda state: state.has_any({"Wall Kick", "Triple Jump", "Side Flip", "Backflip", "Ledge Grab"}, player))
            if world.EnableCoinStars[player]:
                add_rule(world.get_location("JRB: 100 Coins", player), lambda state: state.has("Climb", player))  # Brings available coin count from 102 to 104
                add_rule(world.get_location("WF: 100 Coins", player), lambda state: state.has("Ground Pound", player))  # Stomp on Whomps for coins
                add_rule(world.get_location("SL: 100 Coins", player), lambda state: state.has("Vanish Cap", player))  # Compensates for coin gathering difficulty with reduced moves

    #Rules for Secret Stars
    add_rule(world.get_location("Wing Mario Over the Rainbow Red Coins", player), lambda state: state.has("Wing Cap", player))
    add_rule(world.get_location("Wing Mario Over the Rainbow 1Up Block", player), lambda state: state.has("Wing Cap", player))
    add_rule(world.get_location("Toad (Basement)", player), lambda state: state.can_reach("Basement", 'Region', player) and state.has("Power Star", player, 12))
    add_rule(world.get_location("Toad (Second Floor)", player), lambda state: state.can_reach("Second Floor", 'Region', player) and state.has("Power Star", player, 25))
    add_rule(world.get_location("Toad (Third Floor)", player), lambda state: state.can_reach("Third Floor", 'Region', player) and state.has("Power Star", player, 35))

    if world.MIPS1Cost[player].value > world.MIPS2Cost[player].value:
        (world.MIPS2Cost[player].value, world.MIPS1Cost[player].value) = (world.MIPS1Cost[player].value, world.MIPS2Cost[player].value)
    add_rule(world.get_location("MIPS 1", player), lambda state: state.can_reach("Basement", 'Region', player) and state.has("Power Star", player, world.MIPS1Cost[player].value))
    add_rule(world.get_location("MIPS 2", player), lambda state: state.can_reach("Basement", 'Region', player) and state.has("Power Star", player, world.MIPS2Cost[player].value))

    world.completion_condition[player] = lambda state: state.can_reach("Bowser in the Sky", 'Region', player) \
        and (not world.RandomizeMoves[player]
             or state.has("Climb", player) and (state.has("Triple Jump", player) or state.has_all({"Side Flip", "Ledge Grab"}, player)))

