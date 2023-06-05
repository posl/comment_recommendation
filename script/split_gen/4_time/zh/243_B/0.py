def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
        elif a[i] in b:
            count2 += 1
    print(count1)
    print(count2)
