def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    maxL = L.pop()
    if maxL < sum(L):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()