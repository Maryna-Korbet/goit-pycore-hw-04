import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory_structure(directory: Path, indent: int = 0):

    if not directory.exists():
        print(Fore.RED + f"The path '{directory}' does not exist")
        return
    
    if not directory.is_dir():
        print(Fore.RED + f"The path '{directory}' is not a directory")
        return
    
    for item in sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if item.is_dir():
            print(" " * indent + Fore.BLUE + f"📂 {item.name}")
            visualize_directory_structure(item, indent + 4)
        elif item.is_file():
            print(" " * indent + Fore.GREEN + f"📜 {item.name}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "First step is: cd task3")
        print(Fore.RED + 'Second step is: python task3.py "./picture"')
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    print(Fore.YELLOW + f"Directory structure '{directory_path}':")
    visualize_directory_structure(directory_path)

if __name__ == "__main__":
    main()