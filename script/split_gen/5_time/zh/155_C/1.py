def main():
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    votes.sort()
    max_cnt = 0
    cnt = 0
    max_vote = ""
    for i in range(n):
        if i == 0:
            cnt = 1
        else:
            if votes[i] == votes[i-1]:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_vote = votes[i-1]
                cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_vote = votes[n-1]
    print(max_vote)
main()
