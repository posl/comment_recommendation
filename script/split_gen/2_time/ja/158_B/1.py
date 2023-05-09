def main():
    N, A, B = map(int, input().split())
    result = N // (A + B) * A
    rest = N % (A + B)
    if rest <= A:
        result += rest
    else:
        result += A
    print(result)
