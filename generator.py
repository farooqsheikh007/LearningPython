def odd_generator(max):
  n=1
  while (n <= max):
    yield n
    n += 2

odd = odd_generator(10)

for i in odd:
  print(i)