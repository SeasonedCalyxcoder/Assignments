class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        self.original_year = year
        self.month = month
        self.day = day

        # Adjust month and year for Jan/Feb
        if month < 3:
            self.month += 12
            self.year = year - 1
        else:
            self.year = year

        self.K = self.year % 100         # Year of the century
        self.J = self.year // 100        # Zero-based century

    def calculate_day_of_week(self) -> str:
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        # Zeller's Congruence Formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        # Map result to day name
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

    def display_result(self):
        weekday = self.calculate_day_of_week()
        print(f"{self.original_year}-{self.month if self.month <= 12 else self.month - 12}-{self.day} was a {weekday}.")

# Example usage
if __name__ == "__main__":
    # Example: What day was September 15, 1589?
    date = DateCalculator(1589, 9, 15)
    date.display_result()
