def problems115_b():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(p[0]//2 + sum(p[1:]))

if __name__ == '__main__':
    problems115_b()