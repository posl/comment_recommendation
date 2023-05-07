def main():
    #入力
    N, X = map(int, input().split())
    ab = []
    for i in range(N):
        ab.append(list(map(int, input().split())))
    #print(N, X, ab)
    #処理
    ans = "No"
    for i in range(2**N):
        #print(i)
        bi = bin(i)[2:].zfill(N)
        #print(bi)
        sum = 0
        for j in range(N):
            if bi[j] == "0":
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == X:
            ans = "Yes"
            break
    #出力
    print(ans)
