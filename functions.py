def my_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

n = int(input("Input a Fibonacci sequence's word count: "))

fibonacci_sequence = my_fibonacci(n)
print("The Fibonacci series upto th word count", n, ":", fibonacci_sequence)
