def route_time(p,q,r):
    return min(p+q,q+r,r+p)

if __name__ == '__main__':
    route_time()