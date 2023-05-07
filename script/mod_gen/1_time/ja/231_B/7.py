def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_set = set(s)
    max_vote = 0
    winner = ""
    for name in s_set:
        if max_vote < s.count(name):
            max_vote = s.count(name)
            winner = name
    print(winner)

if __name__ == '__main__':
    main()