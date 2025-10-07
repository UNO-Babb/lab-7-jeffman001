


# problem 3

import NumberTests

def main():
  total = 0

  
  for e in (range(1, 100000)):
      if NumberTests.isPrime(e):
          if 600851475143 % e == 0:
              total = e
          
        
        

    

  print(total)


if __name__ == '__main__':
  main()
