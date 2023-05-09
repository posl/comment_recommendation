def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    play = T % sum_A
    for i in range(N):
        play -= A[i]
        if play <= 0:
            print(i + 1, A[i] + play)
            break

if __name__ == '__main__':
    main()