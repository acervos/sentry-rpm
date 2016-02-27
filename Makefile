DOCKER_IMAGE?="davey/sentry-builder"

DEFAULT: build

docker:
	docker pull centos:centos7
	docker build -t $(DOCKER_IMAGE) .

docker-private:
	docker pull centos:centos7
	docker build -t $(DOCKER_IMAGE) .
	docker push $(DOCKER_IMAGE)

deps:
	docker pull $(DOCKER_IMAGE)
	mkdir -p src/www/sentry
	docker run -v $(shell pwd)/src:/app --rm=true sentry-ubuntu sh -c "virtualenv /www/sentry --no-site-packages && source /www/sentry/bin/activate && pip install sentry supervisor https://github.com/getsentry/sentry-auth-github/archive/master.zip https://github.com/getsentry/sentry-slack/archive/master.zip && cp -r /www/sentry/* /app/"

source:
	chmod -R -x+X $(shell pwd)/src/
	tar --exclude ".svn" --exclude ".*.sw?" --exclude "*.py[co]" -czf SOURCES/sentry.tar.gz src/

build: deps source
