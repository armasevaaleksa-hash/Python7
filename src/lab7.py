def process_data():
    filename_in = "data1.txt"

    #читання файлу та сума
    try:
        with open(filename_in, "r", encoding="utf-8") as file:
            lines = file.readlines()
            numbers = []
            for line in lines:
                cleaned_line = line.strip()
                if cleaned_line:
                    numbers.append(int(cleaned_line))

        total_sum = sum(numbers)
        print(f"[INFO] З файлу '{filename_in}' прочитано {len(numbers)} чисел.")
        print(f"[INFO] Сума всіх чисел: {total_sum}")

        #запит порога и запис в filtered_data1.txt
        user_threshold_str = input("Введіть поріг для фільтрації чисел: ")
        user_threshold = int(user_threshold_str)

        filtered_numbers = [n for n in numbers if n > user_threshold]
        filename_out = "filtered_data1.txt"

        with open(filename_out, "w", encoding="utf-8") as file_out:
            for num in filtered_numbers:
                file_out.write(f"{num}\n")
        print(f"[INFO] У файл '{filename_out}' записано {len(filtered_numbers)} чисел, більших за {user_threshold}.")

        #парні числа
        target_filename = input("Введіть ім'я файлу, який хочете відфільтрувати за парністю (напр. data1.txt): ")

        with open(target_filename, "r", encoding="utf-8") as target_file:
            target_lines = target_file.readlines()
            target_numbers = [int(line.strip()) for line in target_lines if line.strip()]

            even_numbers = [n for n in target_numbers if n % 2 == 0]
            print(f"[INFO] З файлу '{target_filename}' прочитано та відфільтровано парні числа:")
            print(*even_numbers)

    except FileNotFoundError:
        print(f"[ERROR] Файл не знайдено!")
    except ValueError:
        print(f"[ERROR] Помилка: у файлі містяться не лише числа або введено некоректне значення!")
    except IOError as e:
        print(f"[ERROR] Помилка введення-виведення (IOError): {e}")


if __name__ == "__main__":
    process_data()
    print("Роботу завершено.")
