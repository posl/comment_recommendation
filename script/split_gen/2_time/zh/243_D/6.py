def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        l = input().split()
        x.append(int(l[0]))
        y.append(int(l[1]))
    s = input()
    flag = False
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                continue
            elif s[i] == 'R':
                if s[j] == 'L':
                    continue
                else:
                    if x[i] > x[j]:
                        continue
                    elif x[i] == x[j]:
                        if y[i] > y[j]:
                            continue
                        else:
                            flag = True
                            break
                    else:
                        flag = True
                        break
            else:
                if s[j] == 'R':
                    continue
                else:
                    if x[i] < x[j]:
                        continue
                    elif x[i] == x[j]:
                        if y[i] > y[j]:
                            continue
                        else:
                            flag = True
                            break
                    else:
                        flag = True
                        break
        if flag:
            break
    if flag:
        print('Yes')
    else:
        print('No')
