import json
import os
from unittest.mock import MagicMock, patch

# Minimal OpenAPI specification to satisfy FastMCP validation
MOCK_OPENAPI_SPEC = {
    "openapi": "3.1.0",
    "info": {"title": "Test API", "version": "1.0.0"},
    "paths": {"/health": {"get": {"operationId": "get_health", "responses": {"200": {"description": "OK"}}}}},
}


def test_server_initialization():
    os.environ["NAME"] = "Dependabot Test Server"
    os.environ["BASE_URL"] = "https://mock.api.local"
    os.environ["ROUTE_MAPS_JSON"] = json.dumps([{"methods": ["GET"], "mcp_type": "TOOL"}])

    # Patch the httpx.get call to prevent real network requests
    with patch("httpx.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_OPENAPI_SPEC
        mock_get.return_value = mock_response

        # Import the server module (triggers the module-level execution)
        import internal_mcp_server.server as server

        # 4. Verify successful execution
        assert server.mcp.name == "Dependabot Test Server"
        assert server.client.base_url == "https://mock.api.local"
        mock_get.assert_called_once_with("https://mock.api.local/openapi.json")
