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
# Betslip ID

# for parlays -------
# Individual Risk/Winnings 0.0
# 8 lines then start next bet (8 lines)...and etc
# Betslip ID
# Parlay Keyword
# Odds
# Risk BTC
# Winnings BTC


f = open('NS Wagers.txt', 'r')

s = f.read()
print s
