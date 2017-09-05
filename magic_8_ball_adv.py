import random, sys, arcade


def draw_eight_ball(position_x, position_y):
    """
    This function draws a magic 8 ball.
    """

    # Draw a black circle with a white triangle inside it
    arcade.draw_circle_filled(center_x=position_x,
                              center_y=position_y,
                              radius=300,
                              color=arcade.color.BLACK)
    arcade.draw_triangle_filled(position_x - 200, position_y - 150,
                                position_x + 200, position_y - 150,
                                position_x, position_y + 200,
                                arcade.color.WHITE)


def answer_1():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('NO', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)
    arcade.finish_render()
    arcade.run()


def answer_2():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('Yasssss', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)

    arcade.finish_render()
    arcade.run()


def answer_3():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('ummmmmm maybe?', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)

    arcade.finish_render()
    arcade.run()


def answer_4():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('idk tbqh', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)

    arcade.finish_render()
    arcade.run()


def answer_5():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('definitely', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)

    arcade.finish_render()
    arcade.run()


def answer_6():
    arcade.open_window(800, 600, "Magic 8 Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    draw_eight_ball(400, 300)
    arcade.render_text(text=arcade.create_text('ask me tomorrow', arcade.color.BLACK),
                       start_x=350,
                       start_y=300,
                       rotation=0)

    arcade.finish_render()
    arcade.run()


ans = True

while ans:
    question = input("Ask a question…if you dare")

    answers = random.randint(1, 6)

    if question == "q":
        sys.exit()

    elif answers == 1:
        answer_1()

    elif answers == 2:
        answer_2()

    elif answers == 3:
        answer_3()

    elif answers == 4:
        answer_4()

    elif answers == 5:
        answer_5()

    elif answers == 6:
        answer_6()
