# Космический Инстаграм

Проект позволяет скачать фотографии Земли, космических объектов и запусков космических аппаратов с помощью API SpaceX и Nasa.

## Как установить

Для запуска проекта необходимо выполнить последовательность действий:

### 1. Получаем Nasa API Key

- Заходим на сайт https://api.nasa.gov/
- Заполняем форму и получаем API-ключ

Ключ выглядит как комбинация букв в различном регистре и цифр, например: `TfbQZApcTjCARDXB3N86NI0m0qnhyG1lthB36EZM` (ключ нерабочий, приведен для ознакомительных целей). 

### 2. Регистрируем нового Телеграм-бота

Для регистрации необходимо зайти в специального телеграм-бота [@BotFather](https://telegram.me/BotFather) и ввести следующую команду:

```
/newbot
```
BotFather предложит задать имя и username для нового бота. Задаем и получаем в ответном сообщении токен для API. Он выглядит примерно так: `958423683:AAEAtJ5Lde5YYfkjergber` (токен нерабочий и представлен для ознакомления).

### 3. Создаем новый Телеграм-канал

После регистрации делаем созданного в шаге 2 бота администратором этого канала. Записываем `chat_id` канала (это ссылка на него, например `@BotFather`, если не помните - можно посмотреть в Channel Info).

### 4. Создаем в корне проекта файл .env

В файл нужно поместить полученные токены и chat_id в следующем формате:

```
NASA_TOKEN=
TG_TOKEN=
CHAT_ID=
```


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Как запустить

Для скачивания фотографий, запуска бота и загрузки фотографий в канал необходимо выполнить следующую команду:

```
python3 bot.py
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).