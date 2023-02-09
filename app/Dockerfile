from python:3.8

copy . /root/app
# ENV FLASK_APP=app.py
workdir /root/app
copy ./requirements.txt ./
ENV test="test"
run pip install -r requirements.txt
expose 5000
entrypoint ["flask", "run", "--host=0.0.0.0", "--port=8000"]
# cmd ["python3.8","app.py"]