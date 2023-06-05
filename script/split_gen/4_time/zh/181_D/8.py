def main():
    s = input()
    ans = 'No'
    if len(s) == 1:
        if s == '8':
            ans = 'Yes'
    elif len(s) == 2:
        if int(s) % 8 == 0:
            ans = 'Yes'
        elif int(s[::-1]) % 8 == 0:
            ans = 'Yes'
    else:
        s = list(s)
        for i in range(112, 1000, 8):
            t = list(str(i))
            if len(set(t)) == 3:
                continue
            else:
                for j in range(0, 3):
                    if t[j] in s:
                        s.remove(t[j])
                    else:
                        break
                else:
                    ans = 'Yes'
                    break
    print(ans)
