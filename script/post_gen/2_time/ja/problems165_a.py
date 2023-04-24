Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(A, B + 1):
        if i % K == 0:
            print("OK")
            break
    else:
        print("NG")

=======
Suggestion 2

def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif (A // K) + 1 <= B // K:
        print("OK")
    else:
        print("NG")

=======
Suggestion 3

def main():
    K = int(input())
    A, B = map(int, input().split())

    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif A % K != 0 and B % K != 0:
        if A // K + 1 <= B // K:
            print("OK")
        else:
            print("NG")

=======
Suggestion 4

def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0:
        print("OK")
        return
    if b % k == 0:
        print("OK")
        return
    if a // k == b // k:
        print("NG")
        return
    print("OK")

=======
Suggestion 5

def main():
    K = int(input())
    A, B = map(int, input().split())
    if B // K - A // K == 0:
        if A % K == 0:
            print("OK")
        else:
            print("NG")
    else:
        print("OK")

=======
Suggestion 6

def main():
    K = int(input())
    A, B = map(int, input().split())

    if A % K == 0 or B % K == 0:
        print("OK")
    elif A // K + 1 <= B // K:
        print("OK")
    else:
        print("NG")

=======
Suggestion 7

def main():
    k = int(input())
    a,b = map(int,input().split())
    if a%k == 0 or b%k == 0:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def main():
    K = int(input())
    A, B = map(int, input().split())

    if B // K - A // K > 0:
        print("OK")
    elif A % K == 0:
        print("OK")
    else:
        print("NG")

=======
Suggestion 9

def main():
    #入力
    K = int(input())
    A, B = map(int, input().split())
    #出力
    if A % K == 0:
        print('OK')
        return
    if B // K - A // K >= 1:
        print('OK')
        return
    print('NG')
    return

=======
Suggestion 10

def main():
    # 標準入力から、K, A, B を取得
    K = int(input())
    A, B = map(int, input().split())

    # A 以上 B 以下の数値のリストを作成
    numbers = [i for i in range(A, B + 1)]

    # K の倍数のリストを作成
    multiples = [i for i in numbers if i % K == 0]

    # K の倍数のリストが空であれば NG を出力
    if not multiples:
        print('NG')
    # K の倍数のリストが空でなければ OK を出力
    else:
        print('OK')
