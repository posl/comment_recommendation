def main():
    n = int(input())
    doublets = 0
    for _ in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            doublets += 1
        else:
            doublets = 0
        if doublets >= 3:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()