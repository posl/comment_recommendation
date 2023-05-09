def main():
    # input
    L, R = map(int, input().split())
    # compute
    # output
    if R <= 3:
        print('code'[L-1:R])
    elif 3 < L:
        print('atcoder'[L-1:R])
    else:
        print('code'[L-1:3] + 'atcoder'[0:R])
