def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "Yes"
    for i in range(N):
        if A[i] > x or A[i] > y:
            ans = "No"
            break
        if i == 0:
            x -= A[i]
        else:
            if A[i] > x:
                ans = "No"
                break
            else:
                x -= A[i]
            if A[i] > y:
                ans = "No"
                break
            else:
                y -= A[i]
    print(ans)

if __name__ == '__main__':
    main()