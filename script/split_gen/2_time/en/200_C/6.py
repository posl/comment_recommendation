def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [123, 223, 123, 523, 200, 2000]
    #N = len(A)
    
    # 余りのリストを作成
    mod_list = [a % 200 for a in A]
    
    # 余りのリストを辞書に変換
    mod_dict = {}
    for i, mod in enumerate(mod_list):
        if mod in mod_dict:
            mod_dict[mod].append(i)
        else:
            mod_dict[mod] = [i]
    
    # 辞書の値のリストから組み合わせを作成
    # 組み合わせ数をカウント
    count = 0
    for mod, index_list in mod_dict.items():
        if len(index_list) > 1:
            count += len(index_list) * (len(index_list) - 1) // 2
    
    print(count)
