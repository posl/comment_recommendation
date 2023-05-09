def main():
    N = int(input())
    ans = "No"
    for i in range(N-2):
        D = [int(x) for x in input().split()]
        if D[0] == D[1]:
            D = [int(x) for x in input().split()]
            if D[0] == D[1]:
                D = [int(x) for x in input().split()]
                if D[0] == D[1]:
                    ans = "Yes"
                    break
    print(ans)

if __name__ == '__main__':
    main()