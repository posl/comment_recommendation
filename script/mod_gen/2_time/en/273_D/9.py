def main():
    #H, W, r_s, c_s = map(int, input().split())
    #N = int(input())
    #walls = [tuple(map(int, input().split())) for _ in range(N)]
    #Q = int(input())
    #instructions = [tuple(input().split()) for _ in range(Q)]
    H, W, r_s, c_s = 6, 6, 6, 3
    N = 7
    walls = [(3, 1), (4, 3), (2, 6), (3, 4), (5, 5), (1, 1), (3, 2)]
    Q = 10
    instructions = [('D', 3), ('U', 3), ('L', 2), ('D', 2), ('U', 3), ('D', 3), ('U', 3), ('R', 3), ('L', 3), ('D', 1)]
    #H, W, r_s, c_s = 5, 5, 4, 4
    #N = 3
    #walls = [(5, 3), (2, 2), (1, 4)]
    #Q = 4
    #instructions = [('L', 2), ('U', 3), ('L', 2), ('R', 4)]
    #H, W, r_s, c_s = 10**9, 10**9, 10**9, 10**9
    #N = 0
    #walls = []
    #Q = 2*10**5
    #instructions = [('L', 10**9), ('U', 10**9)]
    #H, W, r_s, c_s = 10**9, 10**9, 1, 1
    #N = 0
    #walls = []
    #Q = 2*10**5
    #instructions = [('L', 10**9), ('U', 10**9)]
    #H, W, r_s, c_s = 10**9, 10**9, 10**9, 1
    #N = 0
    #walls = []
    #Q = 2*10**5

if __name__ == '__main__':
    main()