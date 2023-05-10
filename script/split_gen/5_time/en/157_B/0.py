def main():
    a1,a2,a3 = map(int, input().split())
    b1,b2,b3 = map(int, input().split())
    c1,c2,c3 = map(int, input().split())
    n = int(input())
    b = [int(input()) for _ in range(n)]
    res = 'No'
    if a1 in b and a2 in b and a3 in b:
        res = 'Yes'
    if b1 in b and b2 in b and b3 in b:
        res = 'Yes'
    if c1 in b and c2 in b and c3 in b:
        res = 'Yes'
    if a1 in b and b1 in b and c1 in b:
        res = 'Yes'
    if a2 in b and b2 in b and c2 in b:
        res = 'Yes'
    if a3 in b and b3 in b and c3 in b:
        res = 'Yes'
    if a1 in b and b2 in b and c3 in b:
        res = 'Yes'
    if c1 in b and b2 in b and a3 in b:
        res = 'Yes'
    print(res)
