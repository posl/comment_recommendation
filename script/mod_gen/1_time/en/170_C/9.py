def  main():
     # Read a list of integers, 2 in this case
     x, n = [ int (x) for  x in  input().split()]
     p = [ int (x) for  x in  input().split()]
    
     # We will store the nearest integer in this variable
     nearest =  0 
    
     # We will keep track of the minimum difference between X and the nearest integer in this variable
     min_diff =  100 
    
     # The range of integers we will consider is from 1 to 100
     for  i in  range( 1 ,  101 ):
         # If i is not in the list p, we will consider it
          if  i not in p:
             # Compute the difference between X and i
              diff = abs(x - i)
             # If the difference is smaller than the minimum difference we have seen so far, update the minimum difference and the nearest integer
              if  diff < min_diff:
                min_diff = diff
                nearest = i
    
     # Print the answer
      print(nearest)

if __name__ == '__main__':
    ()