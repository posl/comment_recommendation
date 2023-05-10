def main():
    S = input()
    count = 0
    for i in range(10000):
        password = str(i).zfill(4)
        ok = True
        for j in range(10):
            if S[j] == 'o' and str(j) not in password:
                ok = False
            if S[j] == 'x' and str(j) in password:
                ok = False
        if ok:
            count += 1
    print(count)
