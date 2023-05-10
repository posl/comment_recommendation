def main():
    s = input()
    s_list = []
    for i in s:
        s_list.append(i)
    s_set = set(s_list)
    print(len(s_set))

if __name__ == '__main__':
    main()