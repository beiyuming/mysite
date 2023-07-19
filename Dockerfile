FROM python:3.6
RUN pip install fastapi -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install uvicorn[standard] -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY main.py /
COPY tools.py /
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000