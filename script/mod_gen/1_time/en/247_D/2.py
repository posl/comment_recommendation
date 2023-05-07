def main():
    Q = int(input())
    cylinder = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            cylinder.extend([int(query[1])] * int(query[2]))
        else:
            print(sum(cylinder[:int(query[1])]))
            del cylinder[:int(query[1])]

if __name__ == '__main__':
    main()