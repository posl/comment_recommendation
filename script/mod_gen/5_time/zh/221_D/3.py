def main():
    n = int(input())
    dict = {}
    for i in range(n):
        a,b = map(int,input().split())
        for j in range(a,a+b):
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    for i in range(1,n+1):
        if i in dict:
            print(dict[i],end=" ")
        else:
            print(0,end=" ")

if __name__ == '__main__':
    main()