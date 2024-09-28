from markdown import *
from pdfkit import *


class MD2PDF:
    def __init__(self, source, destination):
        self.souerce = source
        self.destination = destination

    def decode_md(self):
        with open(self.souerce, 'r') as f:
            return markdown(f.read())

    def save(self, content):
        from_string(content, self.destination)

    def main(self):
        decoded_md = self.decode_md()
        self.save(decoded_md)
