FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos primeiro, para aproveitar o cache de camadas do Docker
COPY requirements.txt ./

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte do seu aplicativo para o container
COPY . .

RUN python manage.py collectstatic --noinpu

# Exponha a porta que o uWSGI vai usar
EXPOSE 7000

# Define o comando para rodar o aplicativo
CMD ["uwsgi", "--http", "0.0.0.0:7000", "--module", "demostenes:app"]