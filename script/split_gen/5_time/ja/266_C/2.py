def check_convex(a,b,c,d):
    # a,b,c,dの4点を順番に見ていく
    # a,b,c,dが反時計回りであるとき、a,b,c,dの順番になっているとき、a,b,d,cの順番になっているとき、a,c,b,dの順番になっているとき、a,c,d,bの順番になっているとき、a,d,b,cの順番になっているとき、a,d,c,bの順番になっているとき、
    # この8パターンある
    # この8パターンのうち、1つでも凸であれば凸である
    # 1つも凸でなければ凸でない
    # まず、a,b,c,dが反時計回りであるかを調べる
    # つまり、a,b,c,dを順番に見ていったとき、a,b,cの順番になっているかを調べる
    # つまり、(c-b)×(b-a)のz成分が正かを調べる
    # つまり、(c[0]-b[0])*(b[1]-a[1]) - (c[1]-b[1])*(b[0]-a[0])が正かを調べる
    # つまり、(c[0]-b[0])*(b[1]-a[1]) > (c[1]-b[1])*(b[0]-a[0])が正かを調べる
    # つまり、(c[0]-b[0])*(b[1]-a[1]) - (c[1]-b[1])*(b[0]-a[0]) > 0が正かを調べる
    # つまり、(c[0]-b[0])*(b[1]-a[1]) - (c[1]-b
