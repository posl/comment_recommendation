def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] < L[j] + L[k]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()