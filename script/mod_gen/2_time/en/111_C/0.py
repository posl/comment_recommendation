def   main (): 
     n   =   int ( input ()) 
     v   =   list ( map ( int ,   input (). split ())) 
     v1   =   v [:: 2 ] 
     v2   =   v [ 1 :: 2 ] 
     v1_dict   =   {} 
     v2_dict   =   {} 
     v1_max   =   0 
     v1_max_num   =   0 
     v2_max   =   0 
     v2_max_num   =   0 
     v1_max2   =   0 
     v2_max2   =   0 
     for   i   in   range ( n // 2 ): 
         if   v1 [ i ]   in   v1_dict : 
             v1_dict [ v1 [ i ]]   +=   1 
         else : 
             v1_dict [ v1 [ i ]]   =   1 
         if   v2 [ i ]   in   v2_dict : 
             v2_dict [ v2 [ i ]]   +=   1 
         else : 
             v2_dict [ v2 [ i ]]   =   1 
     for   key ,   value   in   v1_dict . items (): 
         if   v1_max   <   value : 
             v1_max   =   value 
             v1_max_num   =   key 
         elif   v1_max2   <   value : 
             v1_max2   =   value 
     for   key ,   value   in   v2_dict . items (): 
         if   v2_max   <   value : 
             v2_max   =   value 
             v2_max_num   =   key 
         elif   v2_max2   <   value : 
             v2_max2   =   value 
     if   v1_max_num   ==   v2_max_num : 
         print ( min ( n - v1_max - v2_max2 ,   n - v1_max2 - v2_max )) 
     else : 
         print ( n - v1_max - v2_max )
