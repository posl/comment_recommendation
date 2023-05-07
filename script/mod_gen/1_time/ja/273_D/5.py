def   main (): 
     # 入力を受け取る 
     H ,   W ,   r_s ,   c_s   =   map ( int ,   input (). split ()) 
     N   =   int ( input ()) 
     black   =   [] 
     for   _   in   range ( N ): 
         r_i ,   c_i   =   map ( int ,   input (). split ()) 
         black . append (( r_i ,   c_i )) 
     Q   =   int ( input ()) 
     LRUD   =   [] 
     for   _   in   range ( Q ): 
         d_i ,   l_i   =   input (). split () 
         LRUD . append (( d_i ,   int ( l_i ))) 
     # 高橋君の初期位置 
     r ,   c   =   r_s ,   c_s 
     # 各方向の壁までの距離 
     d   =   { 
         "L" :   c   -   1 , 
         "R" :   W   -   c , 
         "U" :   r   -   1 , 
         "D" :   H   -   r 
     } 
     # 各方向の壁までの距離を更新 
     for   d_i ,   l_i   in   LRUD : 
         d [ d_i ]   =   min ( d [ d_i ],   l_i ) 
     # 高橋君の移動 
     r   +=   d [ "D" ]   -   d [ "U" ] 
     c   +=   d [ "R" ]   -   d [ "L" ] 
     # 高橋君の移動後の位置を出力 
     print ( r ,   c ) 
     # 高橋君の移動後の位置を更新 
     r_s ,   c_s   =   r ,   c 
     # 各方向の壁までの距離を更新 
     for   d_i ,   l_i   in   LRUD : 
         d [ d_i ]   -=   l_i 
     # 高橋

if __name__ == '__main__':
    ()