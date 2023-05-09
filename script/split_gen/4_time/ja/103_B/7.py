def main():
    # input
    S = input()
    T = input()
    # compute
    result = "No"
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            result = "Yes"
            break
    # output
    print(result)
