def main():
    A,B,X = map(int,input().split())
    ans = 0
    for i in range(1,11):
        if A*i + B*len(str(i)) <= X:
            ans = i
    print(ans)