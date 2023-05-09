def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = max(h)
    for i in range(n):
        if h[i] == max_h:
            print(i+1)
            break

if __name__ == '__main__':
    main()