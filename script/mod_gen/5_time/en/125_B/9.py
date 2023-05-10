def max_value(n,v,c):
    v.sort(reverse=True)
    c.sort(reverse=True)
    return sum([v[i]-c[i] for i in range(n) if v[i]>c[i]])

if __name__ == '__main__':
    max_value()