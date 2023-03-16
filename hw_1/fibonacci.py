from typing import Optional

def fib(n: int) -> Optional[int]:
    f1, f2 = 0, 1    
    
    if n < 0:
        return None

    if n < 2:
        return [f1, f2][n]
    
    for _ in range(1, n):
        f1, f2 = f2, f1 + f2

    return f2
