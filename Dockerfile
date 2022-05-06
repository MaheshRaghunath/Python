FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \ 
    python3 -m pip install --upgrade Pillow && \
    pip install --upgrade setuptools  && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
    build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser -D user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R user:user /vol && \
    chmod -R 755 /vol/web && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER user

CMD ["entrypoint.sh"]  