#!/usr/bin/env python3
"""Local Test Suite for DocuParser Document & Invoice API"""
from server import extract_invoice_fields, audit_document_pii

SAMPLE_INVOICE = """
Acme Cloud Services Inc.
100 Tech Boulevard, Suite 400
San Francisco, CA 94107

INVOICE #INV-2026-9812
Issue Date: 2026-09-15
Due Date: 2026-10-15

Bill To:
Wayne Enterprises
1007 Mountain Drive

Description                     Qty    Unit Price    Total
Cloud Virtual Server Hosting     2      $150.00       $300.00
Enterprise SLA Support Package   1      $250.00       $250.00

Subtotal: $550.00
Tax (8.5%): $46.75
Total: $596.75
"""

def test_invoice_extraction():
    res = extract_invoice_fields(SAMPLE_INVOICE)
    assert res["success"] is True
    assert res["invoice_number"] == "INV-2026-9812"
    assert res["financials"]["total"] == 596.75
    assert res["financials"]["subtotal"] == 550.00
    assert res["line_items_count"] == 2
    print(f" [PASS] Invoice Extraction: #{res['invoice_number']} Total: ${res['financials']['total']} ({res['line_items_count']} items) in {res['processing_time_ms']}ms")

def test_pii_audit():
    sample_text = "Please reach out to support@acme.com or call +1 (415) 555-0199 if you have any billing questions."
    res = audit_document_pii(sample_text)
    assert res["success"] is True
    assert res["pii_detected"] is True
    assert "support@acme.com" in res["extracted_emails"]
    print(f" [PASS] PII Extraction: Found {res['summary']['emails_count']} emails, {res['summary']['phone_numbers_count']} phones")

if __name__ == "__main__":
    print("Running DocuParser API Test Suite...")
    test_invoice_extraction()
    test_pii_audit()
    print("All DocuParser tests passed 100%!")
