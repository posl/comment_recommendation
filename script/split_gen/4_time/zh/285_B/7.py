def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i+l<n and s[l]!=s[i+l]:
            l+=1
        print(l)
