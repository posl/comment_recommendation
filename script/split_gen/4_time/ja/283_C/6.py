def main():
    #input
    S = input()
    #compute
    count = 0
    while True:
        if len(S) == 1:
            count += int(S)
            break
        else:
            if S[-1] == "0":
                S = S[:-1]
            else:
                count += 10 - int(S[-1])
                S = str(int(S) + 1)
    #output
    print(count)
    return
