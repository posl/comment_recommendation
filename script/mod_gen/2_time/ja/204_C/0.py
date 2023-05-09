def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    
    # 1からNの都市の組み合わせの数をカウントする
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            # 道路がない場合はカウントしない
            for k in range(M):
                if (A[k] == i and B[k] == j) or (A[k] == j and B[k] == i):
                    count += 1
                    break
    
    print(count)

if __name__ == '__main__':
    main()