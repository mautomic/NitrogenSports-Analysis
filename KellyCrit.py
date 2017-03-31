
# Use the Kelly Criterion to figure out optimal bet

# TODO: How can we predict probability of the pick without 
#       relying on the odds?

# values in BTC
bankroll = 0.087245
betOdds = 1.948
probSuccess = 1/(betOdds)
probFailure = 1.0-probSuccess

fraction = ((betOdds * probSuccess) - probFailure)/betOdds

print ("Success% : " + str(probSuccess))

if (bankroll * fraction) < 0:
  print ("Don't Bet")
else:
  print ("Bet Size : " + str(bankroll * fraction))





