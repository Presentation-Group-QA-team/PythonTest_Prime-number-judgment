def Prime(n):
  c = 2
  while c < n:
    if n % c == 0:
      print('Not Prime.')
      break
    c += 1
  if c == n:
    print('Is prime.')
n = 1
while(n >= 0):
  n = int(input('intput number (Enter:=<0 exit.) :'))
  Prime(n)
