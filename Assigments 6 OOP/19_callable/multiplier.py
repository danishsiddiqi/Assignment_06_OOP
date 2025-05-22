class Multiplier:
    def __init__(self, factor):
        self.factor = factor  

    def __call__(self, number):
        return number * self.factor 
     
m = Multiplier(5)

print(callable(m))  

result = m(10)
print(result)   
