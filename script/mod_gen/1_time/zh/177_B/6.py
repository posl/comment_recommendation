def solve():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if min > count:
            min = count
    print(min)

if __name__ == '__main__':
    solve()