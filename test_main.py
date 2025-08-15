import unittest
from main import *
import math


class TestMain(unittest.TestCase):
    def test_solution(self):
        result = 1 * 9
        risks = int(9)
        acc = {"John": 22, "Steve": 24, "James": 30}
        acc2 = {"Ryu": 33, "Brad": 37, "Raymond": 50}
        obj = AccountInfo()
        secondResult = obj.solution(acc, acc2)
        self.assertEqual(secondResult, acc)
        self.assertEqual(result, risks)
        self.assertNotIn(f"{acc2}", "j".lower())
        self.assertNotEqual(acc2, result)
    

    def test_estimate(self):
        result = 2 - 1
        num = 1
        newNum = 0
        report = str()
        account = AccountInfo.estimate(10, 10)
        if result > num:
            newNum = abs(newNum) 
        else: 
            newNum = round(newNum)
        self.assertEqual(account, result)
        self.assertAlmostEqual(account, num)
        self.assertNotIsInstance(newNum, tuple)
        self.assertIsNotNone(report, str)
        
        
    def test_incomeSpike(self):
        result = 0.2 + 1.0
        expected = 1.2 
        agClass = Agriculture("==")
        solution = agClass.incomeSpike(expected)
        self.assertEqual(solution, expected)
        self.assertAlmostEqual(solution, result)
        self.assertIsInstance(solution, float)


if __name__ == '__main__':
    unittest.main()
   
