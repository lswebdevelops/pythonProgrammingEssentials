x = 0
y = 0

def myfunc():
  global x, y
  x = x + 1
  y = y + 1

  

myfunc()
print(x, y)
myfunc()
print(x, y)


# print("Python is " + x)