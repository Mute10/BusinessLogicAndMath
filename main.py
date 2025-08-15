import math
from fastapi import FastAPI
import random
from fractions import Fraction
from decimal import Decimal

app = FastAPI()

def main():
     return 

class AccountInfo:
    try:
     @staticmethod
     def solution(acc:dict, num:dict) -> dict:
            result = 0
            risks = {"positive", "negative"}

            for n in range(0, len(acc), 1):
                if isinstance(n, dict):
                    result += 1
                    risks.add("n is greater or equal to num")
            return acc
    except Exception: print("there's no solution")


    def estimate(highNum:int, lowNum:int) -> int:
     result = 0
     report = str("")
     num = int()
     if num <= highNum:
          result += 1
          report += str(highNum)
     else:
          raise ValueError(f"num must be higher than '{highNum}'")
     if num >= highNum:
          result = math.floor((result + 2) * 4)
          report += str(num > highNum)
     elif lowNum >= num:
          math.ceil(result)
          lowNum = [int(d) for d in str(num)]
     else:
          result -= 1
          randomNum = random.randint(0, 9)
          lowNum = [int(d) for d in str(num)]
          lowNum += [randomNum, randomNum, randomNum]
     return result


class Agriculture(AccountInfo):
    def __init__(self, quickFix):
        self.quickFix = quickFix
    def incomeSpike(self, bonus: float):
          if not isinstance(bonus, (float, int)):
               raise TypeError("Bonus must be a float")
          return bonus
    
    def geometry(self):
          result = {}
          endResult = 2
          statusReport = {"Janurary-March": 5000,
                          "April-June": 10000,
                          "July-September": 17000,
                          "October-December": 2000}
          updateValue = 0
          updatedReport = dict(statusReport).copy()
          for key, value in statusReport:
                    if value > 5000:
                         statusReport.popitem()
                         result.update(statusReport)
                    elif len(key) > 5:
                         short_key = key[:5]

          return (updateValue, updatedReport)



class Distance(Agriculture):
     def __init__(self, quickFix):
        self.quickFix = quickFix
        super().__init__(quickFix)
     def cebuCity(bantayan: float, daanbantayan: float) -> int:
          result = 1
          difference = abs(bantayan, daanbantayan)
          if bantayan >= daanbantayan:
                distance_data = math.floor(difference + result)
                return distance_data
          raise ZeroDivisionError("Can't divide by 0")
disClass = Distance("==")

          
class FlexMath:
     @staticmethod
     def advancedMath(solved: list[float], unsolved: list[float]) -> int:
               result = []
               alpha = [0.9, -0.10, 9, 12]
               beta = [[4.4, 1, 1, 0], [2.2, 1.1, 0.2, 0.3]]
               gamma = {90.90, 9.9, 2.77, 300.00}
               star = {2, 2, 2, 2}
               for i in range(len(solved)):
                    for j in range(len(unsolved) -1, -1, -1):
                         if i >= 20:
                              omega = list(filter(lambda float: float %2 == 0, alpha))
                              result.append(omega)
                         elif i < 20:
                              mega = []
                              for sublist in beta:
                                mega.extend(filter(lambda number: number %2 == 1, sublist))
                              result.append(mega)
                         elif sum(gamma) > sum(star):
                              result.extend([4000, 4000])
                         else:
                              return 0
                         
                         if j > 40:
                            if isinstance(unsolved[i], list):
                                   result.append(unsolved[i][j])
                            else: 
                                 result.append(0)
                         elif j > 20:
                              result.append(unsolved[j])
                         else: 
                              return None
               raise TypeError("result Isn't an integer")
     
Sol = FlexMath() 
adSol = Sol.advancedMath([1.1] * 8**2, [1.2] * 8**2)



class MathBiome:
     @staticmethod
     def magicalChaos(goodNum, badNum):
          f1 = Fraction(22/300)
          f2 = Fraction(17*4) / Fraction(1717/7)
          f3 = Fraction(120/8) + Fraction(19/2)
          dec = Decimal(0.2/3.13) - Decimal(-1 * -19) #-18.93610223642172522839910442
          if f1 >= f2:
               dec = []
               dec.append(random.randint(1, 100))
          elif f1 >= f3:
               dec = []
               dec.append(random.random())
          else:
              tvl = f1 * f2
          return f3
MathBiome.magicalChaos(2, 4)
          

"""""
math.sqrt(x)      # square root
math.pow(x, y)    # x to the power of y
math.floor(x)     # round down
math.ceil(x)      # round up
math.sin(x)       # sine (x in radians)
math.cos(x)       # cosine
math.log(x)       # natural log

abs(x)       # absolute value
round(x, n)  # round to n decimal places
min(a, b, c)
max(a, b, c)
"""

if __name__ == "main" :

            
     main()
            
