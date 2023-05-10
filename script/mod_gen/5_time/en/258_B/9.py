def get_max_number(n, arr):
    max_number = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                number = get_number(n, arr, i, j, k)
                if number > max_number:
                    max_number = number
    return max_number

if __name__ == '__main__':
    get_max_number()