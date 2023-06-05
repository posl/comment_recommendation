def main():
    s = input()
    k = int(input())
    n = len(s)
    for i in range(n):
        if s[i] != '1':
            break
    if i == n-1:
        print(1)
        return
    if k <= i+1:
        print(1)
        return
    if k > n:
        print(s[i+1])
        return
    print(s[k-1])
