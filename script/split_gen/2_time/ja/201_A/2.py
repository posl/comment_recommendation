def main():
    #入力
    A = [int(i) for i in input().split()]
    #並び替え
    A.sort()
    #出力
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")
