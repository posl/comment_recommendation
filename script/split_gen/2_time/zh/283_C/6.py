def main():
    S = input()
    S_len = len(S)
    #print(S_len)
    S = int(S)
    count = 0
    if S == 0:
        print(1)
        return
    for i in range(1, S_len):
        if i == 1:
            count += 10
        else:
            count += 9 * (10 ** (i - 2)) * (i - 1)
    #print(count)
    if S_len == 1:
        print(S)
        return
    for i in range(1, S_len):
        if i == 1:
            count += S - (10 ** (i - 1)) + 1
        else:
            count += (S - (10 ** (i - 1))) * (i - 1)
    print(count)
    return
