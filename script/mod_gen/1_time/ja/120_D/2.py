def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(N, M)
    # print(A)
    # print(B)
    # print("===")
    # 1. まず、すべての島がつながっていると仮定して、不便さを計算する
    # 2. その後、橋を崩壊させる
    # 3. 橋を崩壊させたときに、どの島がつながっているかを記録しておく
    # 4. 橋を崩壊させることで、島がつながっていない場合は、不便さを増やす
    # 5. すべての橋を崩壊させたら、最終的な不便さを出力する
    # 1. まず、すべての島がつながっていると仮定して、不便さを計算する
    inconvenience = N * (N - 1) // 2
    # 2. その後、橋を崩壊させる
    # 3. 橋を崩壊させたときに、どの島がつながっているかを記録しておく
    # 4. 橋を崩壊させることで、島がつながっていない場合は、不便さを増やす
    # 5. すべての橋を崩壊させたら、最終的な不便さを出力する
    # 2. その後、橋を崩壊させる
    # 3. 橋

if __name__ == '__main__':
    main()