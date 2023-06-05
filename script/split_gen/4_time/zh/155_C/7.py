def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    s_max = 1
    s_max_list = []
    for i in range(n-1):
        if s[i] == s[i+1]:
            s_max += 1
        else:
            if s_max > 1:
                s_max_list.append(s[i])
            s_max = 1
    if s_max > 1:
        s_max_list.append(s[-1])
    for i in s_max_list:
        print(i)
