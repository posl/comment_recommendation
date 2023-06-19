def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.sort()
    max = 1
    for i in range(n-1):
        if l[i] == l[i+1]:
            max += 1
        else:
            max = 1
        if max > (n//2):
            print(l[i])
            break
main()
