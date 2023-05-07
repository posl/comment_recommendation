def main():
    # initialize
    N, Q = map(int, input().split())
    # swap_list = [0] * (N+1)
    swap_list = [i+1 for i in range(N)]
    swap_list[0] = 0
    swap_list[N] = 0
    # print(swap_list)
    for i in range(Q):
        x = int(input())
        # print("x=", x)
        # swap_list[x], swap_list[x+1] = swap_list[x+1], swap_list[x]
        # print("swap_list=", swap_list)
        swap_list[x], swap_list[x+1] = swap_list[x+1], swap_list[x]
        # print("swap_list=", swap_list)
    # print(swap_list)
    # print("swap_list[1:]= ", swap_list[1:])
    # print(*swap_list[1:])
    print(*swap_list[1:])

if __name__ == '__main__':
    main()