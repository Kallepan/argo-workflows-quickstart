FROM --platform=linux/amd64 python:3.12

USER root

COPY . .

RUN apt update \
    && apt install -y build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

CMD ["python", "./dicom2nifti.py"]