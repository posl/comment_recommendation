def main():
    n,t = map(int, input().split())
    c = [0]*n
    t = [0]*n
    for i in range(n):
        c[i],t[i] = map(int, input().split())
    min_c = 1001
    for i in range(n):
        if t[i] <= t and c[i] < min_c:
            min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)
