# Nitrogen Sports Betting Analysis
# Built by Sports Betting God Maurya

# Format of NS Betslip ----------
# Game
# Game Prediction
# Odds
# Risk BTC
# Winnings BTC
# Win/Lose
# Sport
# Subcategory
# 9: Betslip ID

# Format of NS parlays -------
# Individual Risk/Winnings 0.0
# 8 lines then start next bet (8 lines)...and etc
# Betslip ID
# Parlay Keyword
# Odds
# Risk BTC
# Winnings BTC


# Program starts here
def main():

  betslips = getData()


# Function to open file of data and parse it into a list of betslips
def getData():

  f = open('NS Wagers 3-31-17.txt', 'r')

  betslips = []
  temp = []

  for line in f:
  	line = line.strip('\n')

  	if len(line) is not 0:
  		temp.append(line)
  	else:
  		betslips.append(temp)
  		temp = []

  # to remove empty lists (spaces)
  bets = [x for x in betslips if x]
  return bets


# TODO
# Filter by Sport
# Odd Range
# Bet range
# Win/lose percentages
 
if __name__ == '__main__':
  main()
