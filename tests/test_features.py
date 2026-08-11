import unittest
import pandas as pd
import numpy as np

class TestMicrostructureFeatures(unittest.TestCase):
    def setUp(self):
        # Sample dataframe representing tick order book and trade data
        data = {
            'BidPriceL1': [100.0, 100.2],
            'AskPriceL1': [100.5, 100.4],
            'BidQtyL1': [10.0, 20.0],
            'AskQtyL1': [5.0, 10.0],
            'BidQtyL2': [15.0, 25.0],
            'AskQtyL2': [10.0, 15.0],
            'Price': [100.2, 100.3],
            'Quantity': [0.0, 15.0]  # First row has 0 volume to test VWAP fallback
        }
        self.df = pd.DataFrame(data)

    def test_micro_price(self):
        # Calculate Micro-price
        micro = (self.df['BidPriceL1'] * self.df['AskQtyL1'] + self.df['AskPriceL1'] * self.df['BidQtyL1']) / (self.df['BidQtyL1'] + self.df['AskQtyL1'] + 1e-9)
        # Row 0: (100.0 * 5.0 + 100.5 * 10.0) / 15.0 = (500 + 1005) / 15 = 1505 / 15 = 100.33333333
        self.assertAlmostEqual(micro.iloc[0], 100.33333333)
        # Row 1: (100.2 * 10.0 + 100.4 * 20.0) / 30.0 = (1002 + 2008) / 30 = 3010 / 30 = 100.33333333
        self.assertAlmostEqual(micro.iloc[1], 100.33333333)

    def test_spread(self):
        spread = self.df['AskPriceL1'] - self.df['BidPriceL1']
        self.assertAlmostEqual(spread.iloc[0], 0.5)
        self.assertAlmostEqual(spread.iloc[1], 0.2)

    def test_weighted_obi(self):
        levels = 2
        weights = 1.0 / np.arange(1, levels + 1)  # [1.0, 0.5]
        
        bid_cols = ['BidQtyL1', 'BidQtyL2']
        ask_cols = ['AskQtyL1', 'AskQtyL2']
        
        weighted_bid = self.df[bid_cols].dot(weights)
        weighted_ask = self.df[ask_cols].dot(weights)
        obi = (weighted_bid - weighted_ask) / (weighted_bid + weighted_ask + 1e-9)
        
        # Row 0: weighted_bid = 10*1.0 + 15*0.5 = 17.5. weighted_ask = 5*1.0 + 10*0.5 = 10.
        # OBI = (17.5 - 10) / 27.5 = 7.5 / 27.5 = 0.272727
        self.assertAlmostEqual(obi.iloc[0], 0.2727272727)

    def test_vwap_fallback(self):
        # VWAP = rolling (price * qty) sum / rolling qty sum. If rolling qty sum is 0, fallback to current price
        # Row 0: price = 100.2, qty = 0.0. rolling sum of qty = 0.0.
        # Fallback price should be 100.2.
        quantity_sum = self.df['Quantity'].rolling(window=1).sum()
        vwap = (self.df['Price'] * self.df['Quantity']).rolling(window=1).sum() / quantity_sum
        vwap = vwap.fillna(self.df['Price'])
        
        self.assertEqual(vwap.iloc[0], 100.2)
        self.assertEqual(vwap.iloc[1], 100.3)

if __name__ == '__main__':
    unittest.main()
