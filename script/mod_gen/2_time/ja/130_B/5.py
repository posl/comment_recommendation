def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    count = 0
    for i in range(N):
        if D[i] + L[i] <= X:
            D.append(D[i] + L[i])
            count += 1
        else:
            break
    print(count + 1)

if __name__ == '__main__':
    main()