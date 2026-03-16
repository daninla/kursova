
from data_model import ElectricityRecord


# -------------------------------------------------------
# ЗАПИТ 1: Введення інформації з текстового файлу
# -------------------------------------------------------
def load_from_file(filename: str) -> list:
    """
    Зчитує записи з текстового файлу і повертає масив покажчиків
    (список об'єктів ElectricityRecord).

    :param filename: Шлях до файлу
    :return: Список об'єктів ElectricityRecord
    """
    records = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                # Пропускаємо порожні рядки та коментарі (#)
                if not line or line.startswith('#'):
                    continue
                try:
                    record = ElectricityRecord.from_file_line(line)
                    records.append(record)  # Додаємо покажчик на об'єкт
                except ValueError as e:
                    print(f"  [Увага] Рядок {line_num} пропущено: {e}")
        print(f"  Успішно завантажено {len(records)} записів з '{filename}'.")
    except FileNotFoundError:
        print(f"  [Помилка] Файл '{filename}' не знайдено.")
    return records


# -------------------------------------------------------
# ЗАПИТ 2: Додавання нового елемента в кінець масиву
# -------------------------------------------------------
def add_record(records: list, record: ElectricityRecord) -> list:
    """
    Додає новий запис у кінець масиву.

    :param records: Поточний масив записів
    :param record: Новий об'єкт ElectricityRecord
    :return: Оновлений масив
    """
    records.append(record)  # Додаємо покажчик на новий об'єкт у кінець
    print(f"  Запис додано в кінець масиву. Всього елементів: {len(records)}.")
    return records


# -------------------------------------------------------
# ЗАПИТ 3: Перегляд всіх елементів масиву
# -------------------------------------------------------
def view_all(records: list):
    """
    Виводить усі записи у вигляді таблиці (один елемент — один рядок).

    :param records: Масив записів
    """
    if not records:
        print("  Масив порожній. Немає елементів для відображення.")
        return
    ElectricityRecord.print_header()
    for i, record in enumerate(records):
        # Виводимо номер елемента та дані запису
        print(f"[{i:>3}] {record}")
    print("-" * 75)
    print(f"  Всього записів: {len(records)}")


