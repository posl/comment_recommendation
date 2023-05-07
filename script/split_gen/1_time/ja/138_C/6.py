def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N - 1):
        v.append((v[i] + v[i + 1]) / 2)
        v.sort()
    print(v[-1])
