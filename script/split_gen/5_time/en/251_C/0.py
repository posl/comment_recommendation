def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
        t[i] = int(t[i])
    max_t = max(t)
    t2 = [0] * n
    for i in range(n):
        if t[i] == max_t:
            t2[i] = 1
    for i in range(n):
        if t2[i] == 1:
            print(i+1)
            break
