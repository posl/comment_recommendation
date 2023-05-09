def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(N, X)
    #print(a)
    #print(b)
    #座標0から座標Xまでの距離
    distance = X
    #print(distance)
    #座標0から座標Xまでの距離を超えるまでのジャンプ回数を求める
    for i in range(N):
        if distance <= a[i]:
            distance = distance - a[i]
        elif distance <= b[i]:
            distance = distance - b[i]
        #print(distance)
    #print(distance)
    if distance > 0:
        print("No")
    else:
        print("Yes")
