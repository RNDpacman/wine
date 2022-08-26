import argparse
import utils
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

FOUNDED = 1920



def main():

    years = datetime.today().year - FOUNDED

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )


    args = utils.get_parser()

    product_cards_catalog = utils.get_catalog(args.file, args.category_key, na_values=None)

    template = env.get_template(args.template_file)

    rendered_page = template.render(
                    years_ago=f'Уже {years} {utils.get_year_word(years)} с вами',
                    product_cards_catalog=product_cards_catalog
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer((args.ip, args.port), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
