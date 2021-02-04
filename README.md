## Exercise 1

build

`$ docker build -t blue-apron-hw .`

run

`$ docker container run -p 443:443 blue-apron-hw`

test

```
$ curl -k https://localhost
$ curl -k --user-agent "h4ck3r" https://localhost
```

## Exercise 2

Dependencies:

* python3
* pip3
* requests

run

```
$ cd exercise-2
$ python3 ex2.py
```

## Exercise 3

1. I would add a Makefile to automate building, tagging and pushing application images to repositories.
2. Depending on which CI/CD is used in the organization, I would generate a pipeline/workflow to handle running of tests, deploys to environments, messaging of success/failures.

