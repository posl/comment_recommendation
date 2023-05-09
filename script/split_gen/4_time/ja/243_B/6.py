def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_set = set(a)
    b_set = set(b)
    
    count_1 = 0
    for i in range(n):
        if a[i] == b[i]:
            count_1 += 1
    
    count_2 = 0
    for i in range(n):
        if a[i] in b_set and a[i] != b[i]:
            count_2 += 1
    
    print(count_1)
    print(count_2)
