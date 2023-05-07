def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int,input().split())
    if N == 3:
        if a[0] == a[1] or a[0] == b[1] or b[0] == a[1] or b[0] == b[1]:
            print("Yes")
        else:
            print("No")
    else:
        if a.count(1) == 1:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()