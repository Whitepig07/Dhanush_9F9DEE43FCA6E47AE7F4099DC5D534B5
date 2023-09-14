class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
Batsman = Batsman()
Bowler=Bowler()

# Call the play() method for each object
Batsman.play()
Bowler.play()