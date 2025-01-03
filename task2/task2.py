from pathlib import Path 

def get_cats_info(path: str) -> list:
    file_path = Path(path)
    cats_info = []

    try: 
        with open(file_path, "r") as file:
            for line in file:
                try:
                    id_, name, age = line.strip().split(",")
                    cats_info.append({"id": id_, "name": name, "age": age})
                except ValueError:
                    print(f"Invalid line omitted: {line.strip()}")

        if not cats_info:
            print(f"File by path '{file_path}' is empty")
            return []

    except FileNotFoundError:
        print(f"File by path '{file_path}' not found")
        return []
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return []

    return cats_info

if __name__ == "__main__":
    cats_info = get_cats_info("task2/cats_file.txt")
    print(cats_info)    