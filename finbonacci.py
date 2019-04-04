# Using Recurcion
def fib_2(n, memo):
  if memo[n] is not None:
    return memo[n]
  elif n == 1 or n == 2:
    return 1
  else:
    result = fib(n-1) + fib(n-2)
  
  memo[n] = result
  return result

def fib_recur(n):
  memo = [None] * (n+1)
  return fib_2(n, memo)

#Using Buttom-up
def fib(n):
  if n == 1 or n== 2:
    return 1

  buttom_up = [1, 1]
  for i in range(2, n+1):
    print(buttom_up[i-1] + buttom_up[i-2])
  
  return buttom_up[n]

print(fib(5))