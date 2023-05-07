def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(i+3,len(S)+1):
            if int(S[i:j]) % 2019 == 0:
                count += 1
    print(count)
