def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 200で割った余りをキーとした辞書を作成
    mod_dict = {}
    for i in range(N):
        mod = A[i] % 200
        if mod in mod_dict:
            mod_dict[mod] += 1
        else:
            mod_dict[mod] = 1
    
    # 余りが同じものの組み合わせの数を求める
    sum = 0
    for i in mod_dict.values():
        sum += i * (i - 1) // 2
    
    print(sum)

if __name__ == '__main__':
    main()