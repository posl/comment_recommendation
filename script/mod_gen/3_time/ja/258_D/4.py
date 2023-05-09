def main():
    N, X = map(int, input().split())
    stage = []
    for i in range(N):
        A, B = map(int, input().split())
        stage.append(A + B)
    stage.sort()
    count = 0
    for i in range(N):
        if X >= stage[i]:
            X -= stage[i]
            count += 1
    if X > 0:
        count -= 1
    print(count)

if __name__ == '__main__':
    main()