# DocuParser Document & Financial Invoice API

> **High-precision key-value financial extraction for invoices, receipts & document PII detection.**  
> Built by the API Operations Team under Liam Vance & Ethan Sterling.

---

## 🚀 RapidAPI Monetization Tiers

| Plan | Price | Monthly Quota | Features |
|---|---|---|---|
| **BASIC** | **$0.00 / month** | 100 calls / mo | Core invoice extraction, rate-limited |
| **PRO** | **$35.00 / month** | 5,000 calls / mo | Line items table extraction & PII audit |
| **ULTRA** | **$85.00 / month** | 20,000 calls / mo | High confidence multi-currency financial parser |
| **MEGA** | **$185.00 / month** | 75,000 calls / mo | Unlimited high-throughput enterprise batch queue |

---

## 📡 Live Endpoints

- `GET /health`: Health and operational latency.
- `POST /v1/invoice/extract`: Structured invoice extraction (vendor, dates, subtotal, tax, total, line items).
- `POST /v1/pii`: Document sensitive information & contact extraction.
