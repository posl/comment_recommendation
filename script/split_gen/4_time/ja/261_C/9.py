def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_set = set(s)
    s_dict = {}
    for i in range(n):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
            print(s[i])
        else:
            s_dict[s[i]] += 1
            print(s[i] + "(" + str(s_dict[s[i]] - 1) + ")")
