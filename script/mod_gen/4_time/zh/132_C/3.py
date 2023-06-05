def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    mid = N//2
    if d[mid] == d[mid-1]:
        print(0)
    else:
        print(d[mid]-d[mid-1])

if __name__ == '__main__':
    main()