# Nitrogen Sports Betting Analysis
# Built by Sports Betting God Maurya

# Format of Betslip ----------
# Game
# Game Prediction
# Odds
# Risk BTC
# Winnings BTC
# Win/Lose
# Sport
# Subcategory
# 9: Betslip ID

# for parlays -------
# Individual Risk/Winnings 0.0
# 8 lines then start next bet (8 lines)...and etc
# Betslip ID
# Parlay Keyword
# Odds
# Risk BTC
# Winnings BTC


f = open('NS Wagers 3-31-17.txt', 'r')

betslips = []
temp = []

for line in f:
	line = line.strip('\n')
	# print line

	if len(line) is not 0:
		temp.append(line)
	else:
		betslips.append(temp)
		temp = []

bets = [x for x in betslips if x]

xyla = 0

for elem in bets:
	xyla = xyla + 1
	print elem

print xyla

# Filter by Sport
# Odd Range
# Bet range
# Win/lose percentages






















