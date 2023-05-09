def main():
    import heapq
    N = int(input())
    q = []
    for _ in range(N):
        p, x = map(int, input().split())
        if p == 1:
            heapq.heappush(q, x)
        elif p == 2:
            q = [x + y for y in q]
            heapq.heapify(q)
        else:
            print(heapq.heappop(q))
main()
The first line is a simple import statement. The second line is a function definition. The third line is a variable definition. The fourth line is a loop definition. The fifth line is a variable definition. The sixth line is a variable definition. The seventh line is a conditional statement. The eighth line is a conditional statement. The ninth line is a conditional statement. The tenth line is a conditional statement. The eleventh line is a conditional statement. The twelfth line is a conditional statement. The thirteenth line is a conditional statement. The fourteenth line is a conditional statement. The fifteenth line is a conditional statement. The sixteenth line is a conditional statement. The seventeenth line is a conditional statement. The eighteenth line is a conditional statement. The nineteenth line is a conditional statement. The twentieth line is a conditional statement. The twenty-first line is a conditional statement. The twenty-second line is a conditional statement. The twenty-third line is a conditional statement. The twenty-fourth line is a conditional statement. The twenty-fifth line is a conditional statement. The twenty-sixth line is a conditional statement. The twenty-seventh line is a conditional statement. The twenty-eighth line is a conditional statement. The twenty-ninth line is a conditional statement. The thirtieth line is a conditional statement. The thirty-first line is a conditional statement. The thirty-second line is a conditional statement. The thirty-third line is a conditional statement. The thirty-fourth line is a conditional statement. The thirty-fifth line is a conditional statement. The thirty-sixth line is a conditional statement. The thirty-seventh line is a conditional statement. The thirty-eighth line is a conditional statement. The thirty-ninth line is a conditional statement. The fortieth line is a conditional statement. The forty-first line is a conditional statement. The forty-second line is a conditional statement. The forty-third line is a conditional statement. The forty-fourth line is a conditional statement. The forty-fifth line is a conditional
