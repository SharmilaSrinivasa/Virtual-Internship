import unittest
from client import getDataPoint
from client import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getRatio_WithNonZeroDenominator(self):
    price_a = 121.68
    price_b = 119.2
    self.assertEqual(getRatio(price_a, price_b), (price_a/price_b))

  def test_getRatio_WithZeroDenominator(self):
		price_a = 121.68
		price_b = 0
		self.assertEqual(getRatio(price_a, price_b), None)

  """ ------------ improvements to uint test ------------ """
  def test_getRatio_ZeroAsResult(self):
		price_a = 0
		price_b = 121.68
		self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_OneAsResult(self):
		price_a = 121.68
		price_b = 121.68
		self.assertEqual(getRatio(price_a, price_b), 1)

  def test_getRatio_NumeratorLessThanDenominator(self):
		price_a = 119.2
		price_b = 121.68
		self.assertLess(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
