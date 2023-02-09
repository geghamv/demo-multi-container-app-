from python:3.8

copy . root/cal_app
# ENV FLASK_APP=app.py
workdir /root/cal_app
copy ./requirements.txt ./
ENV test="test"
run pip install -r requirements.txt
run pip install requests
expose 5080
entrypoint ["flask", "run", "--host=0.0.0.0", "--port=8080"]
# cmd ["python3.8","app.py"]