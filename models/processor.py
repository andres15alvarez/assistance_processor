from datetime import timedelta

from models.student import Student


class Processor:
    def __init__(self) -> None:
        self.students: dict[str, Student] = {}

    def __str__(self) -> str:
        students = self.sort()
        return "\n".join([str(student) for student in students])

    def sort(self):
        students = list(self.students.values())
        students.sort(reverse=True)
        students = filter(lambda x: x > 4, students)
        return students

    def register_student(self, student_name: str):
        student = self.students.get(student_name)
        if student is None:
            self.students[student_name] = Student(student_name)

    def convert_hour_str_to_object(self, hour: str) -> timedelta:
        hour_separated = hour.split(":")
        return timedelta(hours=int(hour_separated[0]), minutes=int(hour_separated[1]))

    def register_presence(
        self, name: str, day: int, initial_hour: str, final_hour: str
    ):
        student = self.students.get(name)
        if student is None:
            return
        initial_hour = self.convert_hour_str_to_object(initial_hour)
        final_hour = self.convert_hour_str_to_object(final_hour)
        if final_hour < initial_hour:
            return
        student.register_presence(day, initial_hour, final_hour)
