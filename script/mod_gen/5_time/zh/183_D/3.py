def main():
    n, w = map(int, input().split())
    p = [0] * 200001
    for i in range(n):
        s, t, c = map(int, input().split())
        p[s] += c
        p[t] -= c
    for i in range(200000):
        p[i + 1] += p[i]
    if max(p) <= w:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()