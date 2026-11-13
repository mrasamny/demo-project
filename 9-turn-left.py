import cyberpi
import mbot2
import mbuild
import event
import time
#=================================
#==  PLACE ALL FUNCTIONS BELOW  ==
#=================================
def turn_left():
    mbot2.turn(-90, 50) # turn left 90 degrees at speed 50


#=================================
#==  PLACE ALL FUNCTIONS ABOVE  ==
#=================================
def go():
	turn_left() # call the turn_left function

#####################################
#   DO NOT TOUCH THE LINES BELOW!   #
#    DO NOT ADD ANY LINES BELOW!    #
#####################################
@event.is_press('a')
def main():
    go()

