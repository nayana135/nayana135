# This references the default Python container from
# the Docker Hub with the 2.7 tag:
# https://registry.hub.docker.com/_/python/
# If you want to use a slim Python container with
# version 3.4.3 you would use: python:3.4-slim
# If you want Google's container you would reference google/python
# Read more about containers on our dev center
# https://devcenter.wercker.com/overview-and-core-concepts/containers/
box: python:2.7
# You can also use services such as databases. Read more on our dev center:
# https://devcenter.wercker.com/administration/services/
# services:
    # - postgres
    # https://devcenter.wercker.com/administration/services/examples/postgresql/

    # - mongo
    # https://devcenter.wercker.com/administration/services/examples/mongodb/

# This is the build pipeline. Pipelines are the core of wercker
# Read more about pipelines on our dev center
# https://devcenter.wercker.com/development/pipelines/
build:
  # The steps that will be executed on build
  # Steps make up the actions in your pipeline
  # Read more about steps on our dev center:
  # https://devcenter.wercker.com/development/steps/
  steps:
    # A step that sets up the python virtual environment
    - virtualenv:
        name: setup virtual environment
        install_wheel: false # Enable wheel to speed up builds (experimental)

    # # Use this virtualenv step for python 3.2
    # - virtualenv
    #     name: setup virtual environment
    #     python_location: /usr/bin/python3.2

    # A step that executes `pip install` command.
    - pip-install

    # # This pip-install clears the local wheel cache
    # - pip-install:
    #     clean_wheel_dir: true

    # A custom script step, name value is used in the UI
    # and the code value contains the command that get executed
    - script:
        name: echo python information
        code: |
          echo "python version $(python --version) running"
          echo "pip version $(pip --version) running"
