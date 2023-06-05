def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = list(map(lambda x: abs(a - (t - x * 0.006)), h))
    print(h.index(min(h)) + 1)

if __name__ == '__main__':
    main()