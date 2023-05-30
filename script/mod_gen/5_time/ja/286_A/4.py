def swap_array(p,q,r,s,array)
  temp1 = array[p-1..q-1]
  temp2 = array[r-1..s-1]
  array[p-1..q-1] = temp2
  array[r-1..s-1] = temp1
  return array
end
n,p,q,r,s = gets.chomp.split.map(&:to_i)
array = gets.chomp.split.map(&:to_i)
puts swap_array(p,q,r,s,array).join(" ")
