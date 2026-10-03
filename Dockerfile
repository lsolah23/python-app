FROM python:3.12-alpine 

COPY ./requirements.txt /tmp

# Crear el entorno virtual durante la construcción
RUN python3 -m venv /opt/venv

# Exportar la ruta del venv para los siguientes comandos y la ejecución del contenedor
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r /tmp/requirements.txt

COPY src /src

CMD python3 /src/app.py


