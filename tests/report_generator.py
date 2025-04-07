import pandas as pd

# Чтение Excel файла
df = pd.read_excel("salaries.xlsx")
#df = pd.read_excel('tests/salaries.xlsx')
# Преобразование даты
df['Date'] = pd.to_datetime(df['Date'])

# Фильтрация по 2023 году
df_2023 = df[df['Date'].dt.year == 2023]

# Группировка по сотруднику, расчёт средней ЗП
avg_salary = df_2023.groupby(['EmployeeID', 'Name'])['SalaryAmount'].mean().reset_index()

# Фильтрация сотрудников с ЗП > 100000
high_paid = avg_salary[avg_salary['SalaryAmount'] >= 100000]

# Сохранение результата
high_paid.to_excel("high_salary_report.xlsx", index=False)

print("Готово! Отчет сохранён в high_salary_report.xlsx")
