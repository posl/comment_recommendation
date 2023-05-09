def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #a_iの値が小さい方からK人を選ぶ
    a.sort()
    #K人選べる回数
    div = K // N
    #余りの人数
    mod = K % N
    for i in range(N):
        if a[i] <= div:
            print(div)
        else:
            if i < mod:
                print(div + 1)
            else:
                print(div)
