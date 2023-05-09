def main():
    N = input()
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[j] % A[i] == 0:
                    break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()