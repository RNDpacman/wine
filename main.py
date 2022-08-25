from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import utils

HOST, PORT = '127.0.0.1', 8000

# год основания компании
FOUNDED = 1920

# лет прошло с момента основания компании
YEARS = datetime.today().year - FOUNDED

# файл каталога
FILE_CATALOG = 'wine3.xlsx'

# Ключ который содержит название категорий
CAT_KEY = 'Категория'

# получаем каталог наших вин
WINES_CATALOG = utils.get_catalog(FILE_CATALOG, CAT_KEY, na_values=None)


print(f'open {HOST=}:{PORT=}')

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
                years_ago=f'Уже {YEARS} {utils.year_word(YEARS)} с вами',
                wines=WINES_CATALOG
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
server.serve_forever()
