# Barra de Progresso Utilizando Celery no Windows

Este simples projeto demonstra uma maneira de implementar uma `barra de progresso` em aplicações `django` utilizando o `celery` com broker em  `redis`, e `python 3` no ambiente do `Windows 10`.

### Bibliotecas utilizadas.
* **Python 3.9.6**
* **django 3.2.6**
* **mysqlclient 2.0.3** ==> Base de dados que será utilizada pelo `django`.
* **redis 3.5.3** ==> Base de dados que será alimentada `celery`.
* **gevent 21.8.0** ==> Auxiliará na compatibilidade do `celery` no `windows 10`
* **celery 5.1.2** ==> Criará `tasks` para monitorar o progresso de execução.
* **django-celery-results 2.2.0** ==>Intermediará a comunicação do `django` com o `celery`.


## Estrutura do projeto
```txt
├── progress
│   ├── progress # Site
│   │   ├── __init__.py # Inicializa o celery.
│   │   ├── asgi.py
│   │   ├── celery.py # configurações pra inicialização do celery.
│   │   ├── asgi.py
│   │   ├── settings.py # Configurações do sistema.
│   │   └── urls.py # urls do site.
│   │
│   ├── service # App
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tasks.py # Contém os métodos assíncronos.
│   │   ├── tests.py
│   │   ├── urls.py # Urls do app.
│   │   └── views.html # Métodos do app.
│   │
│   ├── manage.py # Inicializador do projeto.		
│   └── requeriments.txt # Dependências do sistema.
│
├── venv # ambiente virtual.
├── .gitignore # Arquivos exclusos do git.
└── README.md # Descrição do projeto.
```
## Instalação (Windows)

Primeiramente é necessário instalar o **python 3.9.6**.
Baixe e instale o [python](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe).
Baixe e instale o servidor [Redis](https://github.com/downloads/rgl/redis/redis-2.4.6-setup-64-bit.exe).
Após clonar o repositório:

Criando ambiente virtual.
```bash
$ python -m venv venv
```
Ativando o ambiente virtual.
```bash
$ source venv/Scripts/activate
```
Instalando dependências de pacotes.
```bash
$ pip install -r requirements.txt
```
## Executando o Sistema
Entre na pasta `progress`.
```bash
$ cd progress
```
Aplique os  `migrates`.
```bash
$ python manage.py migrate
```
Execute o sistema.
```bash
$ python manage.py runserver
```
Agora em outra aba do terminal, dentro do repositório, inicie o `ambiente virtual`, entre na pasta `progress` e inicialize o o `worker` do `celery`
```bash
$ celery -A progress worker -l info -P gevent
```
E finalmente no navegador acesse o endereço [127.0.0.1:8000](http://127.0.0.1:8000)

## Fontes
Este exemplo foi construído baseado nas seguintes documentações e projetos.

* [First steps with Django — Celery 5.1.2 documentation (celeryproject.org)](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
* [celery/django-celery-results: Celery result back end with django (github.com)](https://github.com/celery/django-celery-results)
* [celery-progress: Drop in, configurable, dependency-free progress bars for your Django/Celery applications. (github.com)](https://github.com/czue/celery-progress)
* [How to Create a Celery Task Progress Bar in Django](https://www.youtube.com/watch?v=BbPswIqn2VI)
* [python - How to run celery on windows? - Stack Overflow](https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows)