def main():
    #Enter your code here. Read input from STDIN. Print output to STDOUT
    N = int(input())
    lst = []
    for i in range(N):
        lst.append([x for x in input().split()])
        lst[i][1] = int(lst[i][1])
    lst.sort(key = lambda x:x[1], reverse = True)
    print(lst[1][0])

if __name__ == '__main__':
    main()