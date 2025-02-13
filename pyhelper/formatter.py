import black

def format_code(code: str) -> str:
    """Format kode Python secara otomatis."""
    try:
        return black.format_str(code, mode=black.FileMode())
    except Exception as e:
        return f"Format Error: {e}"
