a = 0 
def one():
  global a 
  a = 1
  def two():
    a = 2
    print(a)
  two()
  print(a)
one()
print(a)