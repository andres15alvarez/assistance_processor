from datetime import timedelta

from models.student import Student


class Processor:
    def __init__(self) -> None:
        """
        Processor of students attendance
        """
        self.students: dict[str, Student] = {}

    def __str__(self) -> str:
        students = self.sort()
        return "\n".join([str(student) for student in students])

    def sort(self) -> list[Student]:
        """Sort students by minutes in descending order.

        Returns:
            - list[Student]: list of students sorted.
        """
        students = list(self.students.values())
        students.sort(reverse=True)
        students = filter(lambda x: x > 4, students)
        return students

    def register_student(self, student_name: str):
        """Register new student.

        Args:
            - student_name (str): Name of the student to register.
        """
        student = self.students.get(student_name)
        if student is None:
            self.students[student_name] = Student(student_name)

    def convert_hour_str_to_object(self, hour: str) -> timedelta:
        """Convert hour in string representation to timedelta object.

        The format of the string must be HH:MM to be parsed correctly.

        Args:
            - hour (str): hour in format HH:MM with 24 hours.

        Returns:
            - timedelta: time object with the hours and minutes
        """
        hour_separated = hour.split(":")
        return timedelta(hours=int(hour_separated[0]), minutes=int(hour_separated[1]))

    def register_presence(
        self, name: str, day: int, initial_hour: str, final_hour: str
    ):
        """Register attendance of a student.

        Args:
            - name (str): Name of the student,
            - day (int): number of the day of the week from 1 to 7.
            - initial_hour (str): hour in format HH:MM with 24 hours.
            - final_hour (str): hour in format HH:MM with 24 hours.
        """
        student = self.students.get(name)
        if student is None:
            return
        initial_hour = self.convert_hour_str_to_object(initial_hour)
        final_hour = self.convert_hour_str_to_object(final_hour)
        if final_hour < initial_hour:
            return
        student.register_presence(day, initial_hour, final_hour)
