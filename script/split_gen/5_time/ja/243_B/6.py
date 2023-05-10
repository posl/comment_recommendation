def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dict = {}
    for i in range(n):
        dict[a[i]] = i
    dict2 = {}
    for i in range(n):
        dict2[b[i]] = i
    
    count1 = 0
    for i in range(n):
        if a[i] in b:
            count1 += 1
    
    count2 = 0
    for i in range(n):
        if a[i] in b and dict[a[i]] != dict2[a[i]]:
            count2 += 1
    
    print(count1)
    print(count2)
