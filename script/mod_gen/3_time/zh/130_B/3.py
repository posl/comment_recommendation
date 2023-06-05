def main():
    N, X = map(int, input().split())
    L = [int(x) for x in input().split()]
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([x for x in D if x <= X]))

if __name__ == '__main__':
    main()