def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, x, y)
    #print(A)
    A.append(0)
    A.insert(0, 0)
    #print(A)
    for i in range(1, N+1):
        for j in range(i+1, N+2):
            #print(i, j)
            if abs(A[i]-A[j]) + abs(i-j) == abs(x-y):
                print("Yes")
                exit()
    print("No")
