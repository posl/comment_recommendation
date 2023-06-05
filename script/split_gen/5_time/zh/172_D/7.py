def f(x):
    #xの正除数の和を求める
    return sum([i for i in range(1,x+1) if x%i==0])
