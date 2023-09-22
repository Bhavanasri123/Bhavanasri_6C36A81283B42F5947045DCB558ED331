'''implement a class called player that represents a cricket player The player class should have a
method called play() which prints"The player is playing cricket.derive two classes batsman and
Bowler, from the player class override the play() method in each derived class to print "The batsman 
is bating"and "the bowler is bowling", respectively.write a program to create object of both the
Batsman and bowler classes and call the play() method for each object.'''


#define the base class player
class player:
  def play (self):
    print("The player is playing cricket.")

#define the derived class Batsman
class Batsman (player):
  def play(self):
    print("the batsman is batting.")

#define the derived class bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create object of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each object
batsman.play()
bowler.play()

