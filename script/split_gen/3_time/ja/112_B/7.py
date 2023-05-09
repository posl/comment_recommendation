def main():
    n, t = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    for i in range(n):
        if l[i][1] <= t:
            print(l[i][0])
            exit()
    print("TLE")
