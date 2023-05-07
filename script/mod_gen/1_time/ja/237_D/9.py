def main():
    N = int(input())
    S = input()
    #A = [0 for i in range(N+1)]
    A = [0] * (N+1) # こっちの書き方の方が早い
    l = 0
    r = N
    for i in range(N):
        if S[i] == 'L':
            A[l] = i+1
            l += 1
        else:
            A[r] = i+1
            r -= 1
    print(*A)

if __name__ == '__main__':
    main()