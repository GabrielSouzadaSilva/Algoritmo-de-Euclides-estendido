def euclides (A, B):

  #variáveis para efetuar trocas
  a, b = A,B
  x,x1 = 1,0
  y,y1 = 0,1

  while True:
    #quotient
    quociente = int((a/b) - (a/b)%1)  # math.floor(a/b)

    a, b = b, a % b
    x, x1 = x1, x - (quociente * x1)
    y, y1 = y1, y - (quociente * y1)

    if b == 0 :
      return(a,x,y) # tais que MDC(A,B) = a = x * A + y * B
      break
