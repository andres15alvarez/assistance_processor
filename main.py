import typer


def main(file: str):
    with open(file) as file:
        lines = file.readlines()
        for line in lines:
            print(line)


if __name__ == "__main__":
    typer.run(main)
