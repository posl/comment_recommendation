def main():
    N = int(input())
    L = list(map(int, input().split()))
    #print(N)
    #print(L)
    L.sort(reverse=True)
    #print(L)
    longest = L[0]
    #print(longest)
    others = sum(L[1:])
    #print(others)
    if longest < others:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()