# Internal MCP Server

- [Internal MCP Server](#internal-mcp-server)
  - [Prerequisites](#prerequisites)
  - [Execution Methods](#execution-methods)
    - [1. Via `uv run`](#1-via-uv-run)
    - [2. Docker](#2-docker)
      - [Build the image](#build-the-image)
      - [Run the container](#run-the-container)

This Model Context Protocol (MCP) server integrates an internal API using its OpenAPI specification. It dynamically exposes `GET` routes as tools while explicitly excluding data modification endponts (`DELETE`, `PATCH`).

## Prerequisites

Save your server configuration code in a file named `server.py`. The application requires the `fastmcp` and `httpx` packages.

## Execution Methods

### 1. Via `uv run`

Using `uv` allows you to execute the server with ephemeral dependencies, bypassing the need for manual virtual environment management.

```bash
uv run fastmcp run src/internal_mcp_server/server.py --host 127.0.0.1 --port 8000 --transport http
```

### 2. Docker

To run the server using Docker, build the image and start the container. The container uses HTTP transport by default.

#### Build the image

```bash
docker build -t internal-mcp-server .
```

#### Run the container

```bash
docker run --rm -p 80:80 internal-mcp-server
```
