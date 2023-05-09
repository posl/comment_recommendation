def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10**(N-1), 10**N):
        i = str(i)
        for j in range(M):
            if int(i[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            break
    else:
        print(-1)
