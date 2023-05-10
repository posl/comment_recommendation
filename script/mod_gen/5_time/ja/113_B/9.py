def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    diff = [abs(t - (t - h[i] * 0.006) - a) for i in range(n)]
    print(diff.index(min(diff)) + 1)

if __name__ == '__main__':
    main()