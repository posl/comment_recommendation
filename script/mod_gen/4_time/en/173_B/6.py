def main():
    n = int(input())
    verdicts = [input() for _ in range(n)]
    verdicts_dict = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for verdict in verdicts:
        verdicts_dict[verdict] += 1
    print('AC x', verdicts_dict['AC'])
    print('WA x', verdicts_dict['WA'])
    print('TLE x', verdicts_dict['TLE'])
    print('RE x', verdicts_dict['RE'])

if __name__ == '__main__':
    main()