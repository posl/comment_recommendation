def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S[0] == 'R' or S[1] == 'R' or S[2] == 'R':
        print(1)
    else:
        print(0)
