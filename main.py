import pandas as pd

# Імпортуємо дані з нашої таблиці
file_path = "task_2_data.xlsx"
data = pd.read_excel(file_path)

# Рахуємо заробіток за 3 місяці з одного користувача (для всіх 40 тижнів рахуємо для 12 тижнів) і
# потім ділимо на кількість завантажень
data['Total revenue per 3 month'] = data.iloc[:, 2:14].sum(axis=1)
data['Revenue per user per 3 months'] = data['Total revenue per 3 month'] / data['Number of installs']
avg_per_user_3m = round(data['Revenue per user per 3 months'].mean(), 2)
print(f'Компанія заробляє з одного користувача за 3 місяці: {avg_per_user_3m} дол.')

# Рахуємо заробіток за 1 рік з одного користувача (для всіх 40 тижнів рахуємо для 40 тижнів, так як
# в нас є тільки 40 тижнів в таблиці) і потім ділимо на кількість завантажень
data['Total revenue per 1 year'] = data.iloc[:, 2:42].sum(axis=1)
data['Revenue per user per 1 year'] = data['Total revenue per 1 year'] / data['Number of installs']
avg_per_user_1y = round(data['Revenue per user per 1 year'].mean(), 2)
print(f'Компанія заробляє з одного користувача за 1 рік: {avg_per_user_1y} дол.')
