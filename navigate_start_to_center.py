import cyberpi
import mbot2
import mbuild
import event
import time
#=================================
#==  PLACE ALL FUNCTIONS BELOW  ==
#=================================
def navigate_from_start_to_center():
   mbot2.straight(25). # move mbot forward 25cm at speed 50




#=================================
#==  PLACE ALL FUNCTIONS ABOVE  ==
#=================================
def go():
   navigate_from_start_to_center()

#####################################
#   DO NOT TOUCH THE LINES BELOW!   #
#    DO NOT ADD ANY LINES BELOW!    #
#####################################
@event.is_press('a')
def main():
    go()

