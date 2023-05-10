def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c_i, t_i = map(int, input().split())
        c.append([c_i, t_i])
    
    c.sort(key=lambda x: x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            return
    print("TLE")
