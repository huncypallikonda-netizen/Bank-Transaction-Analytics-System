# BankSight — Bank Transaction Analytics System

A student project demonstrating a web dashboard for recording bank transactions, summarising activity, flagging selected high-value transactions, and displaying monthly charts.

## Team responsibilities

| Team member | Module | Main files |
|---|---|---|
| KOLLI ANILKUMAR | Frontend Development | `frontend/` — HTML, CSS, Bootstrap, login and dashboard |
| BONTHU DEVA KASI | Backend Development | `backend/` — Flask routes, authentication and API |
| TELUGU AKSHAY KUMAR | Data Analytics & Security | `analytics_security/` — Pandas analysis and rule-based alerts |
| CHINTHI KALYANI | Database Management | `database/` — MySQL schema, records and CRUD support |
| PALLIKONDA HUNCY ANGEL | Data Visualization & Reports | `visualization_reports/` — charts, monthly summary and CSV export |

## Requirements

- Python 3.10 or later
- MySQL Server 8 or later
- A modern browser

## Setup

1. Create a MySQL database and tables by running `database/schema.sql` in MySQL Workbench or the MySQL client.
2. Copy `.env.example` to `.env` in the project root and enter your local MySQL credentials. Set a unique `SECRET_KEY`.
3. Install dependencies:

   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

4. Create the demo user:

   ```bash
   python database/create_demo_user.py
   ```

5. Start the Flask API from the project root:

   ```bash
   python backend/app.py
   ```

6. Open `frontend/index.html` in a browser. If your browser blocks local-file API requests, serve the frontend folder with `python -m http.server 5500 --directory frontend` and open `http://127.0.0.1:5500`.

Demo login: `admin` / `admin123`.

## API endpoints

- `GET /api/health` — service health check
- `POST /api/login` — authenticate and receive a bearer token
- `GET /api/dashboard` — dashboard totals and recent transactions
- `GET /api/transactions` — list the signed-in user's transactions
- `POST /api/transactions` — add a transaction
- `GET /api/alerts` — list the signed-in user's alerts
- `GET /api/reports/monthly-chart` — monthly chart image

## Notes and limitations

- This is an educational prototype, not a real banking application. Do not connect real bank accounts or upload real customer information.
- The example uses simple, explainable amount-based screening rules. These are demonstrations, not a reliable fraud-detection system.
- Before any public deployment, replace the demo credentials, configure HTTPS, restrict CORS to your frontend domain, use a production-grade secret, add rate limiting/CSRF protections as appropriate, and review authentication/session design.
- The chart endpoint currently uses a query-string token for the image element because browsers cannot attach custom authorization headers to an ordinary image request. For a production system, use a safer cookie-based session or fetch the image as a blob with the authorization header.
- The website you selected on Lovable is a separate hosted frontend. This repository is the source-code project scaffold; it does not automatically download or mirror the Lovable project.

## GitHub upload

Create an empty GitHub repository, then run these commands from this folder:

```bash
git init
git add .
git commit -m "Add BankSight project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/BankSight.git
git push -u origin main
```
