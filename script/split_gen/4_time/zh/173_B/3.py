def main():
    n = int(input())
    s = [input() for i in range(n)]
    c = [s.count('AC'), s.count('WA'), s.count('TLE'), s.count('RE')]
    print('AC x', c[0])
    print('WA x', c[1])
    print('TLE x', c[2])
    print('RE x', c[3])
