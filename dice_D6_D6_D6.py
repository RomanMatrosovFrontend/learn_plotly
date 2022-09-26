from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

# Создание 3 кубиков D6
die1 = Die()
die2 = Die()
die3 = Die()

rolls = 5000000

# Моделирование серии бросков с сохранением результата в списке
results = []
for roll_num in range(rolls):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(1, max_result + 1))
data = Bar(x=x_values, y=frequencies)

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title=f'Results of rolling three D6 {rolls} times',
                  xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')