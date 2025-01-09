# Use the official Python image as a base image
FROM python:3.12
# Copy application code to the container
COPY . /app
# Set the working directory inside the container
WORKDIR /app
# Install required Python packages
RUN pip install -r requirements.txt
# Expose the port 9500
EXPOSE 9500
CMD ["python", "main.py"]


####################
#"""
#FROM python:3.10 — This instruction specifies that container will use the Python Docker container as a base. 
#The text after ":" specifies the tag, which defines the specific version of the base container that you want to use.
#
#COPY . /app — When you build the container, the content of the current folder (".") will be copied to the /app folder in the container.

#WORKDIR /app — This instruction specifies that the command that follows it will be executed from this folder.

#RUN pip install -r requirements.txt — The RUN instruction specifies the commands that will be executed when building the container. 
#This particular instruction will install required Python packages to the container.

#EXPOSE 5000 — This instruction specifies that the container will listen on the TCP port 5000 at run time.

#CMD ["python3", "main.py"]—This instruction specifies the commands that will be executed when you start the container.
#"""
####################