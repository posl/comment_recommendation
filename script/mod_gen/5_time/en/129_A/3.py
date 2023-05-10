def problems129_a():
    p,q,r = map(int, input().split())
    print(min(p+q, q+r, r+p))

if __name__ == '__main__':
    problems129_a()