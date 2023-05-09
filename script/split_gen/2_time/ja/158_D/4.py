def main():
    s = input()
    q = int(input())
    rev = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = 1 - rev
        else:
            if (query[1] == '1' and rev == 0) or (query[1] == '2' and rev == 1):
                s = query[2] + s
            else:
                s = s + query[2]
    if rev == 1:
        s = s[::-1]
    print(s)
