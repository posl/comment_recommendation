def get_nearest_square_number(n):
    for i in range(1, n+1):
        if i**2 > n:
            return i-1

if __name__ == '__main__':
    get_nearest_square_number()