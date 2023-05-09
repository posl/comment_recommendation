def main():
    num = int(input())
    vote = {}
    for i in range(num):
        name = input()
        if name in vote:
            vote[name] += 1
        else:
            vote[name] = 1
    print(max(vote, key=vote.get))
