def main():
    n,t = map(int,input().split())
    c_t = []
    for i in range(n):
        c_t.append(list(map(int,input().split())))
    c_t.sort(key=lambda x:x[1])
    for i in range(n):
        if c_t[i][1] > t:
            c_t.pop(i)
            n -= 1
    if n == 0:
        print('TLE')
    else:
        print(min(c_t,key=lambda x:x[0])[0])
