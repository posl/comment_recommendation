def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    print("Yes" if L[0] < sum(L[1:]) else "No")

if __name__ == '__main__':
    main()