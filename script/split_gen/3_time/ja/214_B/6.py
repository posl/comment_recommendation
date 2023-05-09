def main():
    #入力
    S, T = map(int, input().split())
    #計算
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    #出力
    print(count)
