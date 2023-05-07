def main():
    S = input()
    S = S.split('/')
    if int(S[0]) == 2019 and int(S[1]) <= 4 and int(S[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')
