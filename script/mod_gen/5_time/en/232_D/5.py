def main():
    # Take input Here and Call solution function
    h, w = get_ints_in_variables()
    matrix = []
    for i in range(h):
        matrix.append(get_string())
    print(solution(h, w, matrix))

if __name__ == '__main__':
    main()