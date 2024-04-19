from datetime import timedelta


class Student:
    def __init__(self, name: str) -> None:
        """Student model.

        Args:
            - name (str): Name of the student.
        """
        self.name: str = name
        self.days: int = 0
        self.minutes: float = 0
        self.days_of_week: list[int] = []

    def __str__(self) -> str:
        record = f"{self.name}: {self.minutes} minutes"
        if self.days > 0:
            record += f" in {self.days} days"
        return record

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __gt__(self, other) -> bool:
        if isinstance(other, int):
            return self.minutes > other
        return self.minutes > other.minutes

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            return self.minutes < other
        return self.minutes < other.minutes

    def calculate_minutes(
        self, initial_hour: timedelta, final_hour: timedelta
    ) -> float:
        """Calculate the minutes spend in class.

        Args:
            - initial_hour (timedelta): hour in which the student come to class.
            - final_hour (timedelta): hour in which the student out of class.

        Returns:
            - float: minutes in class.
        """
        time_in_class = final_hour - initial_hour
        return time_in_class.seconds / 60

    def register_presence(
        self, day: int, initial_hour: timedelta, final_hour: timedelta
    ):
        """Register student time of presence.

        Args:
            - day (int): number from 1 to 7 indicating day of week.
            - initial_hour (timedelta): hour in which the student come to class.
            - final_hour (timedelta): hour in which the student out of class.
        """
        if day not in self.days_of_week:
            self.days_of_week.append(day)
            self.days += 1
        self.minutes += self.calculate_minutes(initial_hour, final_hour)
