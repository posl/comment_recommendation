def func(n,a,b):
    result = 1
    for i in range(n):
        result *= (b[i]-a[i]+1)
    print(result%998244353)

if __name__ == '__main__':
    func()