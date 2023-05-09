def main():
    N=int(input())
    A=list(map(int,input().split()))
    # 偶数の数を数える
    cnt_even=0
    for a in A:
        if a%2==0:
            cnt_even+=1
    if cnt_even%2==0:
        print(-1)
    else:
        print(max(A))

if __name__ == '__main__':
    main()