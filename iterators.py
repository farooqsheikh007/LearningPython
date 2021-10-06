# an object to be called an iterator it should have 2

class Odd:
  def __init__(self,max):
    self.n = 1
    self.max = max
  def __iter__(self):
    return self
  def __next__(self):
    if(self.n <= self.max):
      item = self.n
      self.n += 2
      return item
    else:
      raise StopIteration 

odds = Odd(10)

print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
