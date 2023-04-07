# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define byakuya = Character('Byakuya Togami', color='#e38929')
define shuichi = Character('Shuichi Saihara', color='#2992e3')

# Declare background
image bg gym = im.FactorScale('backgrounds/gym.png', 2)

# Declare character sprites
image byakuya command = im.FactorScale('characters/byakuya/command.png', 1.5)
image byakuya leave = im.FactorScale('characters/byakuya/leave.png', 1.5)
image byakuya mock = im.FactorScale('characters/byakuya/mock.png', 1.5)
image byakuya neutral = im.FactorScale('characters/byakuya/neutral.png', 1.5)
image byakuya shock = im.FactorScale('characters/byakuya/shock.png', 1.5)
image byakuya smirk = im.FactorScale('characters/byakuya/smirk.png', 1.5)
image byakuya think = im.FactorScale('characters/byakuya/think.png', 1.5)

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg gym

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show byakuya neutral

    # Play music
    play music 'audio/music/despair_searching.ogg'

    play sound 'audio/sfx/byakuya/out_with_it.ogg'
    byakuya 'All right. Let us go over the case form the beginning.'
    label weapon:
        show byakuya neutral
        byakuya 'What as the weapon used in the murder?'
        menu:
            'A knife':
                jump knife
            'A sledgehammer':
                jump sledgehammer
        label knife:
            shuichi 'They used a knife.'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            byakuya 'Correct.'
            byakuya 'The culprit stabbed the victim once she was cornered in the bathroom.'
            jump location
        label sledgehammer:
            shuichi 'They used a sledgehammer.'
            show byakuya mock
            play sound 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'I was a fool to name you my servant...'
            byakuya 'Try. Again.'
            jump weapon
    label location:
        show byakuya neutral
        byakuya 'Where was the murder committed?'
        menu:
            'Sayaka Maizono\'s room':
                jump sayaka
            'Makoto Naegi\'s room':
                jump makoto
        label sayaka:
            shuichi 'In Sayaka Maizono\'s room.'
            show byakuya mock
            play sound 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'I was a fool to name you my servant...'
            byakuya 'Try. Again.'
            jump location
        label makoto:
            shuichi 'In Makoto Naegi\'s room'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            byakuya 'Indeed.'
            jump location_evidence
    label location_evidence:
        show byakuya neutral
        byakuya 'How do we know that is the case?'
        menu:
            'The rooms\' nameplates were swapped':
                jump swapped
            'There was evidence of a struggle':
                jump struggle
        label swapped:
            shuichi 'The nameplates on the doors of both rooms were swapped.'
            shuichi 'The victim and Makoto Naegi switched rooms for the night, which the victim used as an opportunity to switch the nameplates around and lure Leon Kuwata to what he thought was her room.'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            byakuya 'Well done, my servant.'
            jump motive
        label struggle:
            shuichi 'There was evidence of a struggle in the room.'
            show byakuya mock
            play sound 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'That tells us nothing!'
            byakuya 'Try. Again.'
            jump location_evidence
    label motive:
        show byakuya neutral
        byakuya 'Did the culprit plan to murder the victim?'
        menu:
            'Yes':
                jump planned
            'No':
                jump accident
        label planned:
            shuichi 'Of course.'
            show byakuya mock
            play sound 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'I was a fool to name you my servant...'
            byakuya 'Try. Again.'
            jump motive
        label accident:
            shuichi 'No... It was all an accident...'
            shuichi 'The victim planned to lure the culprit to her room, and murder him...'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            byakuya 'Corect, once again.'
            jump message
    label message:
        show byakuya neutral
        byakuya 'Why do we know Leon Kuwata is the culprit?'
        menu:
            'The vitim left a message in blood.':
                jump blood
            'Wait...he is...??':
                jump confused
        label blood:
            shuichi 'The victim left a message in...her own blood with the last of her strength...'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            jump message_content
        label confused:
            shuichi 'Wait...he is...???'
            show byakuya mock
            play sound 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'I was a fool to name you my servant...'
            byakuya 'Try. Again.'
            jump message
    label message_content:
        show byakuya neutral
        byakuya 'What did the message say?'
        menu:
            '11037':
                jump numbers
            'LEON':
                jump leon
        label numbers:
            shuichi 'She simply wrote the numbers "11037".'
            show byakuya mock
            play voice 'audio/sfx/byakuya/such_ignorance.ogg'
            byakuya 'I was a fool to name you my servant...'
            byakuya 'Try. Again.'
            jump message_content
        label leon:
            shuichi 'While it seems like the numbers "11037", if you were to flip it upside down, you\'d see that it spells out "LEON".'
            play sound 'audio/sfx/general/got_it.ogg'
            shuichi 'Daming evidence that Leon Kuwata is the culprit!'
            show byakuya smirk
            play sound 'audio/sfx/byakuya/naturally.ogg'
            byakuya 'Daming evidence indeed!'
            jump end
    label end:
        show byakuya leave
        play sound 'audio/sfx/byakuya/lets_go.ogg'
        byakuya 'Let\'s go. Monokuma will begin the class trial soon.'
        shuichi 'Right.'

    # This ends the game.
    return
