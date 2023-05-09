def main():
    X, Y, A, B = map(int, input().split())
    #Aで進める回数を求める
    num_A = 0
    tmp = X
    while tmp * A < Y:
        num_A += 1
        tmp *= A
    #Bで進める回数を求める
    num_B = (Y - X - 1) // B
    #Aで進める回数が多い場合は、Aで進める回数を出力する
    if num_A >= num_B:
        print(num_A)
    #Bで進める回数が多い場合は、Aで進める回数とBで進める回数の和を出力する
    else:
        print(num_A + num_B)
