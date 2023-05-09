def main():
    S = input()
    N = len(S)
    people = [1] * N
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            people[i] += people[i + 1]
            people[i + 1] = 0
    for i in range(N - 1, 0, -1):
        if S[i - 1] == S[i]:
            people[i] += people[i - 1]
            people[i - 1] = 0
    print(*people)
