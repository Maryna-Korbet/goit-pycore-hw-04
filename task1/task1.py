from pathlib import Path

def total_salary(path: str) -> tuple:
    file_path = Path(path)

    try:
        with open(file_path, "r") as file:
            salaries = []

            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Invalid line omitted: {line.strip()}")

            if not salaries:
                return 0, 0  

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"File by path '{file_path}' not found")
        return 0, 0
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return 0, 0

# Приклад використання
if __name__ == "__main__":
    total, average = total_salary("task1/salary_file.txt")
    print(f"The total amount of salary: {total}, The average salary: {average}")