screen phone_tutorial():
    zorder 200
    style_prefix "tutorial"

    default image_path = "gui/tutorial/"
    default page_number = 1
    default tutorial = (
        "This is your phone. You can access it whenever the phone icon appears in the top right corner.",
        "New notifications are typically accompanied by a buzzing sound. Currently, you have a new message waiting for you.",
        "How you reply to messages matters just as much as any other decision."
    )

    vbox:
        ypos 75

        button:
            xysize (740, 270)
            background "tutorial_background"
            action Show("confirm", message="Are you sure you want to hide the tutorial?", yes_action=[Hide("confirm"), AddToSet(persistent.hidden_tutorials, "phone_tutorial")])

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