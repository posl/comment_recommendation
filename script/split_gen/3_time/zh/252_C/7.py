def main():
    n = int(input())
    s = [input() for i in range(n)]
    #print(s)
    t = 0
    while True:
        t += 1
        for i in range(n):
            if s[i][t % 10] == s[i][0]:
                continue
            else:
                break
        else:
            break
    print(t)
