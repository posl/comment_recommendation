def main():
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if len(str(i))%2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                result += 1
    print(result)
