def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(0)
    A.append(0)
    for i in range(N):
        for j in range(i+1,N+2):
            if i == j:
                continue
            for k in range(j+1,N+3):
                if i == k or j == k:
                    continue
                if (A[i] + A[j])**2 + (A[j] + A[k])**2 == (A[i] + A[k])**2:
                    print('Yes')
                    return
    print('No')
