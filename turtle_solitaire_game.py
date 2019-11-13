from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)



# Functions for Creating the Drawing Canvas

def create_drawing_canvas(show_axes: object = True) -> object:
    """

    :rtype: object
    """
    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

# Test Data for Use During Code Development

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#

def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game


# Game design:
# Hide turtle as it appears when canvas and coordinates are set to 'False'
hideturtle()

# Set locations for starting point of cards (top left side of card for start point),
# these are the ones set on program drawing but -75 on x axis.
location_start = [[-512, 375], [-333, 375], [-154, 375], [26, 375], [205, 375], [384, 375]]

# Set card parameters:
# Change size to change card size.
size = 10 # Use only even numbers

# Card parameters
card_width = (size*12.6)
card_height = (size*20)
radius = (size/2)
angle = 180
length = size



# The next following block of #commented# code (line 400 to line 421) was how I initially wanted to
# write the card number/identifier on the card. It worked perfectly except using 'choice' (and 'randint' and 'sample')
# would return duplicate card numbers sometimes, so I had to write the y axis coordinates as a card number instead

# Set up a list with all card letters and numbers that you want written in cards
#card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#
# Write definition for card identifier(letter/number) on top left of card and bottom right of card.
#def card_identifier():
#    # Following is to draw card number/id on top left side of card:
#    x_number = (xcor())
#    y_number = (ycor())
#    goto(xcor() + ((length / 10) * 7), ycor() + (length * 2.5))
#    pendown()
#    numbers = choice(card_numbers)
#    for draw_number in range(max_cards):
#        write(numbers, font=('Arial', (int(length * 1.8))))
#        penup()
#    # Following is to draw card number/id on bottom right side of card:
#    goto(xcor() + (length * 10.5), ycor() - (length * 15.5))
#    pendown()
#    for draw_number in range(max_cards):
#        write_upside_down(numbers, font=('Arial', (int(length * 1.8))))
#        penup()
#    # Return to card_identifier start point:
#    goto(x_number, y_number)



# Write definition for card identifier(letter/number) on top left of card and bottom right of card.
def card_identifier():
    # Following is to draw card number/id on top left side of card:
    x_number = (xcor())
    y_number = (ycor())
    # Move position ready to write card number:
    goto(xcor() + ((length/10)*7), ycor() + (length*2.4))
    pendown()
    for draw_number in range(max_cards):
        write(int(ycor()/10), font=('Arial', (int(length*1.8))))
        penup()

    # Following is to draw card number/id on bottom right side of card:
    # Move position ready to write card number:
    goto(xcor() + (length*10.5), ycor() - (length*15.5))
    pendown()
    for draw_number in range(max_cards):
        write_upside_down((int(y_number/10)+int(length/5)), font=('Arial', (int(length*1.8))))
        penup()
    # Return to card_identifier start point:
    goto(x_number, y_number)

# Set up and define card drawings:
# Suit_1 is for the orange card.
def Suit_1():
    color("black", "white")
    pendown()
    begin_fill()
    x_orange_point = (xcor())
    y_orange_point = (ycor() - (length*6))
    setheading(0)
    # Draw card
    for draw_card in range(2):
        forward(card_width)
        circle(-radius, angle/2)
        forward(card_height)
        circle(-radius, angle/2)
    penup()
    end_fill()
    setheading(0)
    forward(card_width/2)
    right(angle/2)
    forward(card_height/3)
    setheading(0)
    x_orange = (xcor())
    y_orange = (ycor())
    right(angle/2)
    forward(length*5)
    setheading(0)

    # Define and draw orange fruit
    def orange_fruit():
        goto(x_orange, y_orange + (length*2))
        pendown()
        color("black", "orange")
        begin_fill()
        circle(-radius*11, angle*2)
        end_fill()
        penup()
        right(angle/2)
        forward(length*5)
        setheading(0)

    # Define and draw leaves
    def orange_leaves():
        goto(x_orange, y_orange + (length*2))
        color("black", "green")
        begin_fill()
        circle(radius*9, - angle/4)
        right((angle/3)*2)
        circle(radius*9, - angle/4)
        left(angle/3)
        circle(radius*9, - angle/4)
        right((angle/3) *2)
        circle(radius*9, - angle/4)
        end_fill()
    orange_fruit()
    orange_leaves()
    penup()
    goto(x_orange_point, y_orange_point)
    # Draw card number/id and got to start Suit_1 starting point
    card_identifier()
    goto(x_orange_point, y_orange_point)

