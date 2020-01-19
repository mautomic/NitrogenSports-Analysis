# Nitrogen Sports Betting Analysis

### Updated Jan 2020
# Format of NitrogenSports Betslip 
# Bet type
# Betslip Id
# Date
# Sport
# League
# Event
# Wager
# Odds
# Risk
# To Win

import requests
import csv
from betType import BetType
from metricSet import MetricSet

# Retrieve current Bitcoin spot price via Coinbase
PRICE_JSON = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
BTC = float(PRICE_JSON.json()['data']['amount'])

# Enter your bankroll size
bankroll = 0.15

def main():

    betslips = getData()
    analyze(betslips)

# Function that performs the main analysis
def analyze(betslips):

    mlMetrics = MetricSet(0, 0, 0, 0.0, 0.0)
    spreadMetrics = MetricSet(0, 0, 0, 0.0, 0.0)
    overUnderMetrics = MetricSet(0, 0, 0, 0.0, 0.0)
    unitSize = .01
    parlayCount = 0

    for bet in betslips:

        # filter out header
        if (bet[0] == "Status"):
            continue

        # TODO: add support for parlay tracking
        # a more structured approach would be to add the betslip ID to a dictionary,
        # and then find all bets with the same ID to analyze the parlay results
        if (bet[1] == "parlay"):
            parlayCount = parlayCount + 1
            continue

        betType = getBetType(bet)

        if (betType == BetType.ML):
            updateMetrics(mlMetrics, bet)
        elif (betType == BetType.SPREAD):
            updateMetrics(spreadMetrics, bet)
        else: 
            updateMetrics(overUnderMetrics, bet)

    print("Bitcoin : $" + str(BTC))
    print("Bankroll : $" + str(bankroll * BTC))

    print("ML metrics")
    printStats(mlMetrics, unitSize)
    print("Spread metrics")
    printStats(spreadMetrics, unitSize)
    print("OverUnder metrics")
    printStats(overUnderMetrics, unitSize)

    print("Skipped " + str(parlayCount) + " parlay bets")

# Function to retrieve type of bet from betslip
def getBetType(betslip):
    
    bet = betslip[7]
    if "ML" in bet:
        return BetType.ML
    elif "-" in bet or "+" in bet:
        return BetType.SPREAD
    elif "Over" in bet or "Under" in bet:
        return BetType.OVERUNDER

# Function to update metrics for a type of bet based on the status of the bet
def updateMetrics(metricSet, bet):

    status = bet[0]
    if (status == "push"):
        metricSet.addPush()
    else:
        if (status == "win"):
            metricSet.addWin()
            metricSet.addNetProfit(bet[10])
        elif (status == "lose"):
            metricSet.addLoss()
            metricSet.subtractNetProfit(bet[10])
        metricSet.addBetSize(bet[9])

# Function that takes in a metricSet and prints all relevant stats
def printStats(metricSet, unitSize):

    wins = metricSet.wins
    losses = metricSet.losses
    pushes = metricSet.pushes
    betSize = metricSet.betSize
    netProfit = metricSet.netProfit

    posOrNeg = ""
    units = netProfit/unitSize
    if (units > 0):
        posOrNeg = "+"

    unitString = format(units, '.2f')
    percent = format(float(wins)*100/(float(wins)+float(losses)), '.2f')

    print("-------------------")
    print(str(wins) + "-" + str(losses) + "-" + str(pushes))
    print(percent + "% Success Rate")
    print("Total Profit : " + str(netProfit) + " BTC")
    print("Total Profit : $" + str(netProfit * BTC))
    print("ROI : " + str((((netProfit + betSize) - betSize)/betSize) * 100) + "%")
    print(posOrNeg + unitString + " units")
    print("-------------------")

# Function to open csv of data and parse it into a list of betslips
def getData():

    f = open('MyWagers.csv', 'r')
    data = csv.reader(f, delimiter=',')
    betslips = []
    for line in data:
        betslips.append(line)
    return betslips
 
if __name__ == '__main__':
    main()
