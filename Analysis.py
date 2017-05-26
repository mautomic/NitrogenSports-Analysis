# Nitrogen Sports Betting Analysis

# Format of NS Betslip ----------
# Game
# Game Prediction
# Odds
# Risk BTC
# Winnings BTC
# Win/Lose
# Sport
# Subcategory
# Betslip ID

# Format of NS parlays -------
# Individual Risk/Winnings 0.0
# 8 lines then start next bet (8 lines)...and etc
# Betslip ID
# Parlay Keyword
# Odds
# Risk BTC
# Winnings BTC

import requests

# Retrieve current Bitcoin spot price via Coinbase
PRICE_JSON = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
BTC = float(PRICE_JSON.json()['data']['amount'])

bankroll = 0.0


def main():

    # get data in organized list
    betslips = getData()

    # Filter what you want
    #######################################

    getRecord("All", betslips)

    #######################################


def getRecord(betType, nitroList):

    wins = 0
    losses = 0
    pushes = 0
    betSize = 0.0
    netProfit = 0.0
    unitSize = .003
    units = 0.0

    if betType == "All":

        for nitro in nitroList:

            print(nitro)
            if nitro[5] == "win":
                wins = wins + 1
                betSize = betSize + float(nitro[3])
                netProfit = netProfit + float(nitro[4])
                units = units + (float(nitro[4])/unitSize)
            if nitro[5] == "lose":
                losses = losses + 1
                betSize = betSize + float(nitro[3])
                netProfit = netProfit - float(nitro[3])
                units = units - (float(nitro[3])/unitSize)
            if nitro[5] == "push":
                pushes = pushes + 1

    elif (betType == "ML"):

        for nitro in nitroList:

            if "ML" in nitro[1]:
                 
                print(nitro)
                if nitro[5] == "win":
                    wins = wins + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit + float(nitro[4])
                    units = units + (float(nitro[4])/unitSize)
                if nitro[5] == "lose":
                    losses = losses + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit - float(nitro[3])
                    units = units - (float(nitro[3])/unitSize)
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
                        units = units + (float(nitro[4])/unitSize)
                    if nitro[5] == "lose":
                        losses = losses + 1
                        betSize = betSize + float(nitro[3])
                        netProfit = netProfit - float(nitro[3])
                        units = units - (float(nitro[3])/unitSize)
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
                    units = units + (float(nitro[4])/unitSize)
                if nitro[5] == "lose":
                    losses = losses + 1
                    betSize = betSize + float(nitro[3])
                    netProfit = netProfit - float(nitro[3])
                    units = units - (float(nitro[3])/unitSize)
                if nitro[5] == "push":
                    pushes = pushes + 1

    posOrNeg = ""
    if (units > 0):
        posOrNeg = "+"

    unitString = format(units, '.2f')

    print(' ')
    print(str(wins) + "-" + str(losses) + "-" + str(pushes))
    print("Total Profit : " + str(netProfit) + " BTC")
    print("Total Profit : $" + str(netProfit * BTC))
    print("ROI : " + str((((netProfit + betSize) - betSize)/betSize) * 100) + "%")
    print(posOrNeg + unitString + " units")
    print("Bitcoin : $" + str(BTC))
    print("Bankroll : $" + str(bankroll * BTC))
    print(' ')


# Function to perform calculations
def calculate(betslips):
    return []


# Function to format any non-NitrogenSports bets to proper style. 
# I also use CloudBet so this will adjust those bets
def formatToNitro():
    return []


# Function to open file of data and parse it into a list of betslips
def getData():

    f = open('Wagers.txt', 'r')

    betslips = []
    temp = []
    count = 0

    for line in f:
        line = line.strip('\n')

        # break to start after model following, continue for prior
        if "PHASE" in line:
            break

        # Parse out Blank lines and Parlays
        if len(line) is not 0:
            temp.append(line)
            count = count + 1
        else:
            if (count < 16):
                betslips.append(temp)
            temp = []
            count = 0

    # to remove empty lists (spaces)
    bets = [x for x in betslips if x]
    return bets
 
if __name__ == '__main__':
    main()
