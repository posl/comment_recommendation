def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t.pop()
        else:
            oven2 += t.pop()
    print(max(oven1, oven2))

if __name__ == '__main__':
    main()