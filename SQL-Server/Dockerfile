FROM debian

RUN apt update
RUN apt install -y sqlite3
RUN apt install -y python3

COPY source/Students.db /
COPY source/CHECK-Student.py /

EXPOSE 54321
CMD ["python3", "/CHECK-Student.py", "54321"]
