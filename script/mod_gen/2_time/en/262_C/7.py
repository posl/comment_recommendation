def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)
    #aの値がiのとき、aの値がiである要素のindexをa[i]に格納する
    a_index = [0] * (N+1)
    for i in range(N):
        a_index[a[i]] = i+1
    #print(a_index)
    #aの値がiのとき、aの値がiである要素のindexのうち、最小のものをa_min[i]に格納する
    a_min = [0] * (N+1)
    for i in range(1, N+1):
        if i == 1:
            a_min[i] = a_index[i]
        else:
            a_min[i] = min(a_min[i-1], a_index[i])
    #print(a_min)
    #aの値がiのとき、aの値がiである要素のindexのうち、最大のものをa_max[i]に格納する
    a_max = [0] * (N+1)
    for i in range(N, 0, -1):
        if i == N:
            a_max[i] = a_index[i]
        else:
            a_max[i] = max(a_max[i+1], a_index[i])
    #print(a_max)
    #a_min[i] <= a_max[i]のとき、(a_min[i], a_max[i])は条件を満たす
    ans = 0
    for i in range(1, N+1):
        if a_min[i] <= a_max[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()