
#Problem #5 from project Euler
import NumberTests


def main():
  total = 0

  
  for e in (range(20, 300000000, 20)): #has to be divisible by 20 so increases speed immensly just to jump by that much 
      if NumberTests.isEven(e) and NumberTests.isThreeOrFive(e):  #to help speed up sifting
         set = 0   #to make sure set resets everytime e changes
         for i in range(1, 20): #e should be the same throughout this process
            if e % i == 0:
               set = set + 1 #I tried just having if it got past this to set e to the value, but since it starts with one, it just finished without checking all, this makes it have to run through all numbers 1-20
               if set == 19: #19 because it starts at 1
                  total = e
                  
             
          
        
        

    

  print(total)


if __name__ == '__main__':
  main()