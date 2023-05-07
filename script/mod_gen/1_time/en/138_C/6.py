def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    max_v = v[-1]
    for i in range(n-1):
        max_v = (max_v + v[i]) / 2
    print(max_v)

if __name__ == '__main__':
    main()