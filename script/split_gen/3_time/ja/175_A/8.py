def main():
    S = input()
    #print(S)
    #print(len(S))
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "R":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)
