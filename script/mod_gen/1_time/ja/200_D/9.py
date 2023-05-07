def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    # 2つの数列の組み合わせがあるか
    # 1つの数列の中に200の倍数があるか
    # 2つの数列の中に200の倍数があるか
    # それ以外
    # という3つの場合に分けて考える
    # 1つの数列の中に200の倍数がある場合
    for i in range(N):
        if A[i] % 200 == 0:
            print('Yes')
            print(1)
            print(i+1)
            print(1)
            print(i+1)
            return
    # 2つの数列の中に200の倍数がある場合
    for i in range(N):
        for j in range(i+1,N):
            if (A[i] + A[j]) % 200 == 0:
                print('Yes')
                print(1)
                print(i+1)
                print(2)
                print(i+1, j+1)
                return
    # それ以外
    # 1つの数列の中に200の倍数がない場合
    # 2つの数列の中に200の倍数がない場合
    # 2つの数列の中に200の倍数がある場合
    # という4つの場合に分けて考える
    # 2つの数列の中に200の倍数がある場合
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (A[i] + A[j] + A[k]) % 200 == 0:
                    print('Yes')
                    print(2)
                    print(i+1, j+1)
                    print(1)
                    print(k+1)
                    return
    # 1つの数列の中に200の倍数がない場合
    # 2つの数列の中に200

if __name__ == '__main__':
    main()