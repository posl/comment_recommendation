def main():
    N = int(input())
    x = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    ans3 = 0
    for i in range(N):
        ans1 += abs(x[i])
        ans2 += abs(x[i])**2
        ans3 = max(ans3, abs(x[i]))
    ans2 = ans2**0.5
    print(ans1)
    print(ans2)
    print(ans3)

if __name__ == '__main__':
    main()