#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n * n * n):
      a = a + n * n
         
         This algorithm runs in O(1) Constant Time, there is only one execution happening.


b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2 sum += 1
        
        This algorithm runs in O(n) Linear Time, with the increase of input size space used will grow at the same rate



c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
      
      This algorithm runs in O(1) Constant Time, there is only one execution happening. Space used will be unaffected by the size of the input

## Exercise II

U - Phase
What are we trying to do?
A: Find out the highest floor(n) that an egg can be dropped from. If floor(n) > i.e 10: Egg Broke. 
A: If our egg is broken at the floor we are on, we need to go downstairs 
A: if our is not broken at the floor we are on, we need to go upstairs 

P - Phase
Step 1. If the egg is broken when dropped from middle value of floor(n) move to the current floor - 1 then repeat until return value is egg is not broken 
Step 2. Do the opposite if the egg is not broken from the middle value floor(n) move to the current floor + 1 until return value is egg is broken 
Step 3. If the return value is egg is broken move to the current value floor(n) - 1 then return the value 
Run Time Complexity: O(log n) because as the size of the value of floor(n) increases, the space used will grow 
at a slightly slower rate