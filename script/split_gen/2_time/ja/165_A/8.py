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
