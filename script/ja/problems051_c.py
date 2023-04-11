#問題文
#イルカは x 軸正方向を右、y 軸正方向を上とする 2 次元座標平面にいます。
#イルカは現在点 (sx,sy) にいて、1 秒あたり上下左右に距離 1 だけ進むことができます。
#このとき、移動前と移動後の x 座標、y 座標はともに整数でなければなりません。
#イルカはここから sx < tx と sy < ty を満たす点 (tx,ty) に行き、その後点 (sx,sy) に戻り、また点 (tx,ty) に行き、その後点 (sx,sy) に戻ります。
#このとき、イルカは点 (sx,sy) と点 (tx,ty) を除いて、途中で同じ座標を複数回通らないように移動しなければなりません。
#このような条件を満たすイルカの最短経路を 1 つ求めてください。  
#
#制約
#-1000≦ sx < tx ≦1000 
#-1000≦ sy < ty ≦1000 
#sx,sy,tx,ty は整数である。
#
#入力
#入力は以下の形式で標準入力から与えられる。
#sx sy tx ty
#
#出力
#イルカの最短経路を表す文字列 S を出力せよ。
#S の i 番目の文字はイルカの i 番目の移動を表す。
#イルカの各方向への移動を表す文字の対応関係は以下のとおりである。    
#U: 上方向  
#D: 下方向  
#L: 左方向  
#R: 右方向  
#条件を満たすような最短経路が複数ある場合、そのうちどれか 1 つを出力せよ。
#
#入力例 1
#0 0 1 2
#
#出力例 1
#UURDDLLUUURRDRDDDLLU
#以下に示す移動経路が最短経路の 1 つです。  
#1 回目の (sx,sy) から (tx,ty) への移動: (0,0) → (0,1) → (0,2) → (1,2) 
#1 回目の (tx,ty) から (sx,sy) への移動: (1,2) → (1,1) → (1,0) → (0,0) 
#2 回目の (sx,sy) から (tx,ty) への移動: (0,0) → (-1,0) → (-1,1) → (-1,2) → (-1,3) → (0,3) → (1,3) → (1,2) 
#2 回目の (tx,ty) から (sx,sy) への移動: (1,2) → (2,2) → (2,1) → (2,0) → (2,-1) → (1,-1) → (0,-1) → (0,0) 
#
#入力例 2
#-2 -2 1 1
#
#出力例 2
#UURRURRDDDLLDLLULUUURRURRDDDLLDL

def 