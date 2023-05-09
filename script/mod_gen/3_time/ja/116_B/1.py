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

if __name__ == '__main__':
    f()