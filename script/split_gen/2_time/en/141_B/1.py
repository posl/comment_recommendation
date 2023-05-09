def main():
    S = input()
    if S[0] == 'R' or S[0] == 'U' or S[0] == 'D':
        for i in range(1, len(S)):
            if i % 2 == 0:
                if S[i] == 'L' or S[i] == 'U' or S[i] == 'D':
                    continue
                else:
                    print("No")
                    exit()
            else:
                if S[i] == 'R' or S[i] == 'U' or S[i] == 'D':
                    continue
                else:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")
