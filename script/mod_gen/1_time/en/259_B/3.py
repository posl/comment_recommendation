def main():
  a, b, d = map(int, input().split())
  print(a * cos(radians(d)) - b * sin(radians(d)), a * sin(radians(d)) + b * cos(radians(d)))

if __name__ == '__main__':
    main()