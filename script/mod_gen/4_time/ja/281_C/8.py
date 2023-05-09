def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % T for a in A]
    A.sort()
    A.append(A[0] + T)
    i = 0
    while A[i] < T:
        i += 1
    print(i + 1, A[i] - T)

if __name__ == '__main__':
    main()