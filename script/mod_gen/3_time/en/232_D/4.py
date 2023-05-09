def main():
    # Take input Here and Call solution function
    h,w = get_ints_in_variables()
    grid = []
    for i in range(h):
        grid.append(get_string())
    print(solution(h,w,grid))

if __name__ == '__main__':
    main()