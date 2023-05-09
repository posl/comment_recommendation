def main():
    n,x = map(int, input().split())
    a_list = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += a_list[i]
        else:
            total += a_list[i] - 1
    if total <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()