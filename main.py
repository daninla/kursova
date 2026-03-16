from data_model import ElectricityRecord
from operations import (
    load_from_file,
    add_record,
    view_all,
    save_to_file,
    shell_sort,
    linear_search_by_date,
    insert_before,
    insert_after,
    replace_record,
    delete_from_index,
    range_statistics,
    input_record_from_keyboard,
    input_index,
)


# ============================================================
#  головнe меню
# ============================================================
def print_menu():
    """Виводить головне меню програми."""
    print("\n" + "=" * 55)
    print("   АНАЛІЗ СПОЖИВАННЯ ЕЛЕКТРОЕНЕРГІЇ В БУДИНКУ")
    print("=" * 55)
    print("  1.  Завантажити дані з файлу")
    print("  2.  Додати запис у кінець масиву")
    print("  3.  Переглянути всі записи")
    print("  4.  Зберегти дані у файл")
    print("  5.  Сортування (Шелл) / Пошук за датою (лінійний)")
    print("  6.  Вставити запис ПЕРЕД обраним")
    print("  7.  Вставити запис ПІСЛЯ обраного")
    print("  8.  Замінити обраний запис")
    print("  9.  Видалити елементи починаючи від обраного")
    print("  10. Статистика по діапазону споживання")
    print("  0.  Вихід")
    print("=" * 55)


