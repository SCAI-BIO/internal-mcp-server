# Internal MCP Server

- [Internal MCP Server](#internal-mcp-server)
  - [Configuration](#configuration)
  - [Execution Methods](#execution-methods)
    - [1. Via `uv run`](#1-via-uv-run)
    - [2. Docker](#2-docker)
      - [Build the image](#build-the-image)
      - [Run the container](#run-the-container)

This Model Context Protocol (MCP) server integrates an internal API using its OpenAPI specification.

## Configuration

The server relies on environment variables for its configuration. A template is provided in the repository.

Create a local `.env` file by copyting the example:

```bash
cp .env.example .env
```

The file requires the following variables:

- `NAME`: The display name of the MCP Server.
- `BASE_URL`: The root URL of the target OpenAPI server.
- `ROUTE_MAPS_JSON`: A strict, single-line JSON array defining the include/exclude rules for the OpenAPI endpoints.

**Note for Windows Users:** > Environment variable parsing behavior differs on Windows between `uv` and Docker. Docker reads `.env` variables literally, while `uv` may require complex strings to be wrapped in quotes. If you encounter a `JSONDecodeError` locally, you may need to add or remove single quotes (`'`) around the `ROUTE_MAPS_JSON` value depending on whether you are running the server via `uv` or Docker.

## Execution Methods

### 1. Via `uv run`

Using `uv` allows you to execute the server with ephemeral dependencies, bypassing the need for manual virtual environment management. The `--env-file` flag ensures the environment variables are loaded prior to execution.

```bash
uv run --env-file .env fastmcp run src/internal_mcp_server/server.py --host 127.0.0.1 --port 8000 --transport http
```

### 2. Docker

To run the server using Docker, build the image and start the container. The container uses HTTP transport by default.

#### Build the image

```bash
docker build -t internal-mcp-server .
```

#### Run the container

Pass the configuration to the container using `--env-file` flag.

```bash
docker run --rm -p 80:80 --env-file .env internal-mcp-server
```
