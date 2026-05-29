FROM python:3.8
WORKDIR /code
ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "application.py"]
