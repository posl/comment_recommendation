def main():
    q = int(input())
    s = []
    for i in range(0,q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            for j in range(0,int(query[2])):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
        elif query[0] == '3':
            print(max(s)-min(s))
        else:
            print('error')
