FROM golang:1.15.7-alpine AS build

WORKDIR /go/src/app
ENV CGO_ENABLED=0 GOOS=linux GOARCH=amd64

COPY . ./

RUN go build -o /bin/app

FROM scratch
COPY --from=build /bin/app /bin/app
COPY --from=build /go/src/app/server.crt /bin
COPY --from=build /go/src/app/server.key /bin

EXPOSE 8080

ENTRYPOINT [ "/bin/app" ]
