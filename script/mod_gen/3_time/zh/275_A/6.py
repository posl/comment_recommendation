def main():
    n = int(input())
    h = list(map(int, input().split()))
    h_max = max(h)
    for i in range(n):
        if h[i] == h_max:
            print(i + 1)
            break

if __name__ == '__main__':
    main()