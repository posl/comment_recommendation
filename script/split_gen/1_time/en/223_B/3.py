def main():
    s = input()
    n = len(s)
    s_list = [s]
    for i in range(1,n):
        s_list.append(s[i:] + s[:i])
    print(min(s_list))
    print(max(s_list))
