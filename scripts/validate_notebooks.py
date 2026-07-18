from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
failed = False

for path in sorted((root / "notebooks").glob("*.ipynb")):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell.get("source", []))
        try:
            compile(code, f"{path.name}::cell_{index}", "exec")
        except SyntaxError as exc:
            failed = True
            print(f"FAIL {path.name}, cell {index}: {exc}")
    if not failed:
        print(f"PASS {path.name}")

raise SystemExit(1 if failed else 0)
