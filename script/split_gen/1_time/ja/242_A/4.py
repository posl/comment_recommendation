def main():
    A,B,C,X = map(int,input().split())
    ans = 0
    for i in range(A):
        ans += 1
    for i in range(A,B):
        ans += 1/470
    for i in range(C):
        ans += 1/470
    print(ans)
