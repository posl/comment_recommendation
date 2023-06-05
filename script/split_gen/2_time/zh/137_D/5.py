def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    #print(s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    print(count)
main()
