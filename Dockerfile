FROM centos:centos7
LABEL REPO=git@github.com:acervos/sentry-rpm.git
MAINTAINER David Blooman <david.blooman@gmail.com>

RUN yum install epel-release -y
RUN yum update -y
RUN yum install -y wget python-setuptools python-pip python-devel \
                   libxslt-devel libxml2-devel zlib-devel libffi-devel \
                   openssl-devel libpqxx-devel libyaml-devel gcc \
                   postgresql-devel python-virtualenv rpm-build

RUN useradd -m -u 250 jenkins

RUN mkdir -p /www/sentry/
RUN chown -R jenkins:jenkins /www/sentry/

USER jenkins
