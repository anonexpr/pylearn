# filter looks for output > 0 and returns only those elements
 
odd_arr = filter(lambda x: x%2, range(1,10))
print odd_arr

even_arr = filter(lambda x: x%2 == 0, range(1,10))
print even_arr
