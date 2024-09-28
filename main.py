from setup import Setup
Setup()

from cv_creator import CV
from md2pdf import MD2PDF as m2p

info_file = 'info.json'

cv_md_file = 'CV.md'
rs_md_file = 'Resume.md'

cv_pdf_file = 'CV.pdf'
rs_pdf_file = 'Resume.pdf'

def generate_and_update_cv():
    cv = CV(info_file, cv_md_file)
    cv.main()
    m2p(cv_md_file, cv_pdf_file).main()
    print("\033[92m[+] \033[1mDynamicCVGenerator: \033[0m\033[92mCV Updated and created PDF successfully!\033[0m")


def main():
    generate_and_update_cv()


if __name__ == "__main__":
    main()
