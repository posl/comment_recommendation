def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    PQX = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(AB)
    #print(PQX)
    #print('-----')
    # [i] = [i] + [i - 1]
    # [i] = [i] + [i + 1]
    # [i] = [i] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 7] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i] + [i - 8] + [i - 7] + [i - 6] + [i - 5] + [i - 4] + [i - 3] + [i - 2] + [i - 1] + [i + 1]
    # [i] = [i

if __name__ == '__main__':
    main()