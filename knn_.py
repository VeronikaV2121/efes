import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

# Загрузка данных
data = load_iris()
# Разделение данных на обучающую и тестовую выборки
X1, X2, y1, y2 = train_test_split(data['data'], data['target'], test_size=0.25, random_state=10)

# Создание модели и обучение на обучающей выборке
model = KNeighborsClassifier(n_neighbors=10)
model.fit(X1, y1)

# Тестирование модели на тестовой выборке и вывод отчета о классификации
print(classification_report(y2, model.predict(X2)))

# Кросс-валидация модели с использованием 10-кратного разбиения на выборки
result = cross_val_score(model, data['data'], data['target'], cv=10, scoring='accuracy')

# Вывод результатов кросс-валидации и среднего значения точности
print(result)
print(result.mean())