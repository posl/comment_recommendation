def main():
    a,b,k = map(int,input().split())
    div = []
    for i in range(1,max(a,b)+1):
        if a%i == 0 and b%i == 0:
            div.append(i)
    print(div[-k])
