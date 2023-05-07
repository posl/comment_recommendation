def main():
    S = input()
    ACGT = 'ACGT'
    #print(S)
    #print(ACGT)
    max = 0
    count = 0
    for i in range(len(S)):
        #print(i)
        if S[i] in ACGT:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
