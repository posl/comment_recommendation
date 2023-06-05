def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s_t = list(zip(s, t))
    s_t.sort(key=lambda x: x[1])
    s_t.sort(key=lambda x: x[0])
    # print(s_t)
    for i in range(n):
        if i == 0:
            print(s_t[i][1])
        else:
            if s_t[i][0] == s_t[i - 1][0]:
                print(s_t[i - 1][1])
            else:
                print(s_t[i][1])
