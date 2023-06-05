def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # print(s)
    min_t = 0
    for i in range(n):
        s1 = s[i]
        for j in range(n):
            s2 = s[j]
            if i != j:
                # print(s1, s2)
                for t in range(10):
                    # print(t)
                    cnt = 0
                    for k in range(10):
                        # print(t, k)
                        if s1[k] == s2[(t + k) % 10]:
                            cnt += 1
                        else:
                            break
                    if cnt == 10:
                        break
                # print(t)
                if min_t < t:
                    min_t = t
    print(min_t)
