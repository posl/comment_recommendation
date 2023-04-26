Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(N):
        mod[A[i] % 200] += 1
    for i in range(200):
        if mod[i] > 1:
            print("Yes")
            print(mod[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod[i] -= 1
                    if mod[i] == 0:
                        print()
                        break
            print(mod[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod[i] -= 1
                    if mod[i] == 0:
                        print()
                        break
            break
    else:
        print("No")

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    dic = {}
    for i, a in enumerate(A):
        if a in dic:
            dic[a].append(i + 1)
            x = len(dic[a])
            B = dic[a]
            y = i + 1 - x
            C = [i + 1 for i in range(N) if i + 1 not in B]
            print('Yes')
            print(x, *B)
            print(y, *C)
            return
        else:
            dic[a] = [i + 1]
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [180, 186, 189, 191, 218]
    # N = 5
    # A = [123, 523]
    # N = 2
    # A = [2013, 1012, 2765, 2021, 508, 6971]
    # N = 6

    # 200で割った余り毎にグループ化
    groups = [[] for _ in range(200)]
    for i, a in enumerate(A):
        groups[a % 200].append(i)

    # 200で割った余りが同じグループが2つ以上あるなら、それらを出力
    for g in groups:
        if len(g) > 1:
            print('Yes')
            print(1, g[0] + 1)
            print(1, g[1] + 1)
            return

    # 200で割った余りが同じグループが2つもなければ、
    # 200で割った余りが同じグループがあるなら、それを使って2つのグループを作る
    for i, g in enumerate(groups):
        if len(g) > 0:
            for j, h in enumerate(groups):
                if len(h) > 0 and i != j:
                    print('Yes')
                    print(len(g), ' '.join(map(str, [x + 1 for x in g])))
                    print(len(h), ' '.join(map(str, [x + 1 for x in h])))
                    return

    # 200で割った余りが同じグループが1つもなければ、No
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [x % 200 for x in a]
    d = dict()
    for i, x in enumerate(a):
        if x in d:
            d[x].append(i + 1)
        else:
            d[x] = [i + 1]
    for x in d:
        if len(d[x]) >= 2:
            print('Yes')
            print(len(d[x]), *d[x][:2])
            print(len(d[x]), *d[x][2:])
            return
    print('No')

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    ans = []
    for i in range(2**N):
        B = []
        C = []
        for j in range(N):
            if (i >> j) & 1:
                B.append(j+1)
            else:
                C.append(j+1)
        if len(B) != 0 and len(C) != 0 and len(B) != len(C):
            if sum([A[b-1] for b in B]) % mod == sum([A[c-1] for c in C]) % mod:
                ans.append([B, C])
    if len(ans) == 0:
        print("No")
    else:
        print("Yes")
        print(*ans[0])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割った余りの数列を作成
    A = [a % 200 for a in A]
    # 余りの数列を200個のリストに分類
    # 余りの数列を200個のリストに分類
    A = [list() for i in range(200)]
    for i, a in enumerate(A):
        A[a].append(i)
    # 余りの数列を200個のリストに分類
    for i in range(200):
        if len(A[i]) >= 2:
            print("Yes")
            print(len(A[i]), *A[i])
            print(len(A[i]), *A[i])
            return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 2つの数列の組み合わせを全探索して条件を満たすか判定する
    # 2つの数列の組み合わせは N^2 通りである
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            # 2つの数列の組み合わせについて、条件を満たすか判定する
            # 条件を満たすか判定するためには、
            # 1. 2つの数列の組み合わせの要素数が異なる
            # 2. 2つの数列の組み合わせの要素の和を 200 で割った余りが等しい
            # 3. 2つの数列の組み合わせの要素の和を 200 で割った余りが等しい
            # が成り立つ必要がある
            # 1. と 2. は、条件を満たすか判定するためには必要な条件である
            # 3. は、条件を満たすか判定するためには必要な条件ではないが、
            # 3. が成り立たない場合は、条件を満たす数列の組は存在しない
            # 3. が成り立たない場合は、条件を満たす数列の組は存在しない
            # 1. と 2. は、条件を満たすか判定するためには必要な条件である
            # 3. は、条件を満たすか判定するためには必要な条件ではないが、
            # 3. が成り立たない場合は、条件を

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    # 余りごとにグループを作る
    # 余りが同じなら、そのグループの数列の和を 200 で割った余りは同じ
    # 余りが同じなら、そのグループの数列の和を 200 で割った余りは同じ
    # ということは、ある数列の和を 200 で割った余りが同じなら、
    # その数列は和を 200 で割った余りが同じ数列の和となる
    # ということなので、2つの数列の和を 200 で割った余りが同じなら、
    # その2つの数列は同じグループに属する
    # つまり、あるグループに属する数列の和を 200 で割った余りが同じなら、
    # そのグループに属する数列はすべて同じ数列の和となる
    # つまり、あるグループに属する数列の和を 200 で割った余りが同じなら、
    # そのグループに属する数列はすべて同じ数列の和となる
    # ということなので、2つのグループの和を 200 で割った余りが同じなら、
    # その2つのグループは同じグループに属する
    # つまり、あるグループに属する数列の和を 200 で割った余りが同じなら、
    # そのグループに属する数列はすべて同じ数列の和となる
    #

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200 で割った余りをキーにして、その値が 2 以上のときに答えとなる
    d = {}
    for i, x in enumerate(a):
        x %= 200
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    # 答えがない場合
    if not any([d[x] >= 2 for x in d]):
        print('No')
        return
    # 答えがある場合
    print('Yes')
    # 2 つ以上ある余りのうち、最初に見つかったものを出力
    for i, x in enumerate(a):
        x %= 200
        if d[x] >= 2:
            print(i + 1, end=' ')
            d[x] -= 1
            if d[x] == 0:
                del d[x]
        if not d:
            break
    print()
    # 2 つ以上ある余りのうち、次に見つかったものを出力
    for i, x in enumerate(a):
        x %= 200
        if x in d:
            print(i + 1, end=' ')
            d[x] -= 1
            if d[x] == 0:
                del d[x]
        if not d:
            break
    print()

=======
Suggestion 10

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
