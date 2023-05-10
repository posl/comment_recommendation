def main():
  s = input()
  weather = ['Sunny', 'Cloudy', 'Rainy']
  print(weather[(weather.index(s)+1)%3])
