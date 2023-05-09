def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if A[-1] > B[-1]:
        print(0)
    else:
        print(B[-1] - A[-1] + 1)

if __name__ == '__main__':
    main()