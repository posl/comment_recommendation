def main():
    # put your code here
    N, X = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    print(sum(1 for i in D if i <= X))

if __name__ == '__main__':
    main()