def main():
    N = input()
    k = len(N)
    # 全ての桁の和を計算
    total = sum([int(n) for n in N])
    # 3の倍数でない場合は、最低でも1つの桁を消して3の倍数にする必要がある
    if total % 3 != 0:
        return -1
    # 3の倍数の場合は、0以上k-1以下の桁を消せば3の倍数にできる
    # 3の倍数である場合は、最低でも1つの桁を消して3の倍数にする必要がある
    if total % 3 == 0:
        # 3の倍数である場合は、最低でも1つの桁を消して3の倍数にする必要がある
        for i in range(k):
            # 桁の和を3で割った余りが0になるような桁を消せばよい
            if int(N[i]) % 3 == 0:
                return 1
        # 3の倍数である場合は、最低でも1つの桁を消して3の倍数にする必要がある
        for i in range(k):
            for j in range(i + 1, k):
                # 桁の和を3で割った余りが0になるような2つの桁を消せばよい
                if (int(N[i]) + int(N[j])) % 3 == 0:
                    return 2
        # 3の倍数である場合は、最低でも1つの桁を消して3の倍数にする必要がある
        return -1
    return -1

if __name__ == '__main__':
    main()