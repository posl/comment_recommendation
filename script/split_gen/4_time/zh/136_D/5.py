def main():
    s = input()
    n = len(s)
    #print(s)
    #print(n)
    #print(s[0])
    #print(s[n-1])
    #print(s[0] == 'R')
    #print(s[n-1] == 'L')
    if s[0] == 'R' and s[n-1] == 'L':
        s = s + 'R'
        #print(s)
        n = n + 1
        #print(n)
        a = [0] * n
        #print(a)
        i = 0
        while i < n:
            if s[i] == 'R':
                j = i + 1
                while s[j] == 'R':
                    j += 1
                #print(j)
                j -= 1
                #print(j)
                if (j - i) % 2 == 0:
                    a[j] += 1
                else:
                    a[j - 1] += 1
                i = j + 1
            else:
                j = i - 1
                while s[j] == 'L':
                    j -= 1
                #print(j)
                j += 1
                #print(j)
                if (i - j) % 2 == 0:
                    a[j] += 1
                else:
                    a[j + 1] += 1
                i = j + 1
        #print(a)
        for i in range(n):
            print(a[i], end = ' ')
        print()
    else:
        print('Error!')
