def main():
    N = int(input())
    ans = "No"
    for i in range(N//4+1):
        for j in range(N//7+1):
            if 4*i+7*j == N:
                ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()