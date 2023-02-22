#changes in wallet.py
class Wallet:
  def __init__(self):
    self.balance = 0
  
  def setAmount(self, balance):
    self.balance = balance
  
  def getAmount(self):
    return self.balance
  
  def removeAmount(self):
    self.balance = 0
