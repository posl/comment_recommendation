def main():
    # input
    S = input()
    T = input()
    # compute
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    # output
    print(count)
