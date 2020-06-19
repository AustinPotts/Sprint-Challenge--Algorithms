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


