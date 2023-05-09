def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 選んだ数列の和を200で割った余りを記録する配列
    mod = [0] * 200
    # 選んだ数列の和を200で割った余りを記録する配列のインデックスを記録する配列
    index = [[] for _ in range(200)]
    # 選んだ数列の和を200で割った余りを記録する配列を作成する
    for i in range(N):
        mod[A[i] % 200] += 1
        index[A[i] % 200].append(i)
    # 選んだ数列の和を200で割った余りが同じ数列が存在するかを判定する
    for i in range(200):
        if mod[i] >= 2:
            print("Yes")
            print(mod[i], *index[i][:mod[i]])
            print(mod[i], *index[i][mod[i]:])
            return
    print("No")
