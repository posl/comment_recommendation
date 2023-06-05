def main():
    n = int(input())
    case = [input() for _ in range(n)]
    print('AC x', case.count('AC'))
    print('WA x', case.count('WA'))
    print('TLE x', case.count('TLE'))
    print('RE x', case.count('RE'))
