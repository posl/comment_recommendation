def get_min_route_time(p,q,r):
    times = []
    times.append(p+q)
    times.append(q+r)
    times.append(r+p)
    return min(times)
