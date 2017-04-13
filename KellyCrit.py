
# Use the Kelly Criterion to figure out optimal bet

# TODO: How can we predict probability of the bet without 
#       relying on the odds? Build a custom model to value bets/predict scores

# values in BTC
bankroll = 0.10508
betOdds = 1.948
probSuccess = 1/(betOdds)
probFailure = 1.0-probSuccess

fraction = ((betOdds * probSuccess) - probFailure)/betOdds

print ("Success% : " + str(probSuccess))

if (bankroll * fraction) < 0:
  print ("Don't Bet")
else:
  print ("Bet Size : " + str(bankroll * fraction))





