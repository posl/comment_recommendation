def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    min = len_t
    for i in range(len_s-len_t+1):
        cnt = 0
        for j in range(len_t):
            if s[i+j] != t[j]:
                cnt += 1
        if cnt < min:
            min = cnt
    print(min)
