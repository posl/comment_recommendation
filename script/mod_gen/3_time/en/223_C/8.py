def main():
    n = int(input())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    # print(a_b)
    total_length = sum([x[0] for x in a_b])
    half_length = total_length / 2
    # print(total_length, half_length)
    current_length = 0
    current_speed = 0
    for a, b in a_b:
        current_length += a
        current_speed += b
        if current_length > half_length:
            break
    # print(current_length, current_speed)
    print(current_speed * (current_length - half_length) / current_speed)

if __name__ == '__main__':
    main()