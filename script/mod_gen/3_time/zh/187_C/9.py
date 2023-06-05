def main():
    # import sys
    # readline = sys.stdin.readline
    # readline()
    # s = set()
    # for line in sys.stdin:
    #     if line.startswith('!'):
    #         if line[1:] in s:
    #             print(line[1:])
    #             return
    #     else:
    #         if '!' + line in s:
    #             print(line)
    #             return
    #         s.add(line)
    # print('satisfiable')
    import sys
    readline = sys.stdin.readline
    readline()
    s = set()
    for line in sys.stdin:
        if line.startswith('!'):
            if line[1:] in s:
                print(line[1:])
                return
        else:
            if '!' + line in s:
                print(line)
                return
            s.add(line)
    print('satisfiable')

if __name__ == '__main__':
    main()