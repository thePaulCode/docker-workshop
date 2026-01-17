from pathlib import Path 

current_dic = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dic}:")

for filepath in current_dic.iterdir():
    if filepath.name == current_file:
        continue

    print(f"    - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")