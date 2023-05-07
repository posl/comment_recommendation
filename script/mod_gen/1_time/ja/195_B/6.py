def main():
    A,B,W = map(int, input().split())
    W = W * 1000
    #print(A)
    #print(B)
    #print(W)
    min = 0
    max = 0
    for i in range(1, W+1):
        if A*i <= W and W <= B*i:
            min = i
            break
    for i in range(W, 0, -1):
        if A*i <= W and W <= B*i:
            max = i
            break
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()