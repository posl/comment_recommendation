def main():
    n = int(input())
    d = input().split()
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum += int(d[i])*int(d[j])
    print(sum)
