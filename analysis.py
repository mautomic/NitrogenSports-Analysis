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
from bet_type import BetType
from metric_set import MetricSet

# Retrieve current Bitcoin spot price via Coinbase
PRICE_JSON = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
BTC = float(PRICE_JSON.json()['data']['amount'])

# Enter your bankroll size
bankroll = 0.15

# Main functin to kick off program
def main():

    betslips = get_data()
    analyze(betslips)

# Function that performs the main analysis
def analyze(betslips):

    ml_metrics = MetricSet(0, 0, 0, 0.0, 0.0)
    spread_metrics = MetricSet(0, 0, 0, 0.0, 0.0)
    over_under_metrics = MetricSet(0, 0, 0, 0.0, 0.0)
    unit_size = .01
    parlay_count = 0

    for bet in betslips:

        # filter out header
        if (bet[0] == "Status"):
            continue

        # TODO: add support for parlay tracking
        # a more structured approach would be to add the betslip ID to a dictionary,
        # and then find all bets with the same ID to analyze the parlay results
        if (bet[1] == "parlay"):
            parlay_count = parlay_count + 1
            continue

        betType = get_bet_type(bet)

        if (betType == BetType.ML):
            update_metrics(ml_metrics, bet)
        elif (betType == BetType.SPREAD):
            update_metrics(spread_metrics, bet)
        else: 
            update_metrics(over_under_metrics, bet)

    print("Bitcoin : $" + str(BTC))
    print("Bankroll : $" + str(bankroll * BTC))

    print("ML metrics")
    print_metrics(ml_metrics, unit_size)
    print("Spread metrics")
    print_metrics(spread_metrics, unit_size)
    print("OverUnder metrics")
    print_metrics(over_under_metrics, unit_size)

    print("Skipped " + str(parlay_count) + " parlay bets")

# Function to retrieve type of bet from betslip
def get_bet_type(betslip):
    
    bet = betslip[7]
    if "ML" in bet:
        return BetType.ML
    elif "-" in bet or "+" in bet:
        return BetType.SPREAD
    elif "Over" in bet or "Under" in bet:
        return BetType.OVERUNDER

# Function to update metrics for a type of bet based on the status of the bet
def update_metrics(metric_set, bet):

    status = bet[0]
    if (status == "push"):
        metric_set.add_push()
    else:
        if (status == "win"):
            metric_set.add_win()
            metric_set.add_net_profit(bet[10])
        elif (status == "lose"):
            metric_set.add_loss()
            metric_set.subtract_net_profit(bet[10])
        metric_set.add_bet_size(bet[9])

# Function that takes in a metricSet and prints all relevant stats
def print_metrics(metric_set, unit_size):

    wins = metric_set._wins
    losses = metric_set._losses
    pushes = metric_set._pushes
    bet_size = metric_set._bet_size
    net_profit = metric_set._net_profit

    pos_or_neg = ""
    units = net_profit/unit_size
    if (units > 0):
        pos_or_neg = "+"

    unit_string = format(units, '.2f')
    percent = format(float(wins)*100/(float(wins)+float(losses)), '.2f')

    print("-------------------")
    print(str(wins) + "-" + str(losses) + "-" + str(pushes))
    print(percent + "% Success Rate")
    print("Total Profit : " + str(net_profit) + " BTC")
    print("Total Profit : $" + str(net_profit * BTC))
    print("ROI : " + str((((net_profit + bet_size) - bet_size)/bet_size) * 100) + "%")
    print(pos_or_neg + unit_string + " units")
    print("-------------------")

# Function to open csv of data and parse it into a list of betslips
def get_data():

    f = open('MyWagers.csv', 'r')
    data = csv.reader(f, delimiter=',')
    betslips = []
    for line in data:
        betslips.append(line)
    return betslips
 
if __name__ == '__main__':
    main()
