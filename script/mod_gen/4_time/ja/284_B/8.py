def main():
    # input
    T = int(input())
    ans = []
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        # compute
        odd = 0
        for a in A:
            if a % 2 == 1:
                odd += 1
        ans.append(odd)
    # output
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()