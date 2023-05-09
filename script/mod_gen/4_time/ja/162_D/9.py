def solve():
    N = int(input())
    S = input()
    
    # 2つの条件を満たす組の数を求める
    # 1つ目の条件を満たす組の数を求める
    # 2つ目の条件を満たす組の数を求める
    # 1つ目の条件を満たす組の数 - 2つ目の条件を満たす組の数
    
    # 1つ目の条件を満たす組の数を求める
    # R,G,Bの出現回数を数える
    R_cnt = 0
    G_cnt = 0
    B_cnt = 0
    for i in range(N):
        if S[i] == "R":
            R_cnt += 1
        elif S[i] == "G":
            G_cnt += 1
        else:
            B_cnt += 1
    
    # 1つ目の条件を満たす組の数を求める
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] != S[j]:
                if S[i] == "R":
                    if S[j] == "G":
                        count += B_cnt
                    else:
                        count += G_cnt
                elif S[i] == "G":
                    if S[j] == "R":
                        count += B_cnt
                    else:
                        count += R_cnt
                else:
                    if S[j] == "R":
                        count += G_cnt
                    else:
                        count += R_cnt
    
    # 2つ目の条件を満たす組の数を求める
    for i in range(N):
        for j in range(i+1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                count -= 1
    
    print(count)

if __name__ == '__main__':
    solve()