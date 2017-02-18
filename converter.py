import os, re
import json
import pdb
from bs4 import BeautifulSoup
from django.utils.text import slugify
import collections

sourceLink = "http://quod.lib.umich.edu/c/cme/browse.html"
source = "Corpus of Middle English Prose and Verse"


def jaggedListToDict(text):
	node = { str(i): t for i, t in enumerate(text) }
	node = collections.OrderedDict(sorted(node.items(), key=lambda k: int(k[0])))
	for child in node:
		if isinstance(node[child], list):
			if len(node[child]) == 1:
				node[child] = node[child][0]
			else:
				node[child] = jaggedListToDict(node[child])
	return node

def main():
	if not os.path.exists('cltk_json'):
		os.makedirs('cltk_json')

	for root, dirs, files in os.walk("."):
		path = root.split('/')
		print((len(path) - 1) * '---', os.path.basename(root))
		for fname in files:
			if fname.endswith('sgm'):
				print((len(path)) * '---', fname)
				with open(os.path.join(root, fname), encoding='utf-8') as f:
					try:
						data = f.read()
					except UnicodeDecodeError:
						#
						# To do: fix the occasional unicode errors reading files
						#
						continue

					data = re.sub(r'<PB[^<]+?>', " ", data)
					soup = BeautifulSoup(data, 'html.parser')

				title = soup.title
				if title:
					title = title.text
				else:
					titles = soup.findAll('titlepart')
					titles = [elem.text for elem in titles]
					title = ": ".join(titles)

				author = soup.author

				if author:
					author = soup.author.text
				else:
					author = 'Not available'

				work = {
					'originalTitle': title,
					'englishTitle': title,
					'author': author,
					'source': source,
					'sourceLink': sourceLink,
					'language': 'middle_english',
					'text': {},
					'fname': os.path.join(root, fname),
				}

				text = []
				divs = soup.body.findAll("div1")
				for i, div in enumerate(divs):
					div2s = div.findAll('div2')
					text.append([])
					for j, div2 in enumerate(div2s):
						text[i].append([])
						hasChildren = False
						for elem in div2.children:
							strings = []
							hasChildren = True
							try:
								strings = [s.strip() for s in elem.strings if len(s.strip())]
							except AttributeError:
								if len(elem.strip()):
									strings = [elem.strip()]

							if len(strings):
								text[i][j].append(" ".join(strings))

						if not hasChildren:
							strings = [s.strip() for s in div2.strings if len(s.strip())]
							text[i][j].append(" ".join(strings))

					if len(div2s) == 0:
						strings = [s.strip() for s in div.strings if len(s.strip())]
						text[i].append(" ".join(strings))

				if len(divs) == 0:
					text = [s.strip() for s in soup.body.strings if len(s.strip())]

				work['text'] = jaggedListToDict(text)
				fname = slugify(work['source']) + '__' + slugify(work['englishTitle'][0:140]) + '__' + slugify(work['language']) + '.json'
				fname = fname.replace(" ", "")
				with open('cltk_json/' + fname, 'w') as f:
					json.dump(work, f)



if __name__ == '__main__':
	main()
