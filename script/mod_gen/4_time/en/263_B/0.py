def main():
    N = int(input())
    P = list(map(int, input().split()))
    generations = [0] * N
    for i in range(N - 1):
        generations[P[i] - 1] = generations[i] + 1
    print(max(generations) + 1)

if __name__ == '__main__':
    main()