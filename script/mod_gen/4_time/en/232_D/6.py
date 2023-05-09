def main():
    # Take input Here and Call solution function
    H, W = get_ints_in_variables()
    arr = get_list_of_list_in_variable(H)
    # print(H, W, arr)
    print(solution(H, W, arr))

if __name__ == '__main__':
    main()