def main():
    s = input()
    q = int(input())
    query = [input().split() for _ in range(q)]
    query.reverse()
    ans = list(s)
    reverse = False
    for i in range(q):
        if query[i][0] == '1':
            reverse = not reverse
        else:
            if (query[i][1] == '1' and not reverse) or (query[i][1] == '2' and reverse):
                ans.insert(0, query[i][2])
            else:
                ans.append(query[i][2])
    if reverse:
        ans.reverse()
    print(''.join(ans))
