def main():
    n,t = map(int,input().split())
    c = []
    c = [0]*n
    t = [0]*n
    for i in range(n):
        c[i],t[i] = map(int,input().split())
    min_cost = 1001
    for i in range(n):
        if t[i] <= t:
            min_cost = min(min_cost,c[i])
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()