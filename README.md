# Kanvas MCP Server

## Building and Running the container

### Build

```sh
docker build -t kanvas/mcp:dev -f Dockerfile .
```

### Run

```sh
docker run -p 8888:8888 kanvas/mcp:dev
```

The server will be running with the command:

```sh
python server.py
```


# Todo

Document the whole service(client,server,api)

kanvas create events, see events, set reminders, list reminders