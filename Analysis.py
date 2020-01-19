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

# Retrieve current Bitcoin spot price via Coinbase
PRICE_JSON = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
BTC = float(PRICE_JSON.json()['data']['amount'])

# Enter your bankroll size
bankroll = 0.276

def main():

    betslips = getData()

    # Filter what you want, ie. All, ML, Spread, OverUnder
    analyze("All", betslips)

def analyze(betType, nitroList):

    wins = 0
    losses = 0
    pushes = 0
    betSize = 0.0
    netProfit = 0.0
    unitSize = .003
    units = 0

    if betType == "All":

        for nitro in nitroList:

            print(nitro)

            if (len(nitro) < 10):
                if nitro[5] == "win":
                    wins = wins + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit + float(nitro[4])
                if nitro[5] == "lose":
                    losses = losses + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit - float(nitro[3])
                if nitro[5] == "push":
                    pushes = pushes + 1
            else:
                if nitro[5] == "win" and nitro[13] == "win":
                    wins = wins + 1
                    betSize = betSize + float(nitro[len(nitro)-1].split(" ")[0])
                    netProfit = netProfit + float(nitro[len(nitro)-1].split(" ")[0])
                else:
                    losses = losses + 1
                    betSize = betSize + float(nitro[len(nitro)-2].split(" ")[0])
                    netProfit = netProfit - float(nitro[len(nitro)-2].split(" ")[0])


    elif (betType == "ML"):

        for nitro in nitroList:

            if "ML" in nitro[1]:
                 
                print(nitro)
                if nitro[5] == "win":
                    wins = wins + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit + float(nitro[4])
                if nitro[5] == "lose":
                    losses = losses + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit - float(nitro[3])
                if nitro[5] == "push":
                    pushes = pushes + 1

    elif (betType == "Spread"):

        for nitro in nitroList:

                if "+" in nitro[1] or "-" in nitro[1]: 
                     
                    print(nitro)
                    if nitro[5] == "win":
                        wins = wins + 1
                        betSize = betSize + float(nitro[3])
                        netProfit = netProfit + float(nitro[4])
                    if nitro[5] == "lose":
                        losses = losses + 1
                        betSize = betSize + float(nitro[3])
                        netProfit = netProfit - float(nitro[3])
                    if nitro[5] == "push":
                        pushes = pushes + 1

    elif (betType == "OverUnder"):

        for nitro in nitroList:
            
            if " over " in nitro[1] or " under " in nitro[1] or " Over " in nitro[1] or " Under " in nitro[1]:
                     
                print(nitro)
                if nitro[5] == "win":
                    wins = wins + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit + float(nitro[4])
                if nitro[5] == "lose":
                    losses = losses + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit - float(nitro[3])
                if nitro[5] == "push":
                    pushes = pushes + 1

    posOrNeg = ""
    units = netProfit/unitSize
    if (units > 0):
        posOrNeg = "+"

    unitString = format(units, '.2f')
    percent = format(float(wins)*100/(float(wins)+float(losses)), '.2f')

    print(' ')
    print(str(wins) + "-" + str(losses) + "-" + str(pushes))
    print(percent + "% Success Rate")
    print("Total Profit : " + str(netProfit) + " BTC")
    print("Total Profit : $" + str(netProfit * BTC))
    #print("Total Bet Size: $" + str(betSize * BTC))
    print("ROI : " + str((((netProfit + betSize) - betSize)/betSize) * 100) + "%")
    print(posOrNeg + unitString + " units")
    print("Bitcoin : $" + str(BTC))
    print("Bankroll : $" + str(bankroll * BTC))
    print(' ')


# Function to perform calculations
def calculate(betslips):
    return []


# Function to open file of data and parse it into a list of betslips
def getData():

    f = open('MyWagers.csv', 'r')
    data = csv.reader(f, delimiter=',')
    betslips = []
    for line in data:
        betslips.append(line)
    return betslips
 
if __name__ == '__main__':
    main()
