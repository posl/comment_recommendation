def get_median(a,b):
    c = a + b
    c.sort()
    return c[len(c)//2]

if __name__ == '__main__':
    get_median()