# Проект 0. Угадай число

## Оглавление

[1. Описание проекта](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Описание-проекта)
[2. Какой кейс решаем?](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Какой-кейс-решаем)
[3. Краткая информация о данных](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Краткая-информация-о-данных)
[4. Этапы работы над проектом](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Этапы-работы-над-проектом)
[5. Результат](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Результат)
[6. Выводы](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Выводы)

### Описание проекта

Необходимо понять, что из себя представляют данные и насколько они соответствуют целям проекта. В литературе эта часть работы над  *ML* -проектом называется  *Data Understanding* , или анализ данных.

⬆️[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Оглавление)

### Какой кейс решаем?

Необходимо с помощью SQL-запросов к источнику данных в виде SQL базы данных на Postres происзвести разведовательный анализ данных. Установить некоторые зависимости и сделать выводы, основанные на анализе.

**Что практикуем**
Учимся писать хороший код на python, структурированные запросы на SQL, оформлять проекты в GIt.

### Краткая информация о данных

Данные представлены в виде базы данных SQL.

![img](https://lms.skillfactory.ru/assets/courseware/v1/efd63819603e7d4f4433ed2fedec717c/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_1.png)

**VACANCIES**

Таблица хранит в себе данные по вакансиям и содержит следующие столбцы:

![img](https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_2.png)

Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли). Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.

**AREAS**

Таблица-справочник, которая хранит код города и его название.

![img](https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_3.png)

**EMPLOYERS**

Таблица-справочник со списком работодателей.

![img](https://lms.skillfactory.ru/assets/courseware/v1/d2a26db623c75572c71923b57241e038/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_4.png)

**INDUSTRIES**

Таблица-справочник вариантов сфер деятельности работодателей.

![img](https://lms.skillfactory.ru/assets/courseware/v1/2c76bca09937a1a05a9e66d51008e298/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_5.png)

**EMPLOYERS_INDUSTRIES**

Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.

Эта таблица нужна нам, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их). Для удобства анализа необходимо хранить запись по каждой сфере каждого работодателя в отдельной строке таблицы.

⬆️[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Оглавление)

### Этапы работы над проектом

**Gроект включает в себя несколько этапов:**

* знакомство с данными;
* предварительный анализ данных;
* детальный анализ вакансий;
* анализ работодателей;
* предметный анализ.

⬆️[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Оглавление)

### Результаты:

Результаты оформлены в виде Jupyter notebook с результатами отработки ячеек.

⬆️[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Оглавление)

### Выводы:

1. Получен навыки общения с внешней бд для получения данных.
2. Получены навыки написания структурированных запросов на SQL.
3. Получены навыки правильного оформаления документации, написания кода и публикации его на GitHub.

⬆️[к оглавлению](https://github.com/SaakyanAG/Pub/tree/main/Project_0%20Game%20Number%20Guess/README.md#Оглавление)

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
