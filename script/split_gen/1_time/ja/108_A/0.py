def main():
    K = int(input())
    count = 0
    for i in range(1,K+1):
        if i%2 == 0:
            for j in range(1,K+1):
                if j%2 == 1:
                    count += 1
    print(count)
