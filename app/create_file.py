import os
import sys
import datetime
from typing import List


def create_directory(dirs: List[str]) -> None:
    try:
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        print(f"Directory {"/".join(dirs)} created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def create_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            line_number = 1

            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1

            print(f"File {file_path} updated successfully.")
    except Exception as e:
        print(f"Error creating or updating file: {e}")


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dirs = sys.argv[dir_index: sys.argv.index("-f")]
        file_name = sys.argv[sys.argv.index("-f") + 1]

        create_directory(dirs)
        create_file(os.path.join(*dirs, file_name))

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dirs = sys.argv[dir_index:]
        create_directory(dirs)

    elif "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        create_file(file_name)

    else:
        print("Invalid arguments. Use -d for directories and -f for files.")


if __name__ == "__main__":
    main()
