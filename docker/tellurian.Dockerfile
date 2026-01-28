FROM python:3.12-alpine3.23

ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_IGNORE_VIRTUALENVS=1
ENV PIPENV_NOSPIN=1
ENV PIPENV_HIDE_EMOJIS=1


RUN mkdir -p /tellurian
COPY . /tellurian
WORKDIR /tellurian
RUN uv sync

CMD ["uv", "run", "python", "-m", "tellurian"]