# ============================================================
# Головна функція програми
# ============================================================
def main():
    """
    Головна функція: ініціалізація масиву покажчиків та цикл меню.
    Масив records — це список покажчиків на динамічні об'єкти
    класу ElectricityRecord.
    """
    # Масив покажчиків на записи (динамічні об'єкти)
    records: list = []

    print("\n  Програма 'Аналіз споживання електроенергії в будинку'")
    print("  Варіант №12 | Сортування Шелла | Лінійний пошук")

    # ---- Головний цикл меню ----
    while True:
        print_menu()
        choice = input("  Ваш вибір: ").strip()

        # --------------------------------------------------
        #  Завантаження з файлу
        # --------------------------------------------------
        if choice == '1':
            print("\n--- Завантаження з файлу ---")
            filename = input("  Введіть ім'я файлу (або Enter для 'data1.txt'): ").strip()
            if not filename:
                filename = 'data1.txt'
            loaded = load_from_file(filename)
            if loaded:
                records = loaded  # Замінюємо поточний масив завантаженим

        # --------------------------------------------------
        #  Додавання запису в кінець
        # --------------------------------------------------
        elif choice == '2':
            print("\n--- Додавання запису в кінець масиву ---")
            new_record = input_record_from_keyboard()
            records = add_record(records, new_record)
            # Після зміни масиву — виводимо всі елементи
            print()
            view_all(records)

        # --------------------------------------------------
        #  Перегляд всіх записів
        # --------------------------------------------------
        elif choice == '3':
            print("\n--- Перегляд всіх елементів масиву ---")
            view_all(records)

        # --------------------------------------------------
        #  Збереження у файл
        # --------------------------------------------------
        elif choice == '4':
            print("\n--- Збереження у файл ---")
            if not records:
                print("  Масив порожній. Нема чого зберігати.")
            else:
                filename = input("  Введіть ім'я файлу (або Enter для 'output.txt'): ").strip()
                if not filename:
                    filename = 'output.txt'
                save_to_file(records, filename)

        # --------------------------------------------------
        #  Сортування Шелла / Лінійний пошук
        # --------------------------------------------------
        elif choice == '5':
            print("\n--- Сортування та пошук ---")
            print("  5а. Сортування масиву за споживанням (алгоритм Шелла)")
            print("  5б. Лінійний пошук за датою")
            sub = input("  Виберіть (5а або 5б): ").strip().lower()

            if sub in ('5а', '5a', 'а', 'a'):
                # Сортування Шелла
                if not records:
                    print("  Масив порожній.")
                else:
                    records = shell_sort(records)
                    print()
                    view_all(records)

            elif sub in ('5б', '5b', 'б', 'b'):
                # Лінійний пошук за датою
                if not records:
                    print("  Масив порожній.")
                else:
                    search_date = input("  Введіть дату для пошуку (РРРР-ММ): ").strip()
                    indices = linear_search_by_date(records, search_date)
                    if indices:
                        print(f"\n  Знайдено {len(indices)} запис(ів) з датою '{search_date}':")
                        ElectricityRecord.print_header()
                        for idx in indices:
                            print(f"[{idx:>3}] {records[idx]}")
                        print("-" * 75)
                    else:
                        print(f"  Записів з датою '{search_date}' не знайдено.")
            else:
                print("  Невірний вибір підпункту.")

        # --------------------------------------------------
        # Вставка ПЕРЕД обраним
        # --------------------------------------------------
        elif choice == '6':
            print("\n--- Вставка ПЕРЕД обраним елементом ---")
            if not records:
                print("  Масив порожній. Спочатку додайте елементи.")
            else:
                view_all(records)
                index = input_index(records)
                new_record = input_record_from_keyboard()
                records = insert_before(records, index, new_record)
                # Після зміни масиву — виводимо всі елементи
                print()
                view_all(records)

        # --------------------------------------------------
        #  Вставка ПІСЛЯ обраного
        # --------------------------------------------------
        elif choice == '7':
            print("\n--- Вставка ПІСЛЯ обраного елемента ---")
            if not records:
                print("  Масив порожній. Спочатку додайте елементи.")
            else:
                view_all(records)
                index = input_index(records)
                new_record = input_record_from_keyboard()
                records = insert_after(records, index, new_record)
                # Після зміни масиву — виводимо всі елементи
                print()
                view_all(records)

        # --------------------------------------------------
        #  Заміна обраного елемента
        # --------------------------------------------------
        elif choice == '8':
            print("\n--- Заміна обраного елемента ---")
            if not records:
                print("  Масив порожній.")
            else:
                view_all(records)
                index = input_index(records)
                print(f"  Поточний елемент [{index}]: {records[index]}")
                print("  Введіть новий запис для заміни:")
                new_record = input_record_from_keyboard()
                records = replace_record(records, index, new_record)
                # Після зміни масиву — виводимо всі елементи
                print()
                view_all(records)

        # --------------------------------------------------
        # Видалення починаючи від обраного
        # --------------------------------------------------
        elif choice == '9':
            print("\n--- Видалення елементів від обраного до кінця ---")
            if not records:
                print("  Масив порожній.")
            else:
                view_all(records)
                index = input_index(records, "  Введіть індекс першого елемента для видалення: ")
                # Попередження перед видаленням
                count = len(records) - index
                confirm = input(f"  Буде видалено {count} елемент(ів). Підтвердіть (т/н): ").strip().lower()
                if confirm in ('т', 'y', 'yes', 'так'):
                    records = delete_from_index(records, index)
                    # Після зміни масиву — виводимо всі елементи
                    print()
                    view_all(records)
                else:
                    print("  Видалення скасовано.")

        # --------------------------------------------------
        #  Статистика по діапазону
        # --------------------------------------------------
        elif choice == '10':
            print("\n--- Статистика по діапазону споживання ---")
            if not records:
                print("  Масив порожній.")
            else:
                # Введення меж діапазону
                while True:
                    try:
                        low = float(input("  Нижня межа діапазону (кВт·год): "))
                        break
                    except ValueError:
                        print("  [Помилка] Введіть числове значення.")
                while True:
                    try:
                        high = float(input("  Верхня межа діапазону (кВт·год): "))
                        if high >= low:
                            break
                        print("  [Помилка] Верхня межа має бути >= нижньої.")
                    except ValueError:
                        print("  [Помилка] Введіть числове значення.")
                range_statistics(records, low, high)

        # --------------------------------------------------
        # Вихід
        # --------------------------------------------------
        elif choice == '0':
            print("\n  Завершення роботи програми. До побачення!")
            break

        else:
            print("  [Помилка] Невірний вибір. Введіть число від 0 до 10.")

        # Пауза перед поверненням до меню
        input("\n  Натисніть Enter для продовження...")


if __name__ == '__main__':
    main()
