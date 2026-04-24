import json
import os

import httpx
from fastmcp import FastMCP
from fastmcp.server.providers.openapi import MCPType, RouteMap

NAME = os.environ["NAME"]
BASE_URL = os.environ["BASE_URL"]
ROUTE_MAPS_JSON = os.environ["ROUTE_MAPS_JSON"]


raw_routes = json.loads(ROUTE_MAPS_JSON)
route_maps = []

for route in raw_routes:
    mcp_type_enum = getattr(MCPType, route.pop("mcp_type"))

    # Cast tags to a set to satisfy FastMCP's internal requirements
    if "tags" in route:
        route["tags"] = set(route["tags"])
    route_maps.append(RouteMap(**route, mcp_type=mcp_type_enum))


client = httpx.AsyncClient(base_url=BASE_URL)
openapi_spec = httpx.get(f"{BASE_URL}/openapi.json").json()

mcp = FastMCP.from_openapi(openapi_spec=openapi_spec, client=client, route_maps=route_maps, name=NAME)
