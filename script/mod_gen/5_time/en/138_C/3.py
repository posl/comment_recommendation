def main():
    n = int(input())
    v = sorted(list(map(int, input().split())))
    for i in range(n-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[-1])

if __name__ == '__main__':
    main()