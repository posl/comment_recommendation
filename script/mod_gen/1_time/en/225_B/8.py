def main():
    N = int(input())
    #print(N)
    a = []
    b = []
    for i in range(N-1):
        ab = input().split()
        #print(ab)
        a.append(int(ab[0]))
        b.append(int(ab[1]))
    #print(a)
    #print(b)
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    if a[0]==1 and b[0]==1 and a[-1]==a[0] and b[-1]==b[0]:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()