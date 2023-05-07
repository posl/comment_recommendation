def main():
    N, M = map(int, input().split())
    #print(N, M)
    if M == 0:
        print(3 ** N)
        return
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    ans = 0
    for i in range(3 ** N):
        c = []
        for j in range(N):
            c.append(i // (3 ** j) % 3)
        #print(c)
        flag = True
        for j in range(M):
            if c[A[j] - 1] == c[B[j] - 1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
