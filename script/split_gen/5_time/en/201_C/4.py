def main():
    S = input()
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        for j in range(10):
            if S[j] == 'o' and str(j) not in i:
                break
            if S[j] == 'x' and str(j) in i:
                break
        else:
            count += 1
    print(count)
