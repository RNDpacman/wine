Скрипт запускает сервер http и посредством шаблонизации позволяет актуализировать карточки товаров с (сайта)[https://github.com/devmanorg/wine] магазина авторского вина "Новое русское вино".
Данные для карточек товаров, скрипт импортирует из файла xlsx.

### Образец структуры данных
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

Образец структуры данных в файле репозитория `product_cards_example.xlsx`. Вы можете отредактировать этот файл под свои нужды. Название столбцов менять нельзя.


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

### Run

```
python ./main.py
```
