def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[-1] < sum(L[:-1]):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()