# Suit_2 is for watermelon card
def Suit_2():
    color("black", "white")
    pendown()
    begin_fill()
    x_watermelon_point = (xcor())
    y_watermelon_point = (ycor() - (length*6))
    setheading(0)
    pendown()
    # Draw card
    for draw_card in range(2):
        forward(card_width)
        circle(-radius, angle/2)
        forward(card_height)
        circle(-radius, angle/2)
    penup()
    end_fill()
    setheading(0)
    forward(card_width/3)
    right(angle/2)
    forward(card_height/2)
    setheading(0)
    x_watermelon = (xcor())
    y_watermelon = (ycor())

    def watermelon_skin():
        # Draw watermelon skin
        goto(x_watermelon, y_watermelon)
        color("black", "green")
        begin_fill()
        pendown()
        left((angle/18)*7)
        forward((length*7.5))
        right(angle/2)
        circle(-(length*7.5), angle)
        right(angle/2)
        forward((length*7.5))
        end_fill()
        penup()

    def watermelon_fruit():
        # Draw watermelon fruit(the red part)
        color("black", "orange red")
        begin_fill()
        pendown()
        forward(length*6.5)
        right(angle/2)
        circle(-(length*6.5), angle)
        right(angle/2)
        forward(length*6.5)
        end_fill()
        penup()

    def watermelon_seeds():
        # Draw watermelon seeds
        color("black")
        turtlesize((length/100), (length/40))
        for seeds in range(50):
            goto(x_watermelon, y_watermelon)
            setheading(randint(-(length*11), (angle/18)*7))
            forward(randint((length*1.5), angle/3))
            stamp()
    watermelon_skin()
    watermelon_fruit()
    watermelon_seeds()
    goto(x_watermelon_point, y_watermelon_point)
    #Draw card number/id and got to start Suit_2 starting point
    card_identifier()
    goto(x_watermelon_point, y_watermelon_point)

# Suit_3 is for strawberry card
def Suit_3():
    color("black", "white")
    pendown()
    begin_fill()
    setheading(0)
    x_strawberry_point = (xcor())
    y_strawberry_point = (ycor() - (length*6))
    setheading(0)
    pendown()
    # Draw card
    for draw_card in range(2):
        forward(card_width)
        circle(-radius, angle/2)
        forward(card_height)
        circle(-radius, angle/2)
    penup()
    end_fill()
    setheading(0)
    forward(card_width/2.7)
    right(angle/2)
    forward(card_height/3.5)
    setheading(0)
    x_strawberry = (xcor())
    y_strawberry = (ycor())

    def strawberry_fruit():
        # Draw strawberry shape and colour in red
        pendown()
        color("black", "crimson")
        begin_fill()
        forward(length*4)
        circle(-(length*2),(angle/18)*11)
        forward(length*8)
        circle(-(length*2),(angle/9)*7)
        forward(length*8)
        circle(-(length*2),(angle/18)*11)
        forward(length*4)
        end_fill()
        penup()

    def strawberry_stem():
        # Draw strawberry stem
        pendown()
        color("black", "green")
        begin_fill()
        left(angle/7)
        forward(length*3)
        left((angle/7)*6)
        forward(length*3)
        right((angle/18)*11)
        forward(length*3)
        left((angle/9)*8)
        forward(length*3)
        right((angle/18)*11)
        forward(length*3)
        left((angle/9)*8)
        forward(length*3.36)
        right((angle/9)*5)
        forward(length*3)
        left((angle/9)*8)
        forward(length*3.36)
        end_fill()
        penup()

    def strawberry_seeds():
        # Draw strawberry seeds
        color("black")
        turtlesize((length/50), (length/25))
        for strawberry_seeds in range(50):
            goto(x_strawberry, y_strawberry)
            setheading(0)
            forward(length*4)
            circle(-(length*2), (angle/18)*11)
            forward(length*8)
            circle(-(length*2), (angle/18)*7)
            setheading(randint((length*6.5), (angle/18)*11.5))
            forward(randint(length, (angle/18)*11.2))
            end_fill()
            stamp()
            penup()
    strawberry_fruit()
    strawberry_stem()
    strawberry_seeds()
    goto(x_strawberry_point, y_strawberry_point)
    # Draw card number/id and got to start Suit_3 starting point
    card_identifier()
    goto(x_strawberry_point, y_strawberry_point)

