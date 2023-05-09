def main():
    n = int(input())
    an = list(map(int, input().split()))
    q = int(input())
    for i in range(0,q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            an[query[1]-1] = query[2]
        else:
            print(an[query[1]-1])

if __name__ == '__main__':
    main()