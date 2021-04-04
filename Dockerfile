FROM python:3-slim

# Adding all necessary files to our image
COPY testbuzz.py /
COPY fizzbuzz.py /
COPY sleepbuzz.sh /

# Will run unit tests before image build is complete
RUN python testbuzz.py

# And will run the fizzbuzz and sleep script when container is started
CMD ["bash", "./sleepbuzz.sh"]

# Honestly, I'm not sure how to reduce the resulting image size through a 
# multi-stage build given the technology I've chosen. I still need access 
# to bash as well as the python interpreter.
