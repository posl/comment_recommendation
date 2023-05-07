def main():
    S = input().split('/')
    if int(S[0]) < 2019:
        print('Heisei')
    elif int(S[0]) > 2019:
        print('TBD')
    elif int(S[1]) < 4:
        print('Heisei')
    elif int(S[1]) > 4:
        print('TBD')
    elif int(S[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')
