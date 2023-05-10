def main():
    S = input()
    count = 0
    for i in range(10000):
        s = str(i).zfill(4)
        f = True
        for j in range(10):
            if S[j] == 'o':
                if str(j) not in s:
                    f = False
                    break
            elif S[j] == 'x':
                if str(j) in s:
                    f = False
                    break
        if f:
            count += 1
    print(count)
