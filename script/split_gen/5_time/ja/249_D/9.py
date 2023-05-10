def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 0
    i = 0
    j = 0
    k = 1
    while i < N:
        if A[i] == A[i+1]:
            j += 1
            i += 1
        else:
            cnt += (j+1) * j // 2
            j = 0
            i += 1
    print(cnt)
