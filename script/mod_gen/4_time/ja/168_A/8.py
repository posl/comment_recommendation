def solve():
    # === 数値の入力 ===
    #n = int(input())
    n = 183
    # === 行列の入力 ===
    #a = list(map(int, input().split()))
    #a = [1, 2, 3, 4, 5]
    # === 行列の入力 ===
    #a = [input() for _ in range(3)]
    #a = ['1', '2', '3']
    # === 行列の入力 ===
    #a = [list(map(int, input().split())) for _ in range(3)]
    #a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # === 行列の入力 ===
    #a = [list(input()) for _ in range(h)]
    #a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    # === 行列の入力 ===
    #a = [list(input().split()) for _ in range(h)]
    #a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    if n % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

if __name__ == '__main__':
    solve()