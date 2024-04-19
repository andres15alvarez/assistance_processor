import typer

from models.processor import Processor


def get_data_from_file(file: str) -> list[str]:
    data = []
    with open(file) as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip())
    return data


def process_data(data: list[str]) -> str:
    processor = Processor()
    for row in data:
        row = row.split()
        if row[0] == "Student":
            processor.register_student(row[1])
        elif row[0] == "Presence":
            processor.register_presence(row[1], row[2], row[3], row[4])
    return str(processor)


def main(file: str):
    data = get_data_from_file(file)
    result = process_data(data)
    print(result)


if __name__ == "__main__":
    typer.run(main)
