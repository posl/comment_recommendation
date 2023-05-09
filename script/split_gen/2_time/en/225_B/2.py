def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    star = True
    for i in range(1, n):
        if a.count(i) != 1 or b.count(i) != 1:
            star = False
            break
    if star:
        print("Yes")
    else:
        print("No")
