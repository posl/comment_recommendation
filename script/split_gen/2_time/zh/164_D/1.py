def main():
    S = input()
    # print(S)
    count = 0
    for i in range(len(S)):
        for j in range(i,len(S)):
            # print(S[i:j+1])
            if int(S[i:j+1])%2019 == 0:
                count += 1
    print(count)
