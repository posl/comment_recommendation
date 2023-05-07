def main():
    n = int(input())
    candidates = {}
    for i in range(n):
        name = input()
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1
    #print(candidates)
    max_vote = max(candidates.values())
    #print(max_vote)
    for key, value in candidates.items():
        if value == max_vote:
            print(key)
