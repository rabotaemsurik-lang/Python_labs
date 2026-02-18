# Programming Principles

## Інкапсуляція

Приватний атрибут у класі Bank:
[Laba8.py#L6-L8](./Laba8.py#L6-L8)

Приватний баланс і доступ через геттер::
[Laba8.py#L20-L22](./Laba8.py#L20-L22)
---
## Наслідування
Клас Labrador наслідується від класу Dog :
[Laba8.py#L46-L50](./Laba8.py#L46-L50)
Клас Discount наслідується від класу Shop :
[Laba8.py#L140-L145](./Laba8.py#L140-L145)
Клас Admin наслідується від класу User :
[Laba8.py#L180-L185](./Laba8.py#L180-L185)
---
## Поліморфізм

Метод show_info юзається в Pets:
[Laba8.py#L35-L40](./Laba8.py#L35-L40)
[Laba8.py#L70-L75](./Laba8.py#L70-L75)
---
## Обробка винятків
Користувача виняток:
[Laba8.py#L100-L105](./Laba8.py#L100-L105)



SOLID Principles
S — Single Responsibility

Bank — фінансові операції:
[Laba8.py#L4](./Laba8.py#L4)
Buffer — тільки буфер і обчислення сум:
[Laba8.py#L77](./Laba8.py#L77)
O — Open/Closed
Класи-нащадки розширюють базові класи без зміни їхнього коду:
Наслідування Dog уLabrador, Bulldog
L — Liskov Substitution
Підставляння об’єктів-наступників (Labrador, Bulldog) у місцях, де очікується Dog:
[Laba8.py#L4](./Laba8.py#L70)
I — Interface Segregation
Окремий клас Privileges для привілеїв адміністратора:
[Laba8.py#L187](./Laba8.py#L187)
Це допомагає не перевантажувати клас Admin.
D — Dependency Inversion
Клас Pets залежить не від конкретної реалізації (Labrador, Bulldog, Dog), а від наявності методу show_info():
[Laba8.py#L35](./Laba8.py#L35)

