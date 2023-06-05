def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    i = 0
    j = 0
    count = 0
    while i < N and j < N:
        if a[i] == j + 1:
            i += 1
        elif b[j] == i + 1:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    print(count)
