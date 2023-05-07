def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Aの中にBの要素があればYesを出力
    if set(B) <= set(A):
        print("Yes")
    else:
        print("No")
