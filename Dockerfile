FROM astral/uv:python3.14-trixie

WORKDIR /internal_mcp_server

COPY . /internal_mcp_server/

RUN uv sync --no-dev --no-cache

EXPOSE 80

# API entry point
CMD ["uv", "run", "fastmcp", "run", "src/internal_mcp_server/server.py", "--host", "0.0.0.0", "--port", "80", "--transport", "http"]