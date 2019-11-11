#
#                        BUILD TEMPORARY BUILD-SYSTEM
#
# Downloads all the pip with the given ssh key. Allows to use private repos
#  without the key
#
FROM microdisseny/py3-development:ubuntu-18.04 as build-system

# Make sure your domain is accepted
RUN mkdir /root/.ssh/
RUN \
  touch ~/.ssh/known_hosts && \
  ssh-keyscan github.com >> ~/.ssh/known_hosts && \
  ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts

ADD ./requirements.txt /tmp/

# Download python requirements
ARG EXTRA_REQUIREMENTS=devel
ENV EXTRA_REQUIREMENTS $EXTRA_REQUIREMENTS

RUN \
  pip3 install --upgrade pip; \
  mkdir /pip; \
  pip3 download -d /pip -r /tmp/requirements.txt && \
  pip3 download -d /pip uwsgi; \
  if [ -n "$EXTRA_REQUIREMENTS" -a -f "/docker/requirements-$EXTRA_REQUIREMENTS.txt" ]; \
    then pip3 download -d /pip -r "/docker/requirements-$EXTRA_REQUIREMENTS.txt"; \
  fi;

#
#                            BUILD RUNTIME SYSTEM
#
# The actuall system that will be run
#
FROM microdisseny/py3-development:ubuntu-18.04

# Copy files
RUN mkdir -p /app
RUN mkdir -p /docker
ADD docker/django/entrypoint.sh /docker/
ADD docker/django/bash.sh /docker/
RUN chmod +x /docker/*.sh

# Install python requirements
COPY --from=build-system /pip /pip
RUN pip3 install --upgrade pip
RUN pip3 install /pip/*
RUN rm -rf /pip

# Configure run
WORKDIR /app
ENTRYPOINT ["/docker/entrypoint.sh"]
