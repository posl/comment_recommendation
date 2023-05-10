def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    a.append(max1)
    for i in range(n):
        if a[i] == max1:
            print(max2)
        else:
            print(max1)
