def main():
    N = int(input())
    cnt = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i > N or j > N:
                continue
            if str(i) == str(j):
                cnt += 1
    for i in range(1, 10):
        for j in range(1, 10):
            if i > N or j > N:
                continue
            if str(i) == str(j):
                cnt += 1
    print(cnt)
