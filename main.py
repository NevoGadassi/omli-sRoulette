import random
pool = [i for i in range(1,16)]

text = True
while text != 'exit':
 number = random.choice(pool)
 print(number)
 pool.remove(number)
 text = input('next number?')
 if text == 'n':
   for _ in range(100):
     print("")
   text = input("yalla benadam haba?")
