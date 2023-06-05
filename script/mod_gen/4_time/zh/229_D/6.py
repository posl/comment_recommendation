def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    i = 0
    while i < n:
        if s[i] == "X":
            count = 0
            while i < n and s[i] == "X":
                count += 1
                i += 1
            l.append(count)
        else:
            i += 1
    ans = 0
    for i in range(len(l)):
        ans = max(ans, l[i])
    for i in range(len(l)):
        if k == 0:
            break
        if l[i] == 1:
            if i == 0:
                if i+1 < len(l):
                    if l[i+1] > 1:
                        if k >= 2:
                            ans = max(ans, l[i]+l[i+1]+1)
                            k -= 2
                    else:
                        if k >= 1:
                            ans = max(ans, l[i]+l[i+1]+1)
                            k -= 1
                else:
                    if k >= 1:
                        ans = max(ans, l[i]+l[i+1]+1)
                        k -= 1
            elif i == len(l)-1:
                if i-1 >= 0:
                    if l[i-1] > 1:
                        if k >= 2:
                            ans = max(ans, l[i]+l[i-1]+1)
                            k -= 2
                    else:
                        if k >= 1:
                            ans = max(ans, l[i]+l[i-1]+1)
                            k -= 1
                else:
                    if k >= 1:
                        ans = max(ans, l[i]+l[i-1]+1)
                        k -= 1
            else:
                if l[i-1] > 1 and l[i+1] > 1:
                    if k >= 3:
                        ans = max(ans, l[i-1]+l[i]+l[i+1]+2)
                        k -= 3
                elif l[i-1] > 1 and l[i+1] <= 1:
                    if k >= 2:
                        ans = max(ans, l[i-1]+l[i]+l[i+1]+1)
                        k -= 2
                elif l[i-1] <=

if __name__ == '__main__':
    main()