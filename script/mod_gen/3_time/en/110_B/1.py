def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    a.sort()
    b.sort()
    if a[-1] >= b[0]:
        print("War")
    else:
        print("No War")

if __name__ == '__main__':
    main()