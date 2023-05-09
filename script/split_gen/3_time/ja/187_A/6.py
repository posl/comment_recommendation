def main():
    a,b = map(int, input().split())
    a_sum = sum(map(int, str(a)))
    b_sum = sum(map(int, str(b)))
    print(max(a_sum, b_sum))
