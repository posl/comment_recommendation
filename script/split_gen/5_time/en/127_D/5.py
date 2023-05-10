def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for i in range(M):
        BC.append(tuple(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for j in range(b):
            if i >= N or A[i] >= c:
                break
            A[i] = c
            i += 1
        else:
            continue
        break
    print(sum(A))
