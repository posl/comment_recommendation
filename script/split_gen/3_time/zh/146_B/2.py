def main():
    N = int(input())
    S = input()
    result = []
    for i in S:
        if ord(i) + N > ord('Z'):
            result.append(chr(ord(i) + N - ord('Z') + ord('A') - 1))
        else:
            result.append(chr(ord(i) + N))
    print(''.join(result))
