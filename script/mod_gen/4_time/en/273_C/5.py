def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0 for i in range(N)]
    count = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ans[count-1] += 1
            count = 1
        else:
            count += 1
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()