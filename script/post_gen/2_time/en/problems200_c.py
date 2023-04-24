Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] - a[j]) % 200 == 0:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(x) % 200 for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for a in A:
        B[a%200] += 1
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = dict()
    for a in A:
        r = a % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x % 200 for x in A]
    D = {}
    for a in A:
        D[a] = D.get(a, 0) + 1
    ans = 0
    for k, v in D.items():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200で割った余りをキーとして、その余りの数を値とする辞書を作成
    d = {}
    for i in range(n):
        r = a[i] % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    # 余りの数が2以上のものを抜き出し、それらの組み合わせの数を計算
    ans = 0
    for k, v in d.items():
        if v >= 2:
            ans += v * (v - 1) // 2
    print(ans)
