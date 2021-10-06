def fibonacci():
  one = 0
  two = 1
  while True:
    yield one
    one,two = two, one + two

fib = fibonacci()

for i in fib:
  if i >= 100:
    break
  print(i)
