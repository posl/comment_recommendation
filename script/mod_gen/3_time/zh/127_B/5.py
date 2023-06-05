def sum(i,r):
    if i > 2000:
        return r*sum(i-1,r)-10
    else:
        return 20

if __name__ == '__main__':
    sum()