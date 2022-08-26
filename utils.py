import argparse
import pandas
from collections import defaultdict

def get_year_word(year: int) -> str:
    '''
    Правильно возвращает слово после кол-ва лет
    (100 Лет, 101 Год, 102 Года)
    '''

    if (year % 10) == 1 and year != 11 and (year % 100) != 11:
        return 'год'

    elif 1 < (year % 10) <= 4 and year not in (12, 13, 14):
        return 'года'

    else:
        return 'лет'



def get_df_from_excel(file: str, na_values='') -> list:
    '''
    Возвращает данные (data frame) из таблицы excel в виде списка словарей

    file - имя файла
    na_values - чем заменить значения nan/Nan
    '''
    df_excel = pandas.read_excel(file,
                                 na_values=na_values,
                                 keep_default_na=False
                                 )

    return df_excel.to_dict(orient='records')


def create_category(iterable, category_key) -> dict:
    '''
    Формирует и возвращает словарь ключи которого название категории category_name_key,
    а значения список словарей.

    iterable - iterable object который содержит словари ключи которых
    являются названием категорий

    category_key - Название ключа, значение которого содержит название категории по которому
    будет идти отбор словарей

    Example:
    iterable:
    [{'Name': 'Caberne',
      'Category': 'Wine'},

     {'Name': 'Vodka',
      'Category': 'Belochka'}
    ]

    return:
    {'Wine': [{'Name': 'Caberne',
      'Category': 'Wine'}],
     'Belochka': [{'Name': 'Vodka',
      'Category': 'Belochka'}]
    }
    '''

    catalog_with_category = defaultdict(list)

    for dictionary in iterable:
        category_name = dictionary[category_key]
        catalog_with_category[category_name].append(dictionary)

    return catalog_with_category


def get_catalog(file: str, category_key, na_values=None) -> dict:
    '''
    Вспомогательная функция.
    Получает из файла xlsx список словарей
    и формирует из него словарь ключи которого имена категорий

    file_name - имя файла
    category_key - ключ словаря значение которого содержит имя категории
    na_values - чем заменить значения nan/Nan
    '''

    product_cards = get_df_excel(file, na_values=na_values)

    return create_category(product_cards, category_key)


def get_parser():
    '''
    Возвращает настроенный и заполненный парсер
    '''
    # defaults values
    tmpl_file = 'template.html'
    cat_key_name = 'Категория'
    ip = '127.0.0.1'
    port = 8000

    formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=52)

    parser = argparse.ArgumentParser(description='Run http server', formatter_class=formatter)
    parser.add_argument('file', help='The xlsx catalog file')
    parser.add_argument('--template-file', metavar='FILE', default=tmpl_file, help=f'Template html file default: {tmpl_file}')
    parser.add_argument('--category-key', metavar='STRING', default=cat_key_name, help=f'The name of the column in the catalog excel file default: {cat_key_name}')
    parser.add_argument('--ip', default=ip, help=f'IP address default: {ip}')
    parser.add_argument('--port', default=port, type=int, help=f'IP address default: {port}')

    return parser.parse_args()

