def problems135_a(a,b):
    if (a+b)%2 == 0:
        return int((a+b)/2)
    else:
        return "IMPOSSIBLE"

if __name__ == '__main__':
    problems135_a()