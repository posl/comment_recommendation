def price(n,a,x,y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

if __name__ == '__main__':
    price()