def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([list(map(int, input().split())) for j in range(int(input()))])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                for k in A[j]:
                    if (i >> (k[0]-1)) & 1 != k[1]:
                        flag = False
                        break
                if not flag:
                    break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
