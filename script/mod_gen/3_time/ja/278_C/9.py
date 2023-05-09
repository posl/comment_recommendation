def follow?(a, b)
  $follow[a].include?(b)
end

if __name__ == '__main__':
    follow?()