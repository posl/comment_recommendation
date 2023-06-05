def get_ans(H):
    if H < 2:
        return 1
    else:
        return 2 * get_ans(H // 2) + 1
H = int(input())
print(get_ans(H))
