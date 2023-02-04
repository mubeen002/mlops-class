from wallet import Wallet

def test_getAmount():
  obj = Wallet()
  obj.setAmount(100)
  assert obj.getAmount() == 100
