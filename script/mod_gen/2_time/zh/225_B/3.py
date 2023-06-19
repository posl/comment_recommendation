def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[0] == 1:
        for i in range(1, N):
            if a[i] != i+1:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()