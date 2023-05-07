def main():
    # input
    S = input()
    # compute
    # output
    if S[0] == S[1] == S[2] == S[3]:
        print('Bad')
    elif S[0] != S[1] != S[2] != S[3]:
        print('Good')
    else:
        print('Bad')
