def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            c = int(query[2])
            for j in range(c):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
                else:
                    break
        else:
            print(max(s) - min(s))
