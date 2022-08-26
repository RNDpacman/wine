Скрипт запускает сервер http и посредством шаблонизации позволяет актуализировать карточки товаров с [сайта](https://github.com/devmanorg/wine) магазина авторского вина "Новое русское вино".
Данные для карточек товаров, скрипт импортирует из файла xlsx.

### Пример структуры данных
| **Категория**   | **Название**        | **Сорт**        | **Цена** | **Картинка**              | **Акция**            |
| --------------- | ------------------- | --------------- | -------- | ------------------------- | -------------------- |
| Белые вина      | Белая леди          | Дамский пальчик | 399      | belaya\_ledi.png          | Выгодное предложение |
| Белые вина      | Ркацители           | Ркацители       | 499      | rkaciteli.png             |                      |
| Белые вина      | Кокур               | Кокур           | 450      | kokur.png                 |                      |
| Белые вина      | Шардоне             | Шардоне         | 315      | shardone.png              |                      |
| Красные вина    | Черный лекарь       | Качич           | 399      | chernyi\_lekar.png        |                      |
| Красные вина    | Хванчкара           | Александраули   | 550      | hvanchkara.png            |                      |
| Красные вина    | Киндзмараули        | Саперави        | 550      | kindzmarauli.png          |                      |
| Красные вина    | Гранатовый браслет  | Бомжур          | 250      | granatovyi\_braslet.png   | Дешман               |
| Красные вина    | Изабелла            | Изабелла        | 296      | izabella.png              | Акция                |
| Крепкие Напитки | Коньяк классический |                 | 350      | konyak\_klassicheskyi.png |                      |
| Крепкие Напитки | Чача                |                 | 299      | chacha.png                | Выгодное предложение |
| Крепкие Напитки | Коньяк кизиловый    |                 | 350      | konyak\_kizilovyi.png     |                      |

В репозитории находится образец этих данных в файле `product_cards_example.xlsx`.

Вы можете отредактировать этот файл под свои нужды. Название столбцов менять нельзя (за исключением столбца `Категория`) без правки кода.


### Install

```
git clone https://github.com/devmanorg/wine.git
```

```
git clone https://github.com/RNDpacman/wine.git tmp
```

```
cp -R ./tmp/* ./wine/
```

```
python -m venv ./wine
```

```
cd ./wine
```

```
source ./bin/activate
```

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Help

```
python ./main.py --help

usage: main.py [-h] [--template-file FILE] [--category-key STRING] [--ip IP] [--port PORT] file

Run http server

positional arguments:
  file                  The xlsx catalog file

options:
  -h, --help            show this help message and exit
  --template-file FILE  Template html file default: template.html
  --category-key STRING
                        The name of the column in the catalog excel file default: Категория
  --ip IP               IP address default: 127.0.0.1
  --port PORT           IP address default: 8000
```

### Run

```
python ./main.py ./product_cards_example.xlsx
```
Затем откройте сайт в браузере http://127.0.0.1:8000
