# Var definitions
# Characters
define player = Character('[povname]', color='#2992e3')

# Backgrounds
image bg classroom = 'bg/classroom-1080.png'
image bg food_court = 'bg/food_court-1080.png'

# Music
define start = 'music/peace.ogg'
define investigation = 'music/detective_theme.ogg'


screen food_court_objects:
    imagemap:
        ground 'bg/food_court-1080.png'
        hover 'bg/food_court-hover-1080.png'

        hotspot(212, 676, 740, 401) clicked Return('discarded')
        hotspot(159, 432, 113, 241) clicked Return('chocolate')
        hotspot(833, 424, 149, 167) clicked Return('ice_cream')
        hotspot(976, 299, 170, 186) clicked Return('takoyaki')
        hotspot(1339, 311, 135, 222) clicked Return('udon')
        hotspot(1480, 311, 281, 232) clicked Return('hk')
        hotspot(1727, 471, 186, 131) clicked Return('couple')


label start:
    # Start in classroom
    scene bg classroom
    # Play start music
    play music start

    # Ask player to name character
    python:
        povname = renpy.input('What\'s your name?').strip()
        if not povname:
            povname = 'Kaede'

    # alert player of scene change
    player 'Now that class is over, I better get right to investigating.'

    label investigation:
        scene bg food_court
        play music investigation

        player 'Now let\'s see here...'

        while True:
            call screen food_court_objects
            $ result = _return
            if result == 'discarded':
                player 'There seems to be a table left behind by two people.'
                player 'One of them has a still-wrapped burger on their tray, whereas the other only has a drink.'
                player 'Perhaps they went to the bathroom.'
            elif result == 'chocolate':
                player 'What looks like a mother and child are ordering something at the popular Musha Musha confectionary shop.'
                player 'As can be seen with its large size, they\'ve been popular for years and still get lots of business'
                player 'compared to other shops here...'
            elif result == 'ice_cream':
                player 'Classic Baskin Ribbons, huh.'
                player 'Old reliable ice cream you can get all over the country.'
                player 'But I think the American Bob & Jenkin\'s are better.'
                player 'Man! I miss them now...'
            elif result == 'takoyaki':
                player 'This restaurant used to really popular until that new Hong Kong street food restaurant came in.'
                player 'Their octopus (tako) and pollock roe (mentaiko) dishes are to die for tho...'
                player 'I should get some takoyaki and mentaiko pasta before I head out...'
            elif result == 'udon':
                player 'This restaurant probably has the best udon in town and their cheap under ¥300 prices make them very popular with schoolkids.'
            elif result == 'hk':
                player 'This Hong Kong street food, or dim sum, restaurant only came in like a month ago when school began.'
                player 'I don\'t think their fish balls ar better than our homegrown takoyaki, but I like having them with curry.'
                player 'Their siu mai dumplings and waffle dishes are really good tho.'
                player 'I should order some before I head out...'
            elif result == 'couple':
                player 'Those two closer to the dim sum restaurant...'
                player 'I wonder if they\'re a couple...'
                player 'They don\'t look lost in love like some couples in my class, but perhaps they\'re really comfortable with each other.'
                player 'It could also be that there\'s some kind of fight between the two of them'
                player 'Maybe I\'ll eavesdrop while I eat...'
