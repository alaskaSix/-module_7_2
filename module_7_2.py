def custom_write(file_name, strings):
    strings_positions = {}  #словарь для хранения позиций байтов и соответствующих строчек
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            byte_position = file.tell()  #позиция байта
            file.write(string + '\n')
            strings_positions[(line_number, byte_position)] = string  # Сохраняем информацию в словарь
    return strings_positions

# Пример использования функции:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)