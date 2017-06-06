# Eventex

Sistema de Eventos encomendado pelo Cliente

## Como desenvolver?

1. Clone o repositório.
2. Cria um virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone github.com:rvettori/eventex-rv.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância do heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py` # hbn.link/secret_gen
heroku config:set DEBUG=False
# configurando o email
git push heroku master --force
```