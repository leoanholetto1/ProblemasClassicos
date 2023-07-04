def fib(n: int) -> []:
    fib_list = []
    fib_list.append(1)
    if n > 1:
        fib_list.append(1)
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

print(str(fib(54)))
