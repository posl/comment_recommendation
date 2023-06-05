def min_time(p,q,r):
    return min(p+q,min(q+r,p+r))

if __name__ == '__main__':
    min_time()