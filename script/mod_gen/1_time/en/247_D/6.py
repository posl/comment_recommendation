def main():
    import sys
    readline = sys.stdin.readline
    Q = int(readline())
    cylinder = []
    for _ in range(Q):
        query = readline().split()
        if query[0] == '1':
            for i in range(int(query[2])):
                cylinder.append(int(query[1]))
        else:
            print(sum(cylinder[:int(query[1])]))
            cylinder = cylinder[int(query[1]):]
main()

if __name__ == '__main__':
    main()