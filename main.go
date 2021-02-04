package main

import (
	"encoding/json"
	"log"
	"net/http"
	"time"
)

type message struct {
	Greeting string `json:"greeting"`
	Date     string `json:"date"`
}

func getMessage() *message {
	now := time.Now()
	m := message{Greeting: "Hello World"}
	m.Date = now.String()
	return &m
}

func handler(w http.ResponseWriter, r *http.Request) {
	if r.UserAgent() == "h4ck3r" {
		w.Write([]byte("HTTP 403 Forbidden"))
	} else {
		w.Header().Set("Content-Type", "application/json")
		m := getMessage()
		json.NewEncoder(w).Encode(m.Greeting + " " + m.Date)
	}
}

func main() {
	http.HandleFunc("/", handler)
	// http.ListenAndServe(":8080", nil)
	err := http.ListenAndServeTLS(":443", "/bin/server.crt", "/bin/server.key", nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}
