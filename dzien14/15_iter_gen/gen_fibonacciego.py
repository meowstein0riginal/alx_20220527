def fib(limit):
    start = 1
    while fib(start-1) + fib(start-2) <= 1:
        yield 1
        end
    while limit <=limit:
        yield fib(n-1) + fib(n-2)

for x in fib(10):
   print(x)
