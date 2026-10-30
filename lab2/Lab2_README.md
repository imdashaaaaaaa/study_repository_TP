# Основы ООП 
## Задача - Реализовать иерархию классов:

<img width="2036" height="1742" alt="image" src="https://github.com/user-attachments/assets/f798adbe-288b-456a-b23a-4819cd94c13b" />

GameObject - базовый класс, от которого наследуются все игровые объекты. Он содержит основную информацию об объектах:

`int getId()` - возвращает идентификатор объекта

`String getName()` - возвращает имя объекта

`int getX()` - где находится объект по X координате

`int getY()` - где находится объект по Y координате

Unit - класс, описывающий юниты - подразделения, люди, рабочие и т.д., которых можно контролировать:

`boolean isAlive()` - возвращает, жив ли юнит

`float getHp()` - возвращает количество здоровья у юнита

`void receiveDamage(float damage)` - метод, который вызывается для получения урона этим юнитом

Archer - класс, описывающий лучника:

он реализует два интерфейса: Attacker и Moveable

Attacker - то, что может атаковать другие юниты:

`void attack(Unit unit)` - метод, принимающий юнит, которому наносится урон

Building - класс, описывающий постройку:

`boolean isBuilt()` - возвращает, построена ли постройка или ещё нет

Fort - класс крепости, тоже реализует интерфейс Attacker (может из пушек стрелять в противников)

MobileHouse - класс дома на колёсах, реализует интерфейс Moveable

# Выполнение: 

## Интерфейсы (умения):
<img width="660" height="472" alt="image" src="https://github.com/user-attachments/assets/d3c353c4-5a99-4260-9136-b35292578a3a" />

## Базовые классы: 
<img width="1109" height="1361" alt="image" src="https://github.com/user-attachments/assets/d9bb51d2-3e01-44bb-893d-f0f1a7be9a72" />

## Конкретные классы:
<img width="1057" height="1102" alt="image" src="https://github.com/user-attachments/assets/2b498479-fc57-4396-adbb-29a11ff20f39" />


## Тестирование: 
<img width="1833" height="598" alt="image" src="https://github.com/user-attachments/assets/03369d64-b88e-4e19-8c8a-7d6ade97116c" />


<img width="1004" height="846" alt="image" src="https://github.com/user-attachments/assets/e0380ed9-7051-4e94-99e2-ed51f86f1f3c" />

