def main():
    S = int(input())
    count = 0
    for i in range(1, S+1):
        for j in range(1, S+1):
            for k in range(1, S+1):
                if i+j+k == S and i >= 3 and j >= 3 and k >= 3:
                    count += 1
    print(count % (10**9+7))
