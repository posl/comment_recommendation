def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(2,int(n**0.5)+1):
            if n%j == 0:
                print(j,int(n/j))
                break
