def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            c = int(query[2])
            x = int(query[1])
            while c > 0:
                if x in s:
                    s.remove(x)
                c -= 1
        elif query[0] == '3':
            print(max(s) - min(s))
