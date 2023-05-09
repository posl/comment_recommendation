def main():
    s = input()
    n = len(s)
    #print(s)
    #print(n)
    a = [0] * n
    #print(a)
    for i in range(n):
        if s[i] == "R":
            a[i+1] += 1
        else:
            a[i] += 1
    #print(a)
    for i in range(10**100):
        b = [0] * n
        for j in range(n):
            if a[j] % 2 == 1:
                b[j-1] += 1
            else:
                b[j+1] += 1
        a = b
    print(*a)