# -------------------------------------------------------
# ЗАПИТ 4: Виведення інформації в текстовий файл
# -------------------------------------------------------
def save_to_file(records: list, filename: str):
    """
    Зберігає всі записи масиву в текстовий файл.

    :param records: Масив записів
    :param filename: Шлях до файлу для збереження
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Заголовок-коментар у файлі
            f.write("# Формат: дата,квартира,споживання_кВтгод,вартість_грн,показник_лічильника\n")
            for record in records:
                f.write(record.to_file_line())
        print(f"  Збережено {len(records)} записів у файл '{filename}'.")
    except IOError as e:
        print(f"  [Помилка] Не вдалося записати файл: {e}")


# -------------------------------------------------------
# ЗАПИТ 5а: Сортування масиву алгоритмом Шелла
#           (сортування за полем consumption — місячне споживання)
# -------------------------------------------------------
def shell_sort(records: list) -> list:
    """
    Сортує масив записів за полем consumption (споживання кВт·год)
    алгоритмом сортування Шелла (Shell Sort).

    Алгоритм Шелла — вдосконалення сортування вставками.
    Спочатку порівнюються елементи, розташовані далеко один від одного
    (великий крок), потім крок зменшується до 1.

    :param records: Масив записів
    :return: Відсортований масив (на місці)
    """
    n = len(records)
    # Початковий крок — половина довжини масиву
    gap = n // 2

    while gap > 0:
        # Для кожного кроку виконуємо сортування вставками
        for i in range(gap, n):
            # Зберігаємо поточний елемент (покажчик на об'єкт)
            temp = records[i]
            j = i
            # Зсуваємо елементи, які більші за temp, на gap позицій вперед
            while j >= gap and records[j - gap].consumption > temp.consumption:
                records[j] = records[j - gap]
                j -= gap
            records[j] = temp  # Вставляємо temp на правильну позицію
        gap //= 2  # Зменшуємо крок вдвічі

    print("  Масив відсортовано за споживанням (алгоритм Шелла).")
    return records


# -------------------------------------------------------
# ЗАПИТ 5б: Лінійний пошук елемента за датою
# -------------------------------------------------------
def linear_search_by_date(records: list, search_date: str) -> list:
    """
    Виконує лінійний пошук записів за заданою датою.
    Повертає список індексів знайдених елементів.

    Лінійний пошук: перегляд кожного елемента масиву по черзі
    від першого до останнього.

    :param records: Масив записів
    :param search_date: Дата для пошуку (формат РРРР-ММ)
    :return: Список індексів знайдених записів
    """
    found_indices = []
    for i, record in enumerate(records):
        # Порівнюємо дату кожного запису з шуканою датою
        if record.date == search_date:
            found_indices.append(i)
    return found_indices


# -------------------------------------------------------
# ЗАПИТ 6: Вставка нового елемента ПЕРЕД обраним
# -------------------------------------------------------
def insert_before(records: list, index: int, record: ElectricityRecord) -> list:
    """
    Вставляє новий запис ПЕРЕД елементом з індексом index.

    :param records: Масив записів
    :param index: Індекс обраного елемента
    :param record: Новий об'єкт ElectricityRecord
    :return: Оновлений масив
    """
    if 0 <= index < len(records):
        records.insert(index, record)  # Вставка покажчика перед позицією index
        print(f"  Запис вставлено ПЕРЕД елементом [{index}]. Всього: {len(records)}.")
    else:
        print(f"  [Помилка] Індекс {index} виходить за межі масиву [0..{len(records)-1}].")
    return records


# -------------------------------------------------------
# ЗАПИТ 7: Вставка нового елемента ПІСЛЯ обраного
# -------------------------------------------------------
def insert_after(records: list, index: int, record: ElectricityRecord) -> list:
    """
    Вставляє новий запис ПІСЛЯ елемента з індексом index.

    :param records: Масив записів
    :param index: Індекс обраного елемента
    :param record: Новий об'єкт ElectricityRecord
    :return: Оновлений масив
    """
    if 0 <= index < len(records):
        records.insert(index + 1, record)  # Вставка покажчика після позиції index
        print(f"  Запис вставлено ПІСЛЯ елемента [{index}]. Всього: {len(records)}.")
    else:
        print(f"  [Помилка] Індекс {index} виходить за межі масиву [0..{len(records)-1}].")
    return records


# -------------------------------------------------------
# ЗАПИТ 8: Заміна обраного елемента
# -------------------------------------------------------
def replace_record(records: list, index: int, record: ElectricityRecord) -> list:
    """
    Замінює елемент масиву на новий запис (новий динамічний об'єкт).

    :param records: Масив записів
    :param index: Індекс елемента для заміни
    :param record: Новий об'єкт ElectricityRecord
    :return: Оновлений масив
    """
    if 0 <= index < len(records):
        records[index] = record  # Покажчик тепер вказує на новий об'єкт
        print(f"  Елемент [{index}] успішно замінено.")
    else:
        print(f"  [Помилка] Індекс {index} виходить за межі масиву [0..{len(records)-1}].")
    return records


# -------------------------------------------------------
# ЗАПИТ 9: Видалення елементів, починаючи від обраного
# -------------------------------------------------------
def delete_from_index(records: list, index: int) -> list:
    """
    Видаляє всі елементи масиву починаючи від індексу index до кінця.

    :param records: Масив записів
    :param index: Індекс першого елемента для видалення
    :return: Скорочений масив
    """
    if 0 <= index < len(records):
        count = len(records) - index  # Кількість елементів, що видаляються
        del records[index:]           # Видалення зрізу масиву
        print(f"  Видалено {count} елементів починаючи з [{index}]. Залишилось: {len(records)}.")
    else:
        print(f"  [Помилка] Індекс {index} виходить за межі масиву [0..{len(records)-1}].")
    return records


# -------------------------------------------------------
# ЗАПИТ 10: Статистика по діапазону значень споживання
# -------------------------------------------------------
def range_statistics(records: list, low: float, high: float):
    """
    Знаходить елементи, де споживання потрапляє в діапазон [low, high].
    Виводить їх таблицею, а також максимум, мінімум та середнє значення.

    :param records: Масив записів
    :param low: Нижня межа діапазону (кВт·год)
    :param high: Верхня межа діапазону (кВт·год)
    """
    # Фільтруємо записи, що потрапляють у діапазон
    filtered = [r for r in records if low <= r.consumption <= high]

    print(f"\n  Елементи зі споживанням від {low} до {high} кВт·год:")

    if not filtered:
        print("  Жодного запису не знайдено у вказаному діапазоні.")
        return

    # Виводимо відфільтровані елементи у вигляді таблиці
    ElectricityRecord.print_header()
    for record in filtered:
        print(f"      {record}")
    print("-" * 75)

    # Обчислення статистики
    consumptions = [r.consumption for r in filtered]
    max_val = max(consumptions)
    min_val = min(consumptions)
    avg_val = sum(consumptions) / len(consumptions)

    print(f"  Знайдено записів : {len(filtered)}")
    print(f"  Максимум         : {max_val:.2f} кВт·год")
    print(f"  Мінімум          : {min_val:.2f} кВт·год")
    print(f"  Середнє значення : {avg_val:.2f} кВт·год")


# -------------------------------------------------------
# Допоміжна функція: введення нового запису з клавіатури
# -------------------------------------------------------
def input_record_from_keyboard() -> ElectricityRecord:
    """
    Зчитує дані нового запису з клавіатури з перевіркою коректності.

    :return: Новий об'єкт ElectricityRecord
    """
    print("  Введіть дані нового запису:")

    # Введення дати з перевіркою формату
    while True:
        date = input("  Дата (РРРР-ММ, наприклад 2024-03): ").strip()
        if len(date) == 7 and date[4] == '-' and date[:4].isdigit() and date[5:].isdigit():
            break
        print("  [Помилка] Невірний формат дати. Використовуйте РРРР-ММ.")

    apartment = input("  Номер квартири / приміщення: ").strip()

    # Введення числового поля споживання
    while True:
        try:
            consumption = float(input("  Споживання (кВт·год): "))
            if consumption >= 0:
                break
            print("  [Помилка] Споживання не може бути від'ємним.")
        except ValueError:
            print("  [Помилка] Введіть числове значення.")

    # Введення вартості
    while True:
        try:
            cost = float(input("  Вартість (грн): "))
            if cost >= 0:
                break
            print("  [Помилка] Вартість не може бути від'ємною.")
        except ValueError:
            print("  [Помилка] Введіть числове значення.")

    # Введення показника лічильника
    while True:
        try:
            meter = float(input("  Показник лічильника (кВт·год): "))
            if meter >= 0:
                break
            print("  [Помилка] Показник лічильника не може бути від'ємним.")
        except ValueError:
            print("  [Помилка] Введіть числове значення.")

    return ElectricityRecord(date, apartment, consumption, cost, meter)


# -------------------------------------------------------
# Допоміжна функція: безпечне введення індексу
# -------------------------------------------------------
def input_index(records: list, prompt: str = "  Введіть індекс елемента: ") -> int:
    """
    Зчитує індекс елемента масиву з клавіатури з перевіркою меж.

    :param records: Масив записів (для перевірки меж)
    :param prompt: Підказка для введення
    :return: Коректний індекс
    """
    while True:
        try:
            index = int(input(prompt))
            if 0 <= index < len(records):
                return index
            print(f"  [Помилка] Введіть індекс від 0 до {len(records)-1}.")
        except ValueError:
            print("  [Помилка] Введіть ціле число.")
