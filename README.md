# Django GreatReads
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) ![GitHub issues](https://img.shields.io/github/issues/Dev-Mehta/dj-greatreads) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Dev-Mehta/dj-greatreads) ![GitHub](https://img.shields.io/github/license/Dev-Mehta/dj-greatreads) ![GitHub Repo stars](https://img.shields.io/github/stars/Dev-Mehta/dj-greatreads?style=social) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Dev-Mehta/dj-greatreads)

 I am creating an app where you can read latest blogposts from various python and django related blog sources, to filter out only GOOD web content to read

## How to run

Make sure you have docker installed.

1. Clone the repo
```
$ git clone https://github.com/Dev-Mehta/dj-greatreads
```

2. Build image and run with docker container

```
$ docker compose up --build
```

> Avoid --build if you have already built it once, and there are no changes made to the source code.

3. To stop the container
```
$ docker compose down
```
### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
