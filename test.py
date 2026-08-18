# Шаг 1: создаём файл с данными
with open('test_ids.txt', 'w') as f:
    f.write('\n111\n222\n333')

# Шаг 2: открываем в 'a+' и пытаемся прочитать
with open('test_ids.txt', 'r') as f:
    content = f.read()
    print(f"Прочитано:{content}")
    print(f"Длина: {len(content)}")
