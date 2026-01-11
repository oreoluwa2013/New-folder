def fibonacci(n):
    a=1
    b=2
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)