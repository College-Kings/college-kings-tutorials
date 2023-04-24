screen fight_tutorial():
    zorder 200
    style_prefix "tutorial"

    default page_number = 1
    default tutorials = (
        ("{u}FIGHT OVERVIEW:{/u}\n During a fight, you and your opponent alternate attacking turns during which you can do damage to each other.", (20, 300)),
        ("{u}FIGHT OVERVIEW:{/u}\n Your goal should be to get your opponent's health bar to zero, before they do the same to yours.", (20, 300)),
        ("{u}ATTACKING:{/u}\n Each turn you get 8 stamina points, shown in blue in the bottom left. (Some actions can increase or decrease your starting stamina)", (20, 550)),
        ("{u}ATTACKING:{/u}\n Every action requires a certain amount of stamina, shown by the blue dots inside the action button.", (20, 550)),
        ("{u}ATTACKING:{/u}\n In order to damage your opponent's health (red), you first have to destroy their guard (blue).", (20, 550)),
        ("{u}ATTACKING:{/u}\n Your turn ends when you run out of stamina or select a turn-ending action.", (20, 550)),
        ("{u}ATTACKING:{/u}\n Clicking on an action shows you a detailed description of what the action does (for example how much damage for attacks)", (20, 550)),
        ("{u}STANCES:{/u}\n Throughout a fight, you'll rotate between four different stances: Aggressive, Forward, Solid and Defensive.", (600, 150)),
        ("{u}STANCES:{/u}\n You can see your current stance at the top. The more left your stance, the more offensively you're positioned. Generally that means you deal and take more damage.", (600, 150)),
        ("{u}STANCES:{/u}\n Each action has an ideal stance. If you do an action from its ideal stance, it'll have a bonus effect. Ideal actions for your current stance are highlighted in green. ", (600, 150)),
        ("{u}STANCES:{/u}\n You can also see each action's ideal stance by selecting the action and looking at the stance bar at the top.", (600, 150)),
        ("{u}STANCES:{/u}\n Each action also has an end stance, which is the stance you'll be in after taking the action.", (600, 150)),
        ("{u}STANCES:{/u}\n The most crucial stance is the one you end your turn on, as more offensive stances leave you vulnerable to your opponent's attacks, whereas more defensive poses slow down your next attacking turn.", (600, 150)),
        ("{u}HEALTH:{/u}\n Your health bar is shown in the top left in red. The blue bar above is your guard.", (20, 150)),
        ("{u}HEALTH:{/u}\n Your guard acts as a buffer during your opponent's attacking turn. The only way for them to damage your health is to break your guard first.", (20, 150)),
        ("{u}HEALTH:{/u}\n Your guard amount is directly determined by your stance at the end of your turn.", (20, 150)),
        ("{u}TIPS:{/u}\n Your opponent learns the way you play and adjusts their moves accordingly, if you become too predictable, you will lose.", (20, 300)),
        ("{u}TIPS:{/u}\n Just because an action is highlighted in green, doesn't mean it's the best possible move for your current situation, always think about the next stance.", (20, 300)),
        ("{u}TIPS:{/u}\n Try out different special attacks and quirks to see which ones you like the most, they can drastically alter your playstyle.", (20, 300)),
    )

    $ tutorial = tutorials[page_number]

    vbox:
        pos tutorial[1]

        button:
            xysize (740, 270)
            background "tutorial_background"
            action Show("confirm", message="Are you sure you want to hide the tutorial?", yes_action=[Hide("confirm"), AddToSet(persistent.hidden_tutorials, "fight_tutorial")])

            frame:
                ysize 220
                ypos 42

                text tutorial[0] xsize 595 align (0.5, 0.5)

                imagebutton:
                    yalign 0.5
                    idle "tutorial_left_button_idle"
                    hover "tutorial_left_button_hover"
                    if page_number > 1:
                        action SetScreenVariable("page_number", page_number - 1)
                    else:
                        action SetScreenVariable("page_number", len(tutorials))

                imagebutton:
                    align (1.0, 0.5)
                    idle "tutorial_right_button_idle"
                    hover "tutorial_right_button_hover"
                    if page_number < len(tutorials):
                        action SetScreenVariable("page_number", page_number + 1)
                    else:
                        action SetScreenVariable("page_number", 1)

                text "{} of {}".format(page_number, len(tutorials)) style "tutorial_page_number" align (0.5, 1.0) yoffset -10

        text "Click on the tutorial box to hide this tutorial." xalign 0.5

