FROM python:slim-bullseye
LABEL maintainer "victor98dl <victor98dl@yahoo.com.br>"
COPY . /root/
# Define workdir
WORKDIR /root/

# Instalação de dependencias (sh)
RUN apt update && apt upgrade -y && apt install -y python3-pip && \
    pip install -U pip && pip3 install bottle pandas numpy scikit-learn joblib

# Copy os arquivos para o container


EXPOSE 5000

# Arquivo que será executado como entrypoint no container
ENTRYPOINT [ "python3" , "/root/classificador/classificador.py"]