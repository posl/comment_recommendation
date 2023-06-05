def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - x * 0.006 for x in h]
    h = [abs(a - x) for x in h]
    print(h.index(min(h)) + 1)

if __name__ == '__main__':
    main()