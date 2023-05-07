def main():
    S = input()
    if S == 'SSS':
        print(0)
    elif S == 'RRS' or S == 'SRR' or S == 'RSR':
        print(1)
    else:
        print(2)
