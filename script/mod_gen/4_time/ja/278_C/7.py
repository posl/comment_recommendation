def follow?(a, b)
  return false if @follows[a].nil? || @follows[a].empty?
  return @follows[a].include?(b)
end

if __name__ == '__main__':
    follow?()