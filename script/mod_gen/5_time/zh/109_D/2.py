def get_even_num(H, W, a_list):
    even_num = 0
    for i in range(H):
        for j in range(W):
            if a_list[i][j] % 2 == 0:
                even_num += 1
    return even_num

if __name__ == '__main__':
    get_even_num()