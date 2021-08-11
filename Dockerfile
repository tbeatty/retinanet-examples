FROM nvcr.io/nvidia/pytorch:21.07-py3

COPY . odtk/
RUN pip install --no-cache-dir -e odtk/
