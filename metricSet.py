class MetricSet:
	
	def __init__(self, wins, losses, pushes, betSize, netProfit):
		self.wins = wins
		self.losses = losses
		self.pushes = pushes
		self.betSize = betSize
		self.netProfit = netProfit

	def addWin(self):
		self.wins = self.wins + 1

	def addLoss(self):
		self.losses = self.losses + 1

	def addPush(self):
		self.pushes = self.pushes + 1

	def addBetSize(self, betSize):
		self.betSize = self.betSize + float(betSize)

	def addNetProfit(self, netProfit):
		self.netProfit = self.netProfit + float(netProfit)

	def subtractNetProfit(self, netProfit):
		self.netProfit = self.netProfit - float(netProfit)

