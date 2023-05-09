def  solve ( k ): 
     lunlun_numbers  =  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ] 
     if  k  <=  len ( lunlun_numbers ): 
         return  lunlun_numbers [ k - 1 ] 
     while  k  >  len ( lunlun_numbers ): 
         new_lunlun_numbers  =  [] 
         for  i  in  range ( len ( lunlun_numbers )): 
             lunlun_number  =  lunlun_numbers [ i ] 
             last_digit  =  lunlun_number  %  10 
             if  last_digit  >  0 : 
                 new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit  -  1 ) 
             new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit ) 
             if  last_digit  <  9 : 
                 new_lunlun_numbers . append ( lunlun_number  *  10  +  last_digit  +  1 ) 
         lunlun_numbers  =  new_lunlun_numbers 
     return  lunlun_numbers [ k - 1 ]

if __name__ == '__main__':
    ()