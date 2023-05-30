def shichi_go_san(num):
    if num < 357:
        return 0
    else:
        if '7' in str(num) and '5' in str(num) and '3' in str(num):
            return 1 + shichi_go_san(num-1)
        else:
            return shichi_go_san(num-1)
print(shichi_go_san(int(input())))
