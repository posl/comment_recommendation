def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    for i in range(q):
        if query[i][0] == '1':
            s = s[::-1]
        elif query[i][0] == '2':
            if query[i][1] == '1':
                s = query[i][2] + s
            elif query[i][1] == '2':
                s = s + query[i][2]
    print(s)
