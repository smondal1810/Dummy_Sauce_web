FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m playwright install --with-deps

CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]
