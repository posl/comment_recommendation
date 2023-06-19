def main():
    # 读取输入
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    for i in range(1, N):
        l = 0
        while (i + l < N):
            if (S[l] != S[i + l]):
                l += 1
            else:
                break
        print(l)
    return
