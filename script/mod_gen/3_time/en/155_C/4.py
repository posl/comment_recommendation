def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    s_dict = {}
    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    max_value = max(s_dict.values())
    for key, value in s_dict.items():
        if value == max_value:
            print(key)

if __name__ == '__main__':
    main()