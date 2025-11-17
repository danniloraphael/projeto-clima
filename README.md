# Projeto Clima

Aplicação Django simples para visualizar o clima de cidades usando a API OpenWeatherMap.

**Resumo:** Esta aplicação permite buscar a previsão/clima atual de uma cidade e exibir informações básicas (temperatura, descrição, ícone, umidade e hora local) via uma interface web.

**Tecnologias:**
- Python 3.x
- Django
- requests
- OpenWeatherMap API

**Pré-requisitos**
- Ter Python 3.8+ instalado
- Ter `pip` disponível
- Ter uma chave de API do OpenWeatherMap (gratuita)

## Instalação

1. Clone o repositório:

```shell
git clone git@github.com:danniloraphael/projeto-clima.git
cd projeto-clima
```

2. Crie e ative um ambiente virtual (opcional):

```shell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependências:

```shell
pip install -r requirements.txt
```

4. Crie o arquivo `.env` (recomendado) 

No arquivo `.env` crie uma variável para a sua chave da api (sem aspas, sem 'export', apenas NOME=VALOR):

```shell
OPENWEATHER_API_KEY=Sua_Chave_Aqui
```

5. Configuração da API (OpenWeatherMap)

1. Crie uma conta em https://openweathermap.org/ e gere uma API Key (chave gratuita geralmente disponível após registro).
2. Coloque a chave na variável de ambiente `OPENWEATHER_API_KEY`.

6. Aplique as migrações:

```shell
python manage.py migrate
```

7. Execute o servidor de desenvolvimento:

```shell
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` no navegador para usar a aplicação.

## Uso

- A tela principal permite inserir o nome de uma cidade e ver o clima atual.
- Se a cidade não for encontrada a aplicação deve mostrar uma mensagem de 'cidade não encontrada'.
- A aplicação usa ícones e dados retornados pela API.

## Estrutura do projeto (resumo)

- `project/` — configurações Django (settings, urls, wsgi, asgi)
- `weather/` — app principal (models, views, templates, static)
- `templates/weather/index.html` — página principal
- `static/weather/css/style.css` — estilos
