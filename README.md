# python-flask-docker
Чобану Светлана
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/praveengovi/emotions-dataset-for-nlp

Задача: предсказать эмоцию текста

Используемые признаки:

- sentence (text)

Преобразования признаков: CountVectorizer

Модель: MultinomialNB

### Клонируем репозиторий и создаем образ
```
$ git clone  https://github.com/LanaTch/project_ml_in_b.git
$ cd project_ml_in_b
$ docker build -t my_project .
```

### Запускаем контейнер
```
$ docker run -d -p 8081:8081 -p 5000:5000 my_project
```

### Переходим на localhost:8081
