from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name


def read_text_auto(path: Path) -> str:
    """
    Decode a text file by detecting common BOMs.

    This prevents failures when a file is UTF-16 (e.g. BOM 0xFF 0xFE)
    but the caller assumes UTF-8.
    """
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe"):
        return raw.decode("utf-16le")
    if raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16be")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig")
    # Fallback for plain UTF-8 (or empty files)
    return raw.decode("utf-8")


print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = read_text_auto(filepath)
        print(f"    Content: {content}")