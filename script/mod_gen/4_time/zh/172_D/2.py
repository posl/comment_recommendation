def f(x):
    return sum([i for i in range(1,x+1) if x%i==0])

if __name__ == '__main__':
    f()