def main():
    N = int(input())
    S = [input() for _ in range(N)]
    a = S.count('AC')
    b = S.count('WA')
    c = S.count('TLE')
    d = S.count('RE')
    print('AC x ' + str(a))
    print('WA x ' + str(b))
    print('TLE x ' + str(c))
    print('RE x ' + str(d))
