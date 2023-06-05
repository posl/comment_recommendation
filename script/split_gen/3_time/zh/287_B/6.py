def main():
    n,m = map(int,input().split())
    a = [input() for i in range(n)]
    b = [input() for i in range(m)]
    c = 0
    for i in a:
        for j in b:
            if i[-3:] == j:
                c += 1
    print(c)
