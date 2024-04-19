import typer
from typing_extensions import Annotated

from models.processor import Processor


def get_data_from_file(file: str) -> list[str]:
    """Get the commands from the txt file.

    Args:
        - file (str): filepath.

    Returns:
        - list[str]: list of commands.
    """
    data = []
    with open(file) as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip())
    return data


def process_data(data: list[str]) -> str:
    """Process every command listed from the file.

    Args:
        - data (list[str]): list of commands.

    Returns:
        - str: Report of the minutes of attendance of the students with days.
    """
    processor = Processor()
    for row in data:
        row = row.split()
        if len(row) == 0:
            continue
        if row[0] == "Student":
            if len(row) < 2:
                continue
            processor.register_student(row[1])
        elif row[0] == "Presence":
            if len(row) < 5:
                continue
            processor.register_presence(row[1], row[2], row[3], row[4])
    return str(processor)


def main(
    file: Annotated[str, typer.Argument(help="Filepath of the TXT file to process")]
):
    """
    Attendance Processor.
    """
    data = get_data_from_file(file)
    result = process_data(data)
    print(result)


if __name__ == "__main__":
    typer.run(main)
