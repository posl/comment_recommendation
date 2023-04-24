Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        if A[i] % 200 == 0:
            B.append(i+1)
        else:
            C.append(i+1)
    if len(B) >= 2:
        print("Yes")
        print(len(B), *B)
        print(1, B[0])
        return
    if len(C) >= 2:
        print("Yes")
        print(1, C[0])
        print(len(C), *C)
        return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(n):
        mod[a[i] % 200] += 1
    for i in range(200):
        if mod[i] >= 2:
            print("Yes")
            count = 0
            for j in range(n):
                if a[j] % 200 == i:
                    count += 1
                    print(j + 1, end=" ")
                    if count == 2:
                        break
            print()
            count = 0
            for j in range(n):
                if a[j] % 200 == i:
                    count += 1
                    print(j + 1, end=" ")
                    if count == 2:
                        break
            print()
            return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print("Yes")
        print("1 1")
        print("1 2")
        return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if i != k and j != l:
                        if (A[i] + A[j]) % 200 == (A[k] + A[l]) % 200:
                            print("Yes")
                            print("2", i+1, j+1)
                            print("2", k+1, l+1)
                            return
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i)
        else:
            d[A[i]] = [i]
    for k in d:
        if len(d[k]) > 1:
            print("Yes")
            print(1, d[k][0] + 1)
            print(1, d[k][1] + 1)
            return
    for i in range(200):
        for j in range(i + 1, 200):
            if i in d and j in d:
                print("Yes")
                print(2, d[i][0] + 1, d[j][0] + 1)
                print(2, d[i][1] + 1, d[j][1] + 1)
                return
    print("No")

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [a % 200 for a in A]
    D = {}
    for i in range(N):
        if A[i] in D:
            print('Yes')
            print(1,i+1)
            print(len(D[A[i]]),*D[A[i]])
            return
        else:
            D[A[i]] = [i+1]
    print('No')
    return

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]

    for i in range(1 << N):
        x = [a for a, b in zip(A, format(i, 'b').zfill(N)) if b == '1']
        y = [a for a, b in zip(A, format(i, 'b').zfill(N)) if b == '0']
        if len(x) > 0 and len(y) > 0 and sum(x) % 200 == sum(y) % 200:
            print('Yes')
            print(len(x), *x)
            print(len(y), *y)
            break
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    modA2 = [[i, a] for i, a in enumerate(modA)]
    modA2.sort(key=lambda x: x[1])
    modA3 = []
    for i in range(len(modA2) - 1):
        if modA2[i][1] == modA2[i + 1][1]:
            modA3.append([modA2[i], modA2[i + 1]])
    if len(modA3) == 0:
        print("No")
        return
    else:
        print("Yes")
        print(2, modA3[0][0][0] + 1, modA3[0][1][0] + 1)
        print(1, modA3[0][0][0] + 1)
        return

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a%mod for a in A]
    modA = [a+mod if a==0 else a for a in modA]

    #print(modA)
    #print(A)
    #print(N)
    #print(mod)

    #modAの中で、同じ値の要素があるかどうか
    #あったら、その要素を出力する
    #なかったら、modAの中で、同じ値の要素があるかどうかを繰り返す
    #あったら、その要素を出力する
    #なかったら、Noと出力する

    #modAの中で、同じ値の要素があるかどうか
    #あったら、その要素を出力する
    #なかったら、modAの中で、同じ値の要素があるかどうかを繰り返す
    #あったら、その要素を出力する
    #なかったら、Noと出力する

    #modAの中で、同じ値の要素があるかどうか
    #あったら、その要素を出力する
    #なかったら、modAの中で、同じ値の要素があるかどうかを繰り返す
    #あったら、その要素を出力する
    #なかったら、Noと出力する

    #modAの中で、同じ値の要素があるかどうか
    #あったら、その要素を出力する
    #なかったら、modAの中で、同じ値の要素があるかどうかを繰り返す
    #あったら、その要素を出力する
    #なかったら、Noと出力する

    #modAの

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    # 余りをキーに、その余りを持つ要素のインデックスをリストで保持する
    r2idxs = [[] for _ in range(mod)]
    for i, a in enumerate(A):
        r2idxs[a % mod].append(i + 1)
    for r in range(mod):
        if len(r2idxs[r]) >= 2:
            print("Yes")
            print(len(r2idxs[r]), *r2idxs[r])
            print(len(r2idxs[r]), *r2idxs[r])
            return
    print("No")
