def median(x):
    x.sort()
    return x[int((len(x)-1)/2)]

if __name__ == '__main__':
    median()