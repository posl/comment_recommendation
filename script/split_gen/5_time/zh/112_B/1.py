def main():
    N, T = map(int, input().split())
    c_t = []
    for i in range(N):
        c_t.append(list(map(int, input().split())))
    c_t.sort(key=lambda x:x[1])
    for i in range(N):
        if c_t[i][1] <= T:
            print(c_t[i][0])
            return
    print("TLE")
