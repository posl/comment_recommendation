def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(sum([max(0, v[i] - c[i]) for i in range(n)]))

if __name__ == '__main__':
    main()