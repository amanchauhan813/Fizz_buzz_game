#write a code in python in which you can get “Fizz Buzz” for 
#all numbers which can be divided by (3, 5, 15).
#The range should from (1 to 100).

#class Fizz:
 #   def __init__(self) -> None:
  #      pass

for i in range(1,100):
    if i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(i)