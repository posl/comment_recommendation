def main():
    N = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(N):
        m.append(a[i])
        for j in range(i + 1, N):
            m.append(min(a[i:j + 1]))
    m.sort()
    print(m[int(len(m) / 2)])
