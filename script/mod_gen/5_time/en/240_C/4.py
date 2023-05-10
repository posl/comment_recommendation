def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) <= x and x <= sum(b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()