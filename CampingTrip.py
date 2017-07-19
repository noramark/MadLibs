""" Camping trip by Liana Vivian Peta and Nora"""
##Nora

Intro = "welcome! You are on a camping trip with your family. Hope you have fun! \n Oh no! a tree has fallen over your path! you have two choices. \n You can either (1) go over the tree and continue on the path or (2) walk around the tree. Please type 1 or 2 based on your decision."
print(Intro)
TreeChoice =input("Enter: ")
if TreeChoice==1:
  print("yay you managed to stick with your group.")
## Vivian
  print("You see caution signs with possible bears ahead. Watch out!!!")
  print("You can neither (1) turn around or (2) keep going. Type 1 or 2 based on your decision. ")
  signChoice=input("Enter: ")
  if signChoice==1:
    print("You will be leaving camp.")
    exit(0)
  else:
    print("yayy! You keep camping.")
    ##Peta
    print("oh no! There is a bear in front of you you can either (1) play dead or (2) run away")
    BearChoice=input("Enter: ")
    if BearChoice== 1:
        print("Yay the bear left you alone. you have a nice rest of you trip. Bye")
        exit (0)
    else:
        print("Oh no! The bear chases you out the forest")
        exit(0)
elif TreeChoice == 2:
  print("Oh no! you got separated from the group. ")
 ##Liana
  print("Now that you've been seperated, you have two options. Either you (1) retrace your steps or (2)keep going and pray. Type 1 or 2 based on your decision.")
  lostChoice=input("Enter: ")
  if lostChoice==1:
     print("You found your family! You headed up to the top of the mountain and had a good trip!")
     exit(0)
  else:
     print("You didn't find your family! You keep walking alone.")
     ##nora
     print("while you're walking, you get stung by a bee and you start having an allergic reaction!! What do you do? \n Do you (1) run back to your car and get your epipen or \n (2) run around and scream.")
     BeeChoice=input("Enter: ")
     if BeeChoice == 1:
         print("great! you got to your car in time and stopped the allergic reaction")
         ##Vivian
         print("Now your reaction was over, you tried to reenter the forest. But you do not remember the path and you see two trial. (1)the blue trial (2)the red trial")
         trialChoice=input("Enter:")
         if trialChoice==1:
            print("yayy you finds your family. Have a nice trip.")
            exit(0)
         else:
            print("Finds a cabin and spend the night and find your car the next day and go home.")
            exit(0)
     else:
         print ("you wake up the next day in a hospital after your family found you when you were screaming. You decide camping is not for you and head home. Bye")
         exit(0)
elif TreeChoice != 1 and TreeChoice != 2:
  print("sorry you can't follow simple instructions. bye. ")
  exit(0)
