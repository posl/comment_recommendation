def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    Lmax = L.pop(0)
    Lsum = sum(L)
    if Lmax < Lsum:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()