# Suit_4 is for avocado card
def Suit_4():
    color("black", "white")
    begin_fill()
    penup()
    setheading(0)
    x_avocado_point = (xcor())
    y_avocado_point = (ycor() - (length*6))
    pendown()
    # Draw card
    for draw_card in range(2):
        forward(card_width)
        circle(-radius, angle/2)
        forward(card_height)
        circle(-radius, angle/2)
    penup()
    end_fill()
    setheading(0)
    forward(card_width/10)
    right(angle/2)
    forward(card_height/1.7)
    setheading(0)
    x_avocado = (xcor())
    y_avocado = (ycor())

    def avocado_skin():
        # Draw avocado skin
        pendown()
        color("black", "dark green")
        begin_fill()
        left((angle/18)*7.5)
        circle(-(length*4.8), - (angle/18)*19)
        forward(-(length*9.6))
        circle(-(length*2.4), - (angle/18)*15.3)
        forward(-(length*11.2))
        end_fill()
        penup()

    def avocado_fruit():
        # Draw avocado fruit(inside part)
        goto(x_avocado, y_avocado)
        setheading(0)
        right(angle/18)
        forward((length/10)*3)
        left(angle/2)
        forward((length/10)*2)
        setheading(0)
        left((angle/18)*7.5)
        pendown()
        color("black", "light green")
        begin_fill()
        circle((-(length*5.7))*.8, - ((angle/18)*19))
        forward((-(length*11.4))*.8)
        circle((-(length*2.85))*.8, - ((angle/18)*15.3))
        forward((-(length*13.3))*.8)
        end_fill()
        penup()

    def avocado_seed():
        # Draw avocado seed
        goto(x_avocado, y_avocado)
        setheading(0)
        right(angle/18)
        forward((angle/18)*7.5)
        setheading(0)
        left((angle/18)*7.5)
        pendown()
        color("black", "brown")
        begin_fill()
        circle((length*2.5), (angle*2))
        end_fill()
        penup()
    avocado_skin()
    avocado_fruit()
    avocado_seed()
    goto(x_avocado_point, y_avocado_point)
    # Draw card number/id and got to start Suit_4 starting point
    card_identifier()
    goto(x_avocado_point, y_avocado_point)

# Suit_joker is for joker card
def Suit_joker():
    color("black", "magenta")
    x_joker = (xcor())
    y_joker = (ycor())
    pendown()
    begin_fill()
    setheading(0)
    # Draw card
    for draw_card in range(2):
        forward(card_width)
        circle(-radius, angle/2)
        forward(card_height)
        circle(-radius, angle/2)
    penup()
    end_fill()
    setheading(0)
    forward(card_width/3.2)
    right(angle/2)
    forward(card_height/3.5)
    setheading(0)

    def joker_cup():
        # Draw glass cup
        pendown()
        color("black", "white")
        begin_fill()
        for draw_card in range(2):
            forward(length*5)
            right(angle/2)
            forward(length*10)
            right(angle/2)
        end_fill()
        penup()

    def joker_drink():
        # Draw water in cup
        right(angle/2)
        forward(length*2)
        setheading(0)
        pendown()
        color("black", "light blue")
        begin_fill()
        for cup in range(2):
            forward(length*5)
            right(angle/2)
            forward(length*8)
            right(angle/2)
        end_fill()
        penup()

    def joker_straw():
        # Draw straw for umbrella
        color("black")
        begin_fill()
        pendown()
        forward(length*4)
        left((angle/9)*4)
        forward(length*5)
        left((angle/9)*5)
        forward(length/2)
        left((angle/9)*4)
        forward(length*5)
        penup()
        end_fill()
    joker_cup()
    joker_drink()
    joker_straw()
    # Go to Suit_joker starting point
    goto(x_joker, y_joker)
    # No need to draw card number/id on joker card

# Next lines of code are to run game
def deal_cards(game):
    for deck in game:
        # If statements to place cards on correct stack in relation to game function
        if deck[0] == 'Stack 1':
            goto(location_start[0])
        elif deck[0] == 'Stack 2':
            goto(location_start[1])
        elif deck[0] == 'Stack 3':
            goto(location_start[2])
        elif deck[0] == 'Stack 4':
            goto(location_start[3])
        elif deck[0] == 'Stack 5':
            goto(location_start[4])
        elif deck[0] == 'Stack 6':
            goto(location_start[5])

        # Next loop is to place cards(suits,drawings and card numbers/ids) on correct rows and multiply by
        # number of cards(number_of_cards) represented in game function
        for fruit in range(deck[2]):
            if deck[1] == 'Suit A':
                Suit_1()
            elif deck[1] == 'Suit B':
                Suit_2()
            elif deck[1] == 'Suit C':
                Suit_3()
            elif deck[1] == 'Suit D':
                Suit_4()

        # Next lines are to add 'Joker" card to stacks. So far I have only figured how to add it to the end of stack
        # not replace an existing card position.
        for joker_extra in range(deck[3]):
            if joker_extra == True:
                Suit_joker()



# Main Program
#
# This main program sets up the background
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('slow')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Summer Fruits")

### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_0) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

