def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    n = 2
    a = [1, 1]
    b = [2, 3]
    c = []
    for i in range(n):
        c.append([a[i], b[i]])
    print(c)
    print("n = ", n)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("answer = ", answer(n, c))
    return
