from markdown2 import markdown, markdown_path
from weasyprint import HTML, CSS
from .exceptions import ValidationError


class MD2PDF:
    """
    Converts input markdown to styled HTML and renders it to a PDF file.

    Args:
        destination_file: output PDF file path.
        source_content: input markdown raw string content.
        source_file: input markdown file path.
        css_file_path: input styles path (CSS).
        base_url: absolute base path for markdown linked content (as images).

    Returns:
        None

    Raises:
        ValidationError: if md_content and source_file are empty.
    """
    def __init__(self, source_file: str = None, source_content: str = None, destination_file: str = None, css_file_path: str = None, base_url: str = None):
        # Offline
        self.souerce_file = source_file
        self.source_content = source_content
        self.destination_file = destination_file

        # Styling
        self.css_file_path = css_file_path

        # NetInstall
        self.base_url = base_url

    def md2html(self):
        ret = ''
        extras = ['cuddled-lists', 'tables', 'footnotes']

        if self.souerce_file:
            ret = markdown_path(self.souerce_file, extras=extras)

        elif self.source_content:
            ret = markdown(self.source_content, extras=extras)

        if not len(ret):
            raise ValidationError('Input markdown seems empty')

        return ret
    
    def get_css(self):
        ret = []

        if self.css_file_path:
            ret.append(CSS(self.css_file_path))

        return ret

    def main(self):
        raw_html = self.md2html()
        html = HTML(string=raw_html, base_url=self.base_url)
        css = self.get_css()

        html.write_pdf(self.destination_file, stylesheets=css)
