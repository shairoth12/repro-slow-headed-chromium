FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

ARG USER_NAME="pwuser"
ARG GROUP_NAME="pwuser"

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y python3-pip git-lfs sudo x11-utils
RUN git lfs install

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN playwright install

RUN echo ${USER_NAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}
