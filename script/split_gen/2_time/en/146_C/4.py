def  main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 < X:
        print(0)
        return
    if A + B > X:
        print(0)
        return
    min = 1
    max = 10**9
    while max - min > 1:
        mid = (max + min) // 2
        if A * mid + B * (len(str(mid))) <= X:
            min = mid
        else:
            max = mid
    print(min)
