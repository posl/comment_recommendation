def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                print("Yes")
                exit()
    print("No")
