def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    cnt += 1
                else:
                    break
    print(cnt)
main()

if __name__ == '__main__':
    main()