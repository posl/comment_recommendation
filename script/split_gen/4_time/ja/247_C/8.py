def main():
    n = int(input())
    for i in range(1,n+1):
        print(i, end=" ")
        if i == 1:
            continue
        for j in range(i-1,0,-1):
            print(j, end=" ")
        print(i, end=" ")
