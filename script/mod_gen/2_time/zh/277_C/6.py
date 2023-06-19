def main():
    N = int(input())
    #print(N)
    #print(type(N))
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    #print(A)
    #print(B)
    #print(type(A))
    #print(type(B))
    #print(max(A))
    #print(min(B))
    if max(A) <= min(B):
        print(min(B) - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()