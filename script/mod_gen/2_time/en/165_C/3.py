def main():
    N, M, Q = map(int, input().split())
    questions = [list(map(int, input().split())) for _ in range(Q)]
    print(solver(N, M, Q, questions))

if __name__ == '__main__':
    main()