def main():
    N = int(input())
    votes = []
    for i in range(N):
        votes.append(input())
    votes.sort()
    count = 1
    max_count = 0
    max_list = []
    for i in range(N - 1):
        if votes[i] == votes[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_list = [votes[i]]
            elif count == max_count:
                max_list.append(votes[i])
            count = 1
    if count > max_count:
        max_count = count
        max_list = [votes[-1]]
    elif count == max_count:
        max_list.append(votes[-1])
    max_list.sort()
    for i in max_list:
        print(i)
