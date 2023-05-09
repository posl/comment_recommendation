def main():
    N = int(input())
    L = sorted(list(map(int, input().split())), reverse=True)
    if L[0] < sum(L[1:]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()