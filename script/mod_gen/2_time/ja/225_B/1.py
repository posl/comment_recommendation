def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    if a[0] == 1 and b[-1] == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()