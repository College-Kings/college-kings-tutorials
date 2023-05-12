screen fight_preparation_tutorial():
    zorder 200
    style_prefix "tutorial"

    default page_number = 1
    default tutorial = (
        "{u}FIGHT PREPARATION:{/u}\n College Kings 2 fights are turn-based instead of reaction-time-based with a strong emphasis on strategy and customization.",
        "{u}FIGHT PREPARATION:{/u}\n Every fighter shares the same four basic attacks, which set the foundation for fighting.",
        "{u}FIGHT PREPARATION:{/u}\n Before each fight, you'll also be able to select a special attack and quirk to customize your fighting style.",
        "{u}FIGHT PREPARATION:{/u}\n Simply hover over an attack to learn more about it.",
        "{u}FIGHT PREPARATION:{/u}\n You can also preview your opponents fighting style and possible strengths and weaknesses.",
        "{u}FIGHT PREPARATION:{/u}\n Select your special attack, quirk and difficulty and then click play fight to start.",
    )

    vbox:
        pos (1150, 730)

        button:
            xysize (740, 270)
            background "tutorial_background"
            action Show("confirm", message="Are you sure you want to hide the tutorial?", yes_action=[SetDict(persistent.enabled_tutorials, "fight_preparation_tutorial", False), Hide("fight_preparation_tutorial")])

            frame:
                ysize 220
                ypos 42

                text tutorial[page_number - 1] xsize 595 align (0.5, 0.5)

                imagebutton:
                    yalign 0.5
                    idle "tutorial_left_button_idle"
                    hover "tutorial_left_button_hover"
                    if page_number > 1:
                        action SetScreenVariable("page_number", page_number - 1)
                    else:
                        action SetScreenVariable("page_number", len(tutorial))

                imagebutton:
                    align (1.0, 0.5)
                    idle "tutorial_right_button_idle"
                    hover "tutorial_right_button_hover"
                    if page_number < len(tutorial):
                        action SetScreenVariable("page_number", page_number + 1)
                    else:
                        action SetScreenVariable("page_number", 1)

                text "{} of {}".format(page_number, len(tutorial)) style "tutorial_page_number" align (0.5, 1.0) yoffset -10

        text "Click on the tutorial box to hide this tutorial." xalign 0.5

