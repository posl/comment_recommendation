def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #print(N)
    #print(X)
    #print(Y)
    #print(S)
    #左向きの人の数
    left = 0
    #右向きの人の数
    right = 0
    #左向きの人の数が右向きの人の数より大きいときTrue
    left_gt_right = False
    #左向きの人の数が右向きの人の数より小さいときTrue
    left_lt_right = False
    for i in range(N):
        if S[i] == 'L':
            left += 1
        else:
            right += 1
        if left > right:
            left_gt_right = True
        elif left < right:
            left_lt_right = True
    #print(left)
    #print(right)
    #print(left_gt_right)
    #print(left_lt_right)
    if left_gt_right and left_lt_right:
        print('Yes')
    else:
        print('No')
