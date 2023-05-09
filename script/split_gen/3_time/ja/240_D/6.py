def   main (): 
     N   =   int ( input ()) 
     a   =   list ( map ( int ,   input (). split ())) 
     cnt   =   0 
     cnt_list   =   [] 
     for   i   in   range ( N ): 
         if   i   ==   0 : 
             cnt   =   1 
         else : 
             if   a [ i ]   ==   a [ i - 1 ]: 
                 cnt   +=   1 
             else : 
                 cnt_list . append ( cnt ) 
                 cnt   =   1 
     cnt_list . append ( cnt ) 
     # print(cnt_list) 
     ans   =   [] 
     for   i   in   range ( N ): 
         if   i   ==   0 : 
             ans . append ( 1 ) 
         else : 
             if   a [ i ]   ==   a [ i - 1 ]: 
                 ans . append ( ans [ i - 1 ] + 1 ) 
             else : 
                 ans . append ( 1 ) 
     # print(ans) 
     for   i   in   range ( N ): 
         if   i   ==   0 : 
             print ( ans [ i ]) 
         else : 
             if   cnt_list [ i - 1 ]   ==   1 : 
                 print ( ans [ i ]) 
             else : 
                 if   ans [ i ]   ==   cnt_list [ i - 1 ]: 
                     print ( ans [ i ] - 1 ) 
                 else : 
                     print ( ans [ i ])
