Controle de estoque

## Como rodar o projeto?

*   Clone esse repositorio
*   Crie uma virtualenv com python 3
*   Ative a virtualenv
*   Instale as dependencias
*   Rode as migrações


Passos a ser feito quando for abrir o porjeto pela primeira vez em uma maquina ->

    git clone https://github.com/rg3915/estoque.git
    cd estoque
    python3 -m venv .venv
    .venv/bin/activate -Windows
    pip install -r requirements.txt
    python contrib/env_gen.py
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver