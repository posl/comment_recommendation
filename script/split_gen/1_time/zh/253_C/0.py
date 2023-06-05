def main():
    q = int(input())
    s = []
    for i in range(q):
        query = input().split()
        if int(query[0]) == 1:
            s.append(int(query[1]))
        elif int(query[0]) == 2:
            for i in range(int(query[2])):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
        elif int(query[0]) == 3:
            print(max(s)-min(s))
