def main():
    #read input
    N = int(input())
    A = list(map(int, input().split()))
    #initialize
    ans = 0
    #calculate
    A = [a % 200 for a in A]
    count = [0] * 200
    for a in A:
        ans += count[a]
        count[a] += 1
    #output
    print(ans)

if __name__ == '__main__':
    main()