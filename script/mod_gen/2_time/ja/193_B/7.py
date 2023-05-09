def main():
    N = int(input())
    answer = []
    for i in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            answer.append(P)
    if answer:
        print(min(answer))
    else:
        print(-1)

if __name__ == '__main__':
    main()