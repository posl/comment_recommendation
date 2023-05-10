def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)
