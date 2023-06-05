def main():
    s = input()
    s = list(s)
    if len(s) == 1:
        if s[0] == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s[0] + s[1]) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 3:
        for i in range(3):
            for j in range(3):
                if j == i:
                    continue
                for k in range(3):
                    if k == i or k == j:
                        continue
                    if int(s[i] + s[j] + s[k]) % 8 == 0:
                        print('Yes')
                        return
        print('No')
        return
    if len(s) == 4:
        for i in range(4):
            for j in range(4):
                if j == i:
                    continue
                for k in range(4):
                    if k == i or k == j:
                        continue
                    for l in range(4):
                        if l == i or l == j or l == k:
                            continue
                        if int(s[i] + s[j] + s[k] + s[l]) % 8 == 0:
                            print('Yes')
                            return
        print('No')
        return
