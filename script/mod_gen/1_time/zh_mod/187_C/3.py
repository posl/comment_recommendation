def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s_set = set(s)
    for s_i in s:
        if s_i[0] == "!":
            if s_i[1:] in s_set:
                print(s

if __name__ == '__main__':
    main()