def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    min_num = 1000000
    max_num = -1
    for i in range(1,1000001):
        if A * i <= W and W <= B * i:
            min_num = min(min_num,i)
            max_num = max(max_num,i)
    if max_num == -1:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

if __name__ == '__main__':
    main()