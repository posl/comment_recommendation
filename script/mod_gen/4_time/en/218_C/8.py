def rotate ( grid ): 
     N = len ( grid ) 
     return [ [ grid [ N - 1 - j ][ i ] for j in range ( N )] for i in range ( N )] 
 def translate ( grid ,  dx ,  dy ): 
     N = len ( grid ) 
     return [ [ grid [ ( i + dx ) % N ][ ( j + dy ) % N ] for j in range ( N )] for i in range ( N )] 
 def solve ( grid1 ,  grid2 ): 
     N = len ( grid1 ) 
     for dx in range ( N ): 
         for dy in range ( N ): 
             for _ in range ( 4 ): 
                 if  grid1  ==  grid2 : 
                     return  True 
                 grid1  =  rotate ( grid1 ) 
             grid1  =  translate ( grid1 ,  dx ,  dy ) 
     return  False 
 N  = int ( input ()) 
 grid1  = [ list ( input ()) for _ in range ( N )] 
 grid2  = [ list ( input ()) for _ in range ( N )] 
 print ( 'Yes'   if  solve ( grid1 ,  grid2 )   else   'No' )

if __name__ == '__main__':
    rotate()