def main():
    #n = int(input())
    n = 200000
    #n = 25
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%10 == j//100 and i//100 == j%10:
                count += 1
    print(count)
