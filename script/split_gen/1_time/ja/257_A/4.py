def main():
    N, X = map(int, input().split())
    alphabet = [chr(i) for i in range(65, 65+26)]
    count = 0
    for i in range(N):
        for j in range(26):
            count += 1
            if count == X:
                print(alphabet[j])
                return
