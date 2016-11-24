# reverse words in a string"
"Hello world" --> "world hello"

str = "Hello world"

arr_str = str.split()
rev_arr = arr_str[::-1]

str = ' '.join(rev_arr)

print(str)
