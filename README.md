# Attendance Processor

###  This project is a CLI app to proccess students attendance and generate reports of the time spends in class

Prerequisites of the project:
- Python 3.11
- Virtualenv 20.25.3

## Create the virtual environment
```bash
    $ virtualenv venv -p python3.11
```
Onche the virtual environemnt is created, you need to activate it
```bash
    $ source venv/bin/activate
```
Then install the requirements.
```bash
    $ pip install -r requirements.txt
```
Activate pre-commit hooks
```bash
    $ pre-commit install
```

## Run the project
As a CLI app you can obtain information about the usage of the command, so you can get the infomation with:
```bash
    $ python manage.py --help
```
And get the help text
```bash
Usage: main.py [OPTIONS] FILE

 Attendance Processor.

╭─ Arguments ────────────────────────────────────────────────────────────────────────────╮
│ *    file      TEXT  Filepath of the TXT file to process [default: None] [required]    │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯

```

The file `fixture.txt` contain dummy data to test the CLI.

## Example
```bash
    $ python manage.py fixture.txt
```
