def median(a):
    a.sort()
    return a[(len(a)-1)/2]

if __name__ == '__main__':
    median()