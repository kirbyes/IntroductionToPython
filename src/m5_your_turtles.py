"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Eric Kirby.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
turtle1 = rg.SimpleTurtle('turtle')
turtle1.pen = rg.Pen('red', 2)
turtle1.speed = 10

size = 50

for k in range(8):
    turtle1.draw_regular_polygon(k+3, size)

turtle2 = rg.SimpleTurtle("turtle")
turtle2.pen = rg.Pen('green', 2)
turtle2.speed = 10

turtle2.pen_up()
turtle2.right(90)
turtle2.forward(150)

for k in range(8):
    turtle2.pen_down()
    turtle2.draw_circle(size)

    size = size + 10

    turtle2.pen_up()
    turtle2.right(90)
    turtle2.forward(10)
    turtle2.left(90)


window.close_on_mouse_click()

