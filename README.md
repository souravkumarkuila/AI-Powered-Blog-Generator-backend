
# AI-Powered-Blog-Generator-backend (FastAPI)

FastAPI backend that proxies requests to Azure OpenAI and stores drafts via SQLAlchemy.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env to set Azure OpenAI and DB settings

# Run
uvicorn app.main:app --reload --port 8000
```

## Environment variables

```
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com/
AZURE_OPENAI_API_KEY=***
AZURE_OPENAI_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_API_VERSION=2024-08-01-preview
DATABASE_URL=sqlite:///./local.db  # Or mysql+pymysql://user:pass@host:3306/dbname
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

## Endpoints
- `POST /api/generate` → `{ content: string }`
- `POST /api/drafts` → create draft
- `GET /api/drafts` → list drafts
- `GET /api/drafts/{id}` → get by id
- `PUT /api/drafts/{id}` → update
- `DELETE /api/drafts/{id}` → delete

## Notes
- Uses `AzureOpenAI` client from `openai` Python SDK. Deployment name goes into the `model` parameter.
- SQLAlchemy will auto-create tables on first run.
- Default DB is local SQLite; switch to MySQL by setting `DATABASE_URL`.
