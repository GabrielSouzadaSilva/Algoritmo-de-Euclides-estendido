def euclides (a, b):

  x,x1 = 1,0
  y,y1 = 0,1

  while True:
    #quotient
    quociente = int((a/b) - (a/b)%1)  # math.floor(a/b)

    a, b = b, a % b
    x, x1 = x1, x - (quociente * x1)
    y, y1 = y1, y - (quociente * y1)

    if b == 0 :
      return(a,x,y)
      break
