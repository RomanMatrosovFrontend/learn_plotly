from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

# Создание двух кубиков D6
die1 = Die(8)
die2 = Die(8)

# Моделирование серии бросков с сохранением результата в списке
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(1, max_result + 1))
data = Bar(x=x_values, y=frequencies)

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling a D8 and a D8 50000 times',
                  xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')