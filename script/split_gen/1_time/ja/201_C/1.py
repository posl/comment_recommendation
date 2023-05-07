def main():
    S = input()
    count = 0
    for i in range(10000):
        s = str(i).zfill(4)
        flag = True
        for j in range(10):
            if S[j] == 'o' and str(j) not in s:
                flag = False
            if S[j] == 'x' and str(j) in s:
                flag = False
        if flag:
            count += 1
    print(count)
