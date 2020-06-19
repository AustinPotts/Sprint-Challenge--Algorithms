#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n * n * n):
      a = a + n * n
         
         This algorithm runs in O(n) 


b)  sum = 0
    for i in range(n):  # This loop is O(n)
      j = 1
      while j < n: # This loop is O(log n), why? Because with the input size growing i.e 10, J will need be multiplied 
                   # until it is more than 10
        j *= 2 
        sum += 1
        
        This algorithm runs in O(n log n) Linear Time because O(n) + O(long n) = O(n log n)
        As the size of the input increases the the runtime or space used with grow at a slight fatser rate 

# break these apart loop by loop to determine more accurate run time complexity


c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
      
      This algorithm runs in O(n) using recursion

## Exercise II

U - Phase
What are we trying to do?
A: Find out the highest floor(n) that an egg can be dropped from. If floor(n) > i.e 10: Egg Broke. 
A: If our egg is broken at the floor we are on, we need to go downstairs 
A: if our is not broken at the floor we are on, we need to go upstairs 

P - Phase

# This is a Binary Search 

Step 1. If the egg is broken when dropped from middle value of floor(n) move to the current floor - 1 then repeat until return value is egg is not broken 

// You could have just dropped from the middle & if the middle is egg not broken you can treat middle floor - n like new building 

Step 2. Do the opposite if the egg is not broken from the middle value floor(n) move to the current floor + 1 until return value is egg is broken 
Step 3. If the return value is egg is broken move to the current value floor(n) - 1 then return the value 
Run Time Complexity: O(log n) because as the size of the value of floor(n) increases, the space used will grow 
at a slightly slower rate