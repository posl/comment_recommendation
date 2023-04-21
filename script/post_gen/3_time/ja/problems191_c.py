#問題文
#H 行 W 列のマス目があります。このマス目の、上から i 番目、左から j 番目のマスを、マス (i, j) と呼ぶことにします。
#各マスは黒または白に塗られています。S_{i, j} が # ならばマス (i, j) は黒に塗られており、. ならば白に塗られています。
#マス目の一番外側のマス、すなわち (1, j), (H, j), (i, 1), (i, W) のいずれかの形で表されるマスは白に塗られていることが保証されます。  
#黒に塗られた部分を多角形として見たとき、これが (最小で) 何角形になるかを求めてください。  
#ここで、黒に塗られた部分は一つの自己交叉のない多角形となることが保証されます。すなわち、以下のことが保証されます。  
#黒に塗られたマスが少なくとも一つ存在する
#黒に塗られた任意の 2 マスは、辺を共有するマスへの移動を繰り返し、黒に塗られたマスのみを通って互いに到達可能である
#白に塗られた任意の 2 マスは、辺を共有するマスへの移動を繰り返し、白に塗られたマスのみを通って互いに到達可能である(マス目の一番外側のマスは全て白に塗られていることに注意してください)
#
#制約
#3 ≦ H ≦ 10
#3 ≦ W ≦ 10
#S_{i, j} は # または .
#S_{1, j}, S_{H, j} は .
#S_{i, 1}, S_{i, W} は .
#黒に塗られた部分は一つの自己交叉のない多角形となる
#
#入力
#入力は以下の形式で標準入力から与えられる。
#H W
#S_{1, 1} S_{1, 2} S_{1, 3} ... S_{1, W}
#S_{2, 1} S_{2, 2} S_{2, 3} ... S_{2, W}
#S_{3, 1} S_{3, 2} S_{3, 3} ... S_{3, W}
#.
#.
#.
#S_{H, 1} S_{H, 2} S_{H, 3} ... S_{H, W}
#
#出力
#黒に塗られた部分を n 角形として見ることができるような最小の n を出力せよ。  
#
#入力例 1
#5 5
#.....
#.###.
#.###.
#.###.
#.....
#
#出力例 1
#4
#マス目の左上、左下、右上、右下の隅をそれぞれ (0, 0), (H, 0), (0, W), (H, W) とする座標系で表すと、与えられる図形は (1, 1), (4, 1), (4, 4), (1, 4) を頂点とする 4 角形です。  

def 