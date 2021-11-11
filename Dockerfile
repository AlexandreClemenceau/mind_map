FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD [ "python", "main.py" ]

#docker build -t mind_map:v1 .
#docker run -dit --rm -p 5000:5000 --name mind_map mind_map:v1