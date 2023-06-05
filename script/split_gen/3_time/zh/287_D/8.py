def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        print("No\n" * (len_t + 1))
        return
    s = list(s)
    t = list(t)
    for i in range(len_s - len_t + 1):
        for j in range(len_t):
            if s[i + j] != t[j] and s[i + j] != "?":
                break
        else:
            print("Yes\n" * (i + 1) + "No\n" * (len_t - i) + "Yes\n" * (len_s - len_t - i))
            return
    print("No\n" * (len_t + 1))
