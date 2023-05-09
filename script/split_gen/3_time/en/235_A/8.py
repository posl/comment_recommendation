def main():
    # Read the input
    abc = int(input())
    # Split the input into digits
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    # Calculate the answer
    ans = a + b + c + a * 100 + b * 10 + c * 1
    # Print the answer
    print(ans)
