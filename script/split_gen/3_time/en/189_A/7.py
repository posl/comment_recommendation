def main():
    # input
    C1, C2, C3 = input().split()
    # output
    if C1 == C2 and C2 == C3:
        print('Won')
    else:
        print('Lost')
