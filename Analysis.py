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

BTC = 1150

# Program starts here
def main():

    # get data organized in list
    betslips = getData()

    # separate data into CloudBet and NitrogenSports
    cloudBets = []
    nitroBets = []

    for bet in betslips:
        if (bet[0] == "WIN" or bet[0] == "LOSS" or bet[0] == "PUSH"):
            cloudBets.append(bet)
        else:
            nitroBets.append(bet)


    # Filter what you want
    #######################################

    getRecord("NBA", "All", cloudBets, nitroBets)

    #######################################


def getRecord(sport, betType, cloudList, nitroList):

    wins = 0
    losses = 0
    pushes = 0
    betSize = 0.0
    netProfit = 0.0

    if betType == "All":

        for cloud in cloudList:

            print(cloud)
            if cloud[0] == "WIN":
                wins = wins + 1
                betSize = betSize + float(cloud[8])
                netProfit = netProfit - float(cloud[8])
                netProfit = netProfit + float(cloud[2])
            if cloud[0] == "LOSS":
                losses = losses + 1
                betSize = betSize + float(cloud[7])
                netProfit = netProfit - float(cloud[7])
            if cloud[0] == "PUSH":
                pushes = pushes + 1

        for nitro in nitroList:
          if nitro[7] == sport or nitro[7] == "NBA (LIVE)" or nitro[7] == "NBA Player Props":

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

    elif (betType == "ML"):

          for cloud in cloudList:
              if "+" not in cloud[6] and "-" not in cloud[6]:

                print(cloud)
                if cloud[0] == "WIN":
                    wins = wins + 1
                    betSize = betSize + float(cloud[8])
                    netProfit = netProfit - float(cloud[8])
                    netProfit = netProfit + float(cloud[2])
                if cloud[0] == "LOSS":
                    losses = losses + 1
                    betSize = betSize + float(cloud[7])
                    netProfit = netProfit - float(cloud[7])
                if cloud[0] == "PUSH":
                    pushes = pushes + 1

          for nitro in nitroList:
             #f nitro[7] == sport or nitro[7] == "NBA (LIVE)" or nitro[7] == "NBA Player Props":
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

          for cloud in cloudList:
              if "+" in cloud[6] or "-" in cloud[6]:
                  
                print(cloud)
                if cloud[0] == "WIN":
                    wins = wins + 1
                    betSize = betSize + float(cloud[8])
                    netProfit = netProfit - float(cloud[8])
                    netProfit = netProfit + float(cloud[2]) 
                if cloud[0] == "LOSS":
                    losses = losses + 1
                    betSize = betSize + float(cloud[7])
                    netProfit = netProfit - float(cloud[7])
                if cloud[0] == "PUSH":
                    pushes = pushes + 1

          for nitro in nitroList:
             #if nitro[7] == sport or nitro[7] == "NBA (LIVE)" or nitro[7] == "NBA Player Props":
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
             #if nitro[7] == sport or nitro[7] == "NBA (LIVE)" or nitro[7] == "NBA Player Props":
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

    print(' ')
    print(str(wins) + "-" + str(losses) + "-" + str(pushes))
    print("Total Bet Size : " + str(betSize) + " BTC")
    print("Total Profit : " + str(netProfit) + " BTC")
    print("Total Profit : $" + str(netProfit * BTC))
    print("ROI : " + str((((netProfit + betSize) - betSize)/betSize) * 100) + "%")
    print(' ')

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
