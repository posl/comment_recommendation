def get_square_number(num):
    square_num = []
    for i in range(1,num+1):
        if i*i <= num:
            square_num.append(i*i)
    return square_num

if __name__ == '__main__':
    get_square_number()