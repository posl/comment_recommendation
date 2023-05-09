def majority_vote():
    n = int(input())
    s = [input() for i in range(n)]
    return "Yes" if s.count("For") > s.count("Against") else "No"

if __name__ == '__main__':
    majority_vote()