Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 4) + max(A % 10, B % 10, C % 10, D % 10, E % 10))

=======
Suggestion 2

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((A+B+C+D+E+9)//10*10)

=======
Suggestion 3

def solve():
    A, B, C, D, E = map(int, input().split())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10) + E)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(10 * (5 + (max(a, b, c, d, e) - 1) // 10))

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(min(((a+9)//10)*10, ((b+9)//10)*10, ((c+9)//10)*10, ((d+9)//10)*10, ((e+9)//10)*10) + max(a, b, c, d, e))

=======
Suggestion 6

def solve():
    T = [int(input()) for _ in range(5)]
    T.sort()
    if T[4] % 10 == 0:
        print(sum(T))
    else:
        print(sum(T) - (T[4] % 10) + 10)

=======
Suggestion 7

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

=======
Suggestion 8

def get_min_time():
    dishes = [int(input()) for _ in range(5)]
    min_time = 0
    for dish in dishes:
        if dish % 10 != 0:
            min_time += (dish // 10 + 1) * 10
        else:
            min_time += dish
    return min_time - max([dish for dish in dishes if dish % 10 != 0])

print(get_min_time())

=======
Suggestion 9

def main():
    # List of dishes
    dishes = []
    # List of times
    times = []
    # Number of dishes
    num_dishes = 5
    # Get input
    for i in range(0, num_dishes):
        dish = input()
        dishes.append(dish)
        # Calculate the time to serve each dish
        time = int(dish) // 10
        # If the time is not a multiple of 10, add 1
        if time % 10 != 0:
            time += 1
        times.append(time)
    # Get the maximum time
    max_time = max(times)
    # Get the index of the maximum time
    index = times.index(max_time)
    # Get the time to serve the last dish
    last_dish_time = dishes[index]
    # Calculate the total time
    total_time = last_dish_time + (max_time * 10)
    # Print the total time
    print(total_time)

main()
