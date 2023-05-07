def main():
    S = input()
    c = 0
    for i in range(10000):
        n = str(i).zfill(4)
        for j in range(10):
            if S[j] == 'o' and str(j) not in n:
                break
            elif S[j] == 'x' and str(j) in n:
                break
        else:
            c += 1
    print(c)
