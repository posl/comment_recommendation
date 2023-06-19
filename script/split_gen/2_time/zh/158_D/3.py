def main():
    s = raw_input()
    q = int(raw_input())
    query = []
    for i in range(q):
        query.append(raw_input().split())
    for i in range(q):
        if query[i][0] == '1':
            s = s[::-1]
        else:
            if query[i][1] == '1':
                s = query[i][2] + s
            else:
                s = s + query[i][2]
    print s
