Скрипт запускает сервер http и посредством шаблонизации позволяет актуализировать карточки товаров с (https://github.com/devmanorg/wine)[сайта] магазина авторского вина "Новое русское вино".
Данные для карточек товаров, скрипт импортирует из файла xlsx.
Образец структуры данных в файле репозитория wines.xlsx. Вы можете отредактировать этот файл под свои нужды. Название столбцов менять нельзя.


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
