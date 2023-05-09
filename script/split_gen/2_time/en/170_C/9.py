def  main():
    x, n = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    for i in range(101):
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return
