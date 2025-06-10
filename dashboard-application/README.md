## Running with Docker

You can run this project locally using Docker Compose, which sets up all required services:

- **Next.js frontend** (Node.js v22.13.1)
- **Python FastAPI backend** (Python 3.11)
- **MongoDB** (latest)

### Build and Start All Services

From the project root, run:

```bash
docker compose up --build
```

This will build and start the following containers:

- **typescript-app** (Next.js frontend) — available at [http://localhost:3000](http://localhost:3000)
- **python-backend** (FastAPI backend) — available at [http://localhost:8000](http://localhost:8000)
- **mongo** (MongoDB database) — available at `localhost:27017`

### Ports

- **Frontend (Next.js):** `3000` (exposed to host)
- **Backend (FastAPI):** `8000` (internal, accessible to frontend)
- **MongoDB:** `27017` (exposed to host for development)

### Environment Variables

- No required environment variables are set by default. If you need to provide environment variables, uncomment the `env_file` lines in the `docker-compose.yml` and provide the appropriate `.env` files for each service.

### Notes

- The backend and frontend containers run as non-root users for improved security.
- MongoDB data is not persisted by default. To persist data, uncomment the `volumes` section for `mongo` in `docker-compose.yml`.
- The backend automatically installs dependencies (FastAPI, Strawberry GraphQL, Pydantic, PyMongo) in a Python virtual environment.
- The frontend uses production-optimized Node.js builds and only exposes the necessary files.

For development, you can continue to use the local Next.js dev server as described above, or use Docker Compose for a production-like environment.