def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    pre = 0
    cnt = 0
    for i in range(N):
        if A[i] == pre:
            continue
        else:
            pre = A[i]
            cnt += 1
    print(cnt)
