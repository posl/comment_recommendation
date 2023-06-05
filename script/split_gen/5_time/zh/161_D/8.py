def main():
    k = int(input())
    l = [i for i in range(1, 10)]
    while len(l) < k:
        l2 = []
        for i in l:
            s = str(i)
            if s[-1] == '0':
                l2.append(int(s + '0'))
                l2.append(int(s + '1'))
            elif s[-1] == '9':
                l2.append(int(s + '8'))
                l2.append(int(s + '9'))
            else:
                l2.append(int(s + str(int(s[-1]) - 1)))
                l2.append(int(s + s[-1]))
                l2.append(int(s + str(int(s[-1]) + 1)))
        l = l2
    print(l[k - 1])
