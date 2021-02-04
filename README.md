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

