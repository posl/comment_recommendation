def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    num = 0
    for i in range(N):
        if (i+1) != p[i]:
            num += 1
    if num == 0 or num == 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()