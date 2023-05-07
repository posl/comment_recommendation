def main():
    #入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    #解答
    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print('No War')
    else:
        print('War')
