def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[N-1] < sum(L[:N-1]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()