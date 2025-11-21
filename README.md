# Отчеты по CSV-файлам сотрудников

## Описание
* Консольный инструмент для генерации отчетов по данным сотрудников из CSV-файлов.
* Испульзует argparse и csv из стандартной библиотеки и выводит таблицы через tabulate.
* Архитектура раширяема: новые отчеты добавляются отдельными классами.

## Требования
* Python 3.9+
* tabulate (для вывода таблиц)
* pytest (для тестов)
* pandas (для тестов)

## Установка
* Установить зависимости:
  * pip install tabulate
  * pip install pytst (Для тестов)
  * pip install pandas (Для тестов)

## Запуск
* Отчет по средней эффективности по позициям:


  		python3 main.py --files employees1.csv employees2.csv --report performance

## Шаблон нового отчета.
* Создайте новый класс в reports.py
  
	    class YourReport(Report):
	        name = 'your_report'
	        description = 'Описание'
  
	        def compute(self, rows: list[dict]) -> tuple[list[str], list[tuple]]:
	            headers = ['Колонка1', 'Колонка 2']
	            data = []

				return headers, data

* Зарегистрируйте отчет

  		register_report(YourReport())
