from typing import Iterable

def suma(a: float, b: float) -> float:
    """Suma dos números (ejemplo simple)."""
    return a + b

def media(xs: Iterable[float]) -> float:
    """Media aritmética; lanza ValueError si la lista está vacía."""
    xs = list(xs)
    if not xs:
        raise ValueError("Lista vacía")
    return sum(xs) / len(xs)
