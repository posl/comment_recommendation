def main():
    n = int(input())
    a = [0] * (n-1)
    b = [0] * (n-1)
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(set(a))
    #print(set(b))
    #print(set(a) & set(b))
    #print(set(a) | set(b))
    #print(set(a) ^ set(b))
    if len(set(a) & set(b)) == 1 and len(set(a) | set(b)) == n:
        print("Yes")
    else:
        print("No")
