from setup import Setup
# Setup()

import os
from cv_creator import CV
from md2pdf import MD2PDF as m2p
# from md2pdf.core import md2pdf as m2p

info_file = 'info.json'

cv_md_file = 'CV.md'
cv_pdf_file = 'CV.pdf'
cv_css_file = 'cv.css'

rs_md_file = 'Resume.md'
rs_pdf_file = 'Resume.pdf'
rs_css_file = 'resume.css'

def generate_and_update_cv():
    cv = CV(info_file, cv_md_file)
    raw_cv = cv.main()
    print("\033[92m[+] \033[1mDynamicCVGenerator: \033[0m\033[92mCV Updated and created PDF successfully!\033[0m")

    if raw_cv:
        return raw_cv


def generate_and_update_pdf(raw_md=None):
    cv_css_file_path = None

    if os.path.exists(cv_css_file):
        cv_css_file_path = cv_css_file

    m2p(
        source_file=cv_md_file,
        destination_file=cv_pdf_file,
        css_file_path=cv_css_file_path,
        source_content=raw_md
    ).main()


def main():
    raw_cv = generate_and_update_cv()
    generate_and_update_pdf(raw_md=raw_cv)


if __name__ == "__main__":
    main()
