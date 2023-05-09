def main():
    N, Q = map(int, input().split())
    anslist = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            pass
        elif query[0] == 2:
            pass
        else:
            anslist.append(query[1])
    print(anslist)
    return

if __name__ == '__main__':
    main()