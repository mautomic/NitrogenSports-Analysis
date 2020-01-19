class MetricSet:
	
	def __init__(self, wins, losses, pushes, bet_size, net_profit):
		self._wins = wins
		self._losses = losses
		self._pushes = pushes
		self._bet_size = bet_size
		self._net_profit = net_profit

	def add_win(self):
		self._wins = self._wins + 1

	def add_loss(self):
		self._losses = self._losses + 1

	def add_push(self):
		self._pushes = self._pushes + 1

	def add_bet_size(self, bet_size):
		self._bet_size = self._bet_size + float(bet_size)

	def add_net_profit(self, net_profit):
		self._net_profit = self._net_profit + float(net_profit)

	def subtract_net_profit(self, net_profit):
		self._net_profit = self._net_profit - float(net_profit)

