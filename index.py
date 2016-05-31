"""Make index file of Middle English corpus."""

import json
import os

from bs4 import BeautifulSoup


if __name__ == '__main__':
    file_list = os.listdir('xml')
    xml_list = [f for f in file_list if f.endswith('.xml')]

    title_dict = {}
    for xml_file in xml_list:
        bs = BeautifulSoup(open(os.path.join('xml/', xml_file)), 'lxml')
        title_node = bs.find("title")
        title = title_node.string
        title_dict[xml_file] = title

    with open('index_file_title.json', 'w') as file_open:
        json.dump(title_dict, file_open, indent=4, sort_keys=True)
