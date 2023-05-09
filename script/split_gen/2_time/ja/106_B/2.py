def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%2 == 1:
            if len([j for j in range(1,i+1) if i%j == 0]) == 8:
                count += 1
    print(count)
