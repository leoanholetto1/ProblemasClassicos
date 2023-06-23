def calculate_pi(n: int) -> float:
    numerator: float = 4.0
    denominador: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n):
        pi += operation * (numerator/denominador)
        denominador += 2
        operation *= -1
    return pi

if __name__ == "__main__":
    print(calculate_pi(1000000))