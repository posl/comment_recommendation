def main():
    K = int(input())
    alphabets = [chr(i) for i in range(65, 65+26)]
    print(''.join(alphabets[:K]))
