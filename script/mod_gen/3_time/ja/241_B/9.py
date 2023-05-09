def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #Aの中にBの要素があるかを調べる
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()