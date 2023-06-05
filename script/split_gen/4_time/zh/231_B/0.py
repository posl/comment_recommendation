def main():
    n = int(input())
    votes = {}
    for i in range(n):
        name = input()
        if name in votes:
            votes[name] = votes[name] + 1
        else:
            votes[name] = 1
    max = 0
    max_name = ""
    for k in votes:
        if votes[k] > max:
            max = votes[k]
            max_name = k
    print(max_name)
