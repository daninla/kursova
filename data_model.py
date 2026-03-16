
class ElectricityRecord:
    """
    Клас, що представляє один запис про споживання електроенергії.
    Кожен об'єкт зберігається динамічно і є елементом масиву покажчиків.
    """

    def __init__(self, date: str, apartment: str, consumption: float, cost: float, meter_reading: float):
        """
        Ініціалізація запису.

        :param date: Дата у форматі РРРР-ММ (наприклад, 2024-01)
        :param apartment: Номер квартири або назва приміщення
        :param consumption: Місячне споживання електроенергії (кВт·год)
        :param cost: Вартість за місяць (грн)
        :param meter_reading: Показник лічильника на кінець місяця (кВт·год)
        """
        self.date = date                    # Поле дати (рядок РРРР-ММ)
        self.apartment = apartment          # Номер квартири/приміщення
        self.consumption = float(consumption)  # Споживання, кВт·год (числове поле double)
        self.cost = float(cost)            # Вартість, грн
        self.meter_reading = float(meter_reading)  # Показник лічильника

    def __str__(self):
        """Рядкове представлення запису для відображення."""
        return (f"{self.date:<12} {self.apartment:<15} "
                f"{self.consumption:<15.2f} {self.cost:<12.2f} {self.meter_reading:<15.2f}")

    def to_file_line(self):
        """Перетворення запису в рядок для збереження у файл."""
        return f"{self.date},{self.apartment},{self.consumption},{self.cost},{self.meter_reading}\n"

    @staticmethod
    def from_file_line(line: str):
        """
        Статичний метод: створення об'єкта з рядка текстового файлу.
        Формат рядка: дата,квартира,споживання,вартість,показник
        """
        parts = line.strip().split(',')
        if len(parts) != 5:
            raise ValueError(f"Неправильний формат рядка: {line}")
        return ElectricityRecord(
            date=parts[0].strip(),
            apartment=parts[1].strip(),
            consumption=float(parts[2]),
            cost=float(parts[3]),
            meter_reading=float(parts[4])
        )

    @staticmethod
    def print_header():
        """Виведення заголовка таблиці."""
        print("-" * 75)
        print(f"{'Дата':<12} {'Квартира':<15} {'Споживання':<15} {'Вартість':<12} {'Показник лічил.':<15}")
        print(f"{'(РРРР-ММ)':<12} {'(номер)':<15} {'(кВт·год)':<15} {'(грн)':<12} {'(кВт·год)':<15}")
        print("-" * 75)
