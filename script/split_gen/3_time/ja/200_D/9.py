def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 余りをキーとしたリストを作る
    # あとで、各キーのリストの長さが 2 以上なら
    # その中から 2 つを選ぶ組み合わせを求める
    mod_dict = {}
    for i in range(N):
        mod = A[i] % 200
        if mod in mod_dict:
            mod_dict[mod].append(i)
        else:
            mod_dict[mod] = [i]
    # 組み合わせを求める
    for mod in mod_dict:
        if len(mod_dict[mod]) >= 2:
            print("Yes")
            print(1, mod_dict[mod][0]+1)
            print(1, mod_dict[mod][1]+1)
            return
    # 組み合わせがない場合
    print("No")
