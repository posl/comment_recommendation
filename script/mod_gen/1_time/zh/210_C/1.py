def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    max = 0
    for i in range(n-k+1):
        if len(set(c[i:i+k])) > max:
            max = len(set(c[i:i+k]))
    print(max)

if __name__ == '__main__':
    main()