def main():
    s = input()
    q = int(input())
    rev = 0
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            rev ^= 1
        else:
            if (int(query[1]) ^ rev) == 0:
                s = query[2] + s
            else:
                s = s + query[2]
    if rev == 1:
        s = s[::-1]
    print(s)
