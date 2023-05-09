def   is_contiguous_substring ( s ,   t ): 
     if   s   ==   t : 
         return   'Yes' 
     if   len ( s )   <   len ( t ): 
         return   'No' 
     if   s [ 0 ]   ==   t [ 0 ]: 
         return   is_contiguous_substring ( s [ 1 :],   t [ 1 :]) 
     if   s [ - 1 ]   ==   t [ 0 ]: 
         return   is_contiguous_substring ( s [ 0 : - 1 ],   t [ 1 :]) 
     return   'No'
