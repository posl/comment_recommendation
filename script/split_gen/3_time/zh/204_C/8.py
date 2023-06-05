def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                if i in A and j in B:
                    count += 1
    print(count)
