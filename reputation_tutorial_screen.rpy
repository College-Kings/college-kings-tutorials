screen reputation_tutorial():
    zorder 200
    style_prefix "tutorial"

    default page_number = 1
    default tutorial = (
        "{u}EARNING POINTS{/u}\nYour decisions strongly influence how the story progresses and how other characters perceive you.",
        "With each choice, you'll either gain Bro, Boyfriend, or Troublemaker points.",
        "Bros are friends first and foremost, boyfriends are sensible supporters of those close to them, and troublemakers seek thrills and take risks.",
        "These points are then used to identify your reputation. Each reputation will unlock different possibilities and choices, but you can only have one active at a time.",
        "{u}DECISIONS{/u}\nWhen people make important decisions on how they feel about you, they consider what kind of person you are.",
        "Your Key Character Trait (Loyal, Popular, or Confident) has a strong influence on how other characters react to your behavior.",
        "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence.",
        "Your decisions matter and have long term effects, so think about what kind of person you want to be.",
    )

    vbox:
        pos (1180, 500)

        button:
            xysize (740, 270)
            background "tutorial_background"
            action Show("confirm", message="Are you sure you want to hide the tutorial?", yes_action=[Hide("confirm"), AddToSet(persistent.hidden_tutorials, "reputation_tutorial")])

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

