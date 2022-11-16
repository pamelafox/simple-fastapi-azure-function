[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&repo=pamelafox%2Fsimple-flask-api-azure-function)

This repository includes a very simple Python Flask HTTP API, made for demonstration purposes only.

## Local development: FastAPI

1. Open this repository in Github Codespaces or VS Code with Remote Devcontainers extension.
2. Run API v1:

```console
python3 api/flask_app.py
```

3. Click 'http://127.0.0.1:5000' in the terminal, which should open the website in a new tab.
4. Append `/v1/generate_name` to the end of the URL.
5. Run API v2:

```console
python3 api/flask_app.py
```

6. Click 'http://127.0.0.1:8080' in the terminal.
7. Append `/v2/generate_name?starts_with=n` to the end of the URL.

## Local development: Azure Functions

Since this project is designed to be deployed to Azure Functions,
you can also use the local emulator from Azure Functions Core Tools
to test the function locally.

1. Open this repository in Github Codespaces or VS Code with Remote Devcontainers extension.
2. Run `func host start`
3. Click 'http://localhost:7071/{*route}' in the terminal, which should open the website in a new tab.
4. Change the URL to navigate to either the API at `/generate_name` or the docs at `/docs`.

## Deployment

Run `azd up`.

Navigate to the endpoint displayed in the terminal.

To try API v1, append `/generate_name` to the end of the URL.