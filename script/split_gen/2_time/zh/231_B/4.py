def main():
    n = int(input())
    candidates = {}
    max_vote = 0
    max_candidate = ""
    for i in range(n):
        candidate = input()
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
        if candidates[candidate] > max_vote:
            max_vote = candidates[candidate]
            max_candidate = candidate
    print(max_candidate)
