import pandas
from collections import defaultdict

def year_word(year: int) -> str:
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



def get_data_excel(file_name: str, na_values='') -> list:
    '''
    Возвращает данные из таблицы excel в виде списка словарей

    file_name - имя файла
    sheet_name - имя листа в книге
    na_values - чем заменить значения nan/Nan
    '''
    excel_data_df = pandas.read_excel(file_name,
                                      na_values=na_values,
                                      keep_default_na=False
                                      )

    return excel_data_df.to_dict(orient='records')



def create_category(iterable, category_name_key) -> dict:
    '''
    Формирует и возвращает словарь ключи которого название категории category_name_key,
    а значения список словарей.

    iterable - iterable object который содержит словари ключи которых
    являются названием категорий

    category_name_key - Название ключа, значение которого содержит название категории по которому
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
        category_name = dictionary[category_name_key]
        catalog_with_category[category_name].append(dictionary)

    return catalog_with_category


def get_catalog(file_name: str, category_name_key, na_values=None) -> dict:
    '''
    Вспомогательная функция.
    Получает из файла xlsx список словарей
    и формирует из него словарь ключи которого имена категорий

    file_name - имя файла
    category_name_key - ключ словаря значение которого содержит имя категории
    na_values - чем заменить значения nan/Nan
    '''

    dictionary_list = get_data_excel(file_name, na_values=na_values)

    return create_category(dictionary_list, category_name_key)
