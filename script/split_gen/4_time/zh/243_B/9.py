def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                count2 += 1
    print(count1)
    print(count2)
