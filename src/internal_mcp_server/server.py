import httpx
from fastmcp import FastMCP
from fastmcp.server.providers.openapi import MCPType, RouteMap

BASE_URL = "https://api.kitsune.scai.fraunhofer.de"

client = httpx.AsyncClient(base_url=BASE_URL)
openapi_spec = httpx.get(BASE_URL + "/openapi.json").json()
route_maps = [
    RouteMap(methods=["GET"], mcp_type=MCPType.TOOL),
    RouteMap(methods=["DELETE", "PATCH"], mcp_type=MCPType.EXCLUDE),
    RouteMap(tags={"imports"}, mcp_type=MCPType.EXCLUDE),
    RouteMap(methods=["POST"], pattern=r"^/terminologies/", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods=["POST"], pattern=r"^/concepts/", mcp_type=MCPType.EXCLUDE),
    RouteMap(methods=["POST"], pattern=r"^/mappings/", mcp_type=MCPType.EXCLUDE),
]

mcp = FastMCP.from_openapi(openapi_spec=openapi_spec, client=client, route_maps=route_maps, name="Kitsune MCP Server")
