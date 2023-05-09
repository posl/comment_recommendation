def main():
    K = int(input())
    q = [2, 20, 202, 2022, 20222, 202222, 2022222, 20222222, 202222222, 2022222222]
    for i in range(10):
        q.append(q[i] * 10 + 2)
        q.append(q[i] * 10 + 20)
        q.append(q[i] * 10 + 202)
        q.append(q[i] * 10 + 2022)
    q.sort()
    print(q[K - 1])

if __name__ == '__main__':
    main()