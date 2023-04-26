Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

=======
Suggestion 2

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

この問題、解いたことなかったので解いてみました。

a = [s] で初項をリストに入れて、while True で無限ループさせています。

while True: の中で、a.append(f(a[-1])) でリストの最後尾に a[-1] を f に入れた値を追加しています。

そして、if a[-1] in a[:-1]: でリストの最後尾の値がリストの最後尾以外の値に含まれているかどうかを判定しています。

含まれていれば、break で無限ループを抜けます。

そして、print(len(a)) でリストの長さを出力しています。

これで、条件を満たす最小の整数 m を求めるこ�

=======
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1]) > 1:
        break
print(len(a))

=======
Suggestion 4

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1]) > 1:
        print(len(a) - 1)
        break

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i - 1]))
    if a[i] in a[:i]:
        print(a.index(a[i]) + 1)
        break
    i += 1

=======
Suggestion 6

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i - 1]))
    if len(a) != len(set(a)):
        break
    i += 1
print(len(a))

=======
Suggestion 7

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]

while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 8

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while a[i-1] not in a[0:i-1]:
    a.append(f(a[i-1]))
    i += 1
print(i)
