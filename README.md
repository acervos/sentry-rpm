Sentry RPM
=============================

This project is for creating a static RPM with Sentry and it's dependencies included, as well as SystemD service file.  The current packaging in this repo is for Centos7 using SystemD, this is readily available distribution that is available on all cloud platforms.  Python 2.7 is required for Sentry, hence the decision for this version.

### Included files

This is meant as a library dependency in the sense that configuration files will not be included, these will need to be added in another step.  This RPM can be required as a part of another SPEC file in the event you are installing additional packages.  

- A supervisor conf is included to start up all the sentry services
- A sentry service file is included to start supervisor on boot

### Building the Docker image
Building the dependencies will be achieved by building or downloading the Docker image.  If you rely on a private registry, it is important to pass the Docker image name as an argument.

To build the Docker image and push to a custom registry

```sh
make docker-private DOCKER_IMAGE=docker_image_name
```
To simply build the image

```sh
make docker
# with custom image name
make docker DOCKER_IMAGE=docker_image_name
```

### Building the Dependencies

In order to build the RPM, there are 2 phases, compiling the dependencies and creating the RPM.  Both of these occur inside a Docker container to allow any system to build the RPM, the most likely system to build on is a Jenkins or CI server.

Normally, you will build the complete RPM, to build just the deps for testing, you can use the following

```sh
make deps
# with custom image name
make deps DOCKER_IMAGE=docker_image_name
```

### Building the RPM

```sh
make build
# with custom image name
make build DOCKER_IMAGE=docker_image_name
```
