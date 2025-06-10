from setuptools import setup

APP = ['busca_name.py']  # seu arquivo principal do app
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pandas', 'openpyxl', 'tkinter'],  # pacotes que usa
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
