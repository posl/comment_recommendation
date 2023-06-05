def main():
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])
