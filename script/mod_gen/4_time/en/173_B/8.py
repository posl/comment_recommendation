def main():
    n = int(input())
    verdict = ['AC', 'WA', 'TLE', 'RE']
    verdict_count = [0] * 4
    for i in range(n):
        verdict_count[verdict.index(input())] += 1
    for i in range(4):
        print(verdict[i], 'x', verdict_count[i])

if __name__ == '__main__':
    main()