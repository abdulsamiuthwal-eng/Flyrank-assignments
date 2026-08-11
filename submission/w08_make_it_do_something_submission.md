# Week 08 Deliverable: Make It Do Something

**Track:** General AI Fluency  
**Student:** Abdul Sami Uthwal  
**Selected Feature:** End-to-End Live Contact & Lead Capture System (Exactly 1 Feature)  
**Live Site URL:** https://abdulsamiuthwal-portfolio.vercel.app/#contact-page  
**Free Tier Backend Provider:** Web3Forms API  
**Verified Recipient Inbox:** abdulsamiuthwal@gmail.com  

---

## 1. Live Feature & Evidence of Functionality

- **The Selected Feature:** A fully wired, real-time Lead Capture & Contact System built directly into the portfolio.
- **Free Tier Setup:** Uses Web3Forms serverless form API (zero-cost, no cold starts, 250 submissions/month free tier).
- **Evidence of Real Test Submission:** A live test submission was executed on the production URL `https://abdulsamiuthwal-portfolio.vercel.app/#contact-page` with data (`Test User`, `test@example.com`, `Hello world test`). The backend processed the request, and the formatted lead email arrived instantly in `abdulsamiuthwal@gmail.com` at 10:30 PM PKT (see attached screenshot proof).

---

## 2. Plain-Words Explainer

### A. What is a Backend?
In web engineering, a **frontend** is the user interface rendered inside the browser (HTML structure, CSS design, text inputs, buttons). A **backend** is the server-side infrastructure running in the background that executes logic, verifies security, manages databases, and communicates with external services like email servers. 

Without a backend, a contact form is just a visual mock-up—clicking "Submit" has nowhere to send the data. The backend serves as the pipeline that turns user actions into real-world results.

### B. What My Feature Does
My portfolio features a single, fully wired **Lead Capture Engine**. When a hiring manager, client, or recruiter visits my portfolio and fills out the contact form, the feature receives their details (Name, Email, Organization, Project Goals). Instead of triggering a dummy alert or relying on broken `mailto:` links, it transmits the inquiry to a serverless backend API, which immediately delivers a structured email notification to my personal Gmail inbox so I can respond directly.

### C. How the Data Flows (Step-by-Step)
1. **User Action (Frontend):** The visitor fills in the input fields on `https://abdulsamiuthwal-portfolio.vercel.app/#contact-page` and clicks "Send Message / Get Estimate".
2. **Client Dispatch (HTTP Request):** JavaScript intercepts the submit event, gathers the field values into a structured JSON payload alongside an API access key, and sends an asynchronous HTTP `POST` request to `https://api.web3forms.com/submit`.
3. **Backend Processing (Web3Forms API):** Web3Forms acts as the serverless backend. It validates the access key, checks for spam signatures, packages the JSON fields into an HTML email template, and sends it out via SMTP.
4. **Final Inbox Delivery (Output):** The formatted lead lands in my Gmail inbox (`abdulsamiuthwal@gmail.com`) within seconds, with the `Reply-To` header set to the visitor's email address for direct follow-up.
