def safe_eval(expression: str) -> str:
    """Evaluasi ekspresi Python secara aman."""
    allowed_builtins = {"abs": abs, "round": round, "min": min, "max": max, "sum": sum}
    try:
        result = eval(expression, {"__builtins__": allowed_builtins})
        return f"Hasil: {result}"
    except Exception as e:
        return f"Eval Error: {e}"
