def main():
    n, w = map(int, input().split())
    use = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        use[s] += p
        use[t] -= p
    for i in range(1, 200001):
        use[i] += use[i-1]
        if use[i] > w:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()