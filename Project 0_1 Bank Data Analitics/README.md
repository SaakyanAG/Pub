# Проект 0_1. Разведовательный анализ банковских данных об оттоке клиентов

## Оглавление  
[1. Описание проекта](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Результат)    
[6. Выводы](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Выводы) 

### Описание проекта    
Были предоставлены данные об оттоке клиентов банка. Необходимо было ответить на ряд вопросов по заданию, используя изученные иснутрменты визуализации.

:arrow_up:[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать Jupyter Notebook, содержащий строки кода для чтения, обработки и визуализации данных

**Метрика качества**     
Качественная визуализация с правильными выводами в качестве ответа на вопросы

**Что практикуем**     
Учимся писать хороший код на python, работать с данными загруженными из файла, строить визуализации с помощью разных библиотек.


### Краткая информация о данных
```
churn_data = pd.read_csv('data/churn.csv')
churn_data.head()
```
Столбцы таблицы:

#### RowNumber — номер строки таблицы (это лишняя информация, поэтому можете сразу от неё избавиться)
#### CustomerId — идентификатор клиента
#### Surname — фамилия клиента
#### CreditScore — кредитный рейтинг клиента (чем он выше, тем больше клиент брал кредитов и возвращал их)
#### Geography — страна клиента (банк международный)
#### Gender — пол клиента
#### Age — возраст клиента
#### Tenure — сколько лет клиент пользуется услугами банка
#### Balance — баланс на счетах клиента в банке
#### NumOfProducts — количество услуг банка, которые приобрёл клиент
#### HasCrCard — есть ли у клиента кредитная карта (1 — да, 0 — нет)
#### IsActiveMember — есть ли у клиента статус активного клиента банка (1 — да, 0 — нет)
#### EstimatedSalary — предполагаемая заработная плата клиента
#### Exited — статус лояльности (1 — ушедший клиент, 0 — лояльный клиент)
#### Итак, банк обращается к вам за помощью: он хочет разработать кампанию лояльности по удержанию клиентов, но для этого ему необходимо, чтобы вы выяснили основные причины оттока клиентов. Иными словами, нужно установить, чем ушедшие клиенты отличаются от лояльных и как между собой связаны различные признаки, определяющие клиентов.

После разведывательного анализа, с целью выявления наиболее важных признаков оттока, банк сможет построить модель машинного обучения, которая будет прогнозировать уход клиента. 
  
:arrow_up:[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Оглавление)


### Этапы работы над проектом  
#### 1. Каково соотношение ушедших и лояльных клиентов? Покажите это на графике и дайте комментарий по соотношению.

#### 2. Постройте график, показывающий распределение баланса пользователей, у которых на счету больше 2 500 долларов. Опишите распределение и сделайте выводы.

#### 3. Посмотрите на распределение баланса клиента в разрезе признака оттока. Как различаются суммы на накопительном счёте ушедших и лояльных клиентов? Подумайте и напишите, с чем это может быть связано, что может не устраивать ушедших клиентов в банке.

#### 4. Посмотрите на распределение возраста в разрезе признака оттока. В какой группе больше потенциальных выбросов? На какую возрастную категорию клиентов стоит обратить внимание банку?

#### 5. Постройте график, который показывает взаимосвязь кредитного рейтинга клиента и его предполагаемой зарплаты. Добавьте расцветку по признаку оттока клиентов. Какова взаимосвязь между признаками? Если не видите явной взаимосвязи, укажите это.

#### 6. Кто чаще уходит, мужчины или женщины? Постройте график, который иллюстрирует это.

#### 7. Как отток клиентов зависит от числа приобретённых у банка услуг? Для ответа на этот вопрос постройте многоуровневую столбчатую диаграмму.

#### 8. Как влияет наличие статуса активного клиента на отток клиентов? Постройте диаграмму, иллюстрирующую это. Что бы вы предложили банку, чтобы уменьшить отток клиентов среди неактивных?

#### 9. В какой стране доля ушедших клиентов больше? Постройте тепловую картограмму, которая покажет это соотношение на карте мира. Предположите, с чем это может быть связано.

#### 10. Переведите числовой признак CreditScore в категориальный. Для этого воспользуйтесь функцией get_credit_score_cat(), которая приведена ниже. Примените её к столбцу CreditScore и создайте новый признак CreditScoreCat — категории кредитного рейтинга.

:arrow_up:[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Оглавление)


### Результаты:  
Наличие понятной визуализации для ответа на каждый вопрос. Наличие понятных выводов из визуализации.

:arrow_up:[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Оглавление)


### Выводы:  
1. Произведен разведовательный анализ данных, на которых можно дальше построить модель для машинного обучения.
2. Получены навыки правильного оформаления построения визуализаций, написания кода и публикации его на GitHub.

:arrow_up:[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project%200_1%20Bank%20Data%20Analitics/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами