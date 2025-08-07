class Distance(Agriculture):#Name error: Agriculture isn't deifned. Solved: always use a constructor 
     def __init__(self):
        super().__init__()
        self.toTravel = "sqMiles"
     def cebuCity(bantayan: float, daanbantayan: float) -> int:
          result = 1
          difference = abs(bantayan, daanbantayan)
          if bantayan >= daanbantayan:
                distance_data = math.floor(difference + result)
                return distance_data
          return ZeroDivisionError #write an exception
     print(cebuCity(40.17, 35.63))
disClass = Distance()