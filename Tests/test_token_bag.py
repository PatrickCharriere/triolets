
from unittest import TestCase
from TokenBag import TokenBag

class Test(TestCase):
    def test_default_token_bag(self):
        tokenBag = TokenBag()
        self.assertEqual(9, tokenBag.countTokens(0))
        self.assertEqual(9, tokenBag.countTokens(1))
        self.assertEqual(8, tokenBag.countTokens(2))
        self.assertEqual(8, tokenBag.countTokens(3))
        self.assertEqual(7, tokenBag.countTokens(4))
        self.assertEqual(8, tokenBag.countTokens(5))
        self.assertEqual(6, tokenBag.countTokens(6))
        self.assertEqual(6, tokenBag.countTokens(7))
        self.assertEqual(4, tokenBag.countTokens(8))
        self.assertEqual(4, tokenBag.countTokens(9))
        self.assertEqual(3, tokenBag.countTokens(10))
        self.assertEqual(3, tokenBag.countTokens(11))
        self.assertEqual(2, tokenBag.countTokens(12))
        self.assertEqual(2, tokenBag.countTokens(13))
        self.assertEqual(1, tokenBag.countTokens(14))
        self.assertEqual(1, tokenBag.countTokens(15))
        self.assertEqual(83, tokenBag.countTokens())
        self.assertEqual(2, tokenBag.countTokens('x'))
        
        