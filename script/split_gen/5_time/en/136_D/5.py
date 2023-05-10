def main():
    s = input()
    n = len(s)
    a = [0]*n
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == 'R':
            j += 1
        k = j
        while k < n and s[k] == 'L':
            k += 1
        if (j-i) % 2 == 0:
            a[j-1] += (j-i)//2
            a[j] += (j-i)//2
        else:
            if (j-i) % 2 == 1:
                a[j-1] += (j-i)//2 + 1
                a[j] += (j-i)//2
            else:
                a[j-1] += (j-i)//2
                a[j] += (j-i)//2 + 1
        i = k
    print(*a)
