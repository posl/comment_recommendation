def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            a[int(query[1])-1] = int(query[2])
        else:
            print(a[int(query[1])-1])
