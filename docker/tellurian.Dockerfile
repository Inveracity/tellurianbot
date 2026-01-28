FROM python:3.12-alpine3.23

RUN apk add --no-cache curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

RUN mkdir -p /tellurian
COPY . /tellurian
WORKDIR /tellurian
RUN uv sync

CMD ["uv", "run", "python", "-m", "tellurian"]
