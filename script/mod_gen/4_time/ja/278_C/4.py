def follow(a, b)
  if @follows[a].include?(b)
    puts 'Yes'
  else
    puts 'No'
  end
end

if __name__ == '__main__':
    follow()