import ast

def check_syntax(code: str) -> str:
    """Cek apakah kode Python memiliki kesalahan sintaks."""
    try:
        ast.parse(code)
        return "Syntax Benar"
    except SyntaxError as e:
        return f"Syntax Error: {e}"
