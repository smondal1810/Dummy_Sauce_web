FROM python:3.10

WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps

# Now copy project files
COPY . .

CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]
