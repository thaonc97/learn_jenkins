FROM python:3.7.7-slim
COPY . /sample_app/

# Install requirements
WORKDIR /sample_app
RUN pip install -r requirements.txt --no-cache-dir --compile

#RUN tests
WORKDIR /sample_app/tests
RUN pytest --junitxml=coverage2_junit.xml &&\
    pytest --cov=../src --cov-report xml

WORKDIR /sample_app
CMD ["bash"]