screen presidency_tutorial():
    zorder 200
    style_prefix "tutorial"

    default page_number = 1
    default tutorial = (
        "With Chloe and Lindsey competing against each other for one of the most influential positions at San Vallejo, it's up to you to pick sides. Campaign planning unlocks a large amount of opportunities that you don't want to miss out on!",
        "Will you help Chloe, or Lindsey? Or will you even dare to secretly campaign for both at the same time? The potential gratitude of both girls may be huge, but you better not get caught.",
        "When planning a campaign, you get to make the big decisions. Both campaigns are divided into different phases and for each phase you will have multiple approaches with a variety of options on how to execute those approaches.",
        "Will you play dirty or stay clean? Will you try to make deals with the Wolves, or the Apes? Will you persuade people with expensive limos and alcohol, or by ruining the other candidate's reputation? The choice is yours.",
        "Every presidency related action, from executing your big campaign plan, to making a bad joke about one of the candidates, impacts the candidates' popularity, which plays a big role in who's going to be elected.",
        "But beware, just because you intended to help one candidate, doesn't mean that you'll succeed. Playing too dirty may cause backlash and even the best plans can fail. The stakes have never been higher."
    )

    vbox:
        align (1.0, 0.5)

        button:
            xysize (740, 270)
            background "tutorial_background"
            action Show("confirm", message="Are you sure you want to hide the tutorial?", yes_action=[SetDict(persistent.enabled_tutorials, "fight_preparation_tutorial", False), Hide("presidency_tutorial")])

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
