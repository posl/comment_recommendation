def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s = s[::-1]
        else:
            if query[1] == '1':
                s = query[2] + s
            else:
                s = s + query[2]
    print(s)
