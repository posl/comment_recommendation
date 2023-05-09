def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Aの要素をkeyとして、Aの添字をvalueとした辞書を作成
    A_dict = {A[i]:i for i in range(N)}
    # Bの要素をkeyとして、Bの添字をvalueとした辞書を作成
    B_dict = {B[i]:i for i in range(N)}
    # 1.の条件を満たす整数の個数を格納する変数
    cnt1 = 0
    # 2.の条件を満たす整数の組の個数を格納する変数
    cnt2 = 0
    # Aの要素をkeyとして、Aの添字をvalueとした辞書を順番に見ていく
    for key in A_dict:
        # Bの要素をkeyとして、Bの添字をvalueとした辞書にkeyが含まれているか
        if key in B_dict:
            # Aの添字とBの添字が一致しているか
            if A_dict[key] == B_dict[key]:
                # 一致していたら1.の条件を満たすのでカウント
                cnt1 += 1
            # 一致していない場合は2.の条件を満たすのでカウント
            else:
                cnt2 += 1
    # 答えを出力
    print(cnt1)
    print(cnt2)
main()

if __name__ == '__main__':
    main()