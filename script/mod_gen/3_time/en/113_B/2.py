def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    print(h.index(min(h, key=lambda x: abs(a - (t - x * 0.006)))))

if __name__ == '__main__':
    main()