# Week 09 Deliverable: Plant Your Flag — Domain, Analytics & Graduate Badge

**Track:** General AI Fluency  
**Student:** Abdul Sami Uthwal  
**Live Production URL:** `https://abdulsamiuthwal-portfolio.vercel.app/`  
**Submission Date:** 2026-08-12  

---

## 1. Executive Summary & Launch Verification

> *"A custom domain turns 'a project' into a permanent part of your online identity, and analytics turns 'I hope people visit' into knowing they do."*

This deliverable confirms the public, production launch of Abdul Sami Uthwal's FlyRank AI Portfolio over HTTPS, complete with real-time web analytics, launch hygiene verification (Favicon, OpenGraph, Twitter Cards), and the FlyRank Verified Graduate Badge embedded in the website footer.

---

## 2. Launch Hygiene & Deployment Audit

| Requirement | Implementation Detail | Status / Evidence |
|---|---|---|
| **1. Live Domain & HTTPS** | Hosted on Vercel Edge Network (`https://abdulsamiuthwal-portfolio.vercel.app/`) with automatic SSL/TLS certificate | ✅ **PASS (100% Live)** |
| **2. Free Analytics** | Vercel Insights & Speed Analytics script (`/_vercel/insights/script.js`) injected into `<head>` | ✅ **PASS (Active Tracking)** |
| **3. Favicon & Branding** | Custom SVG Lightning Badge Favicon (`data:image/svg+xml...`) | ✅ **PASS (Browser Verified)** |
| **4. OpenGraph Social Card** | `og:title`, `og:description`, `og:image` (`sitemap_sketch.png`), `og:url` | ✅ **PASS (WhatsApp/LinkedIn Verified)** |
| **5. Twitter Summary Card** | `twitter:card` set to `summary_large_image` | ✅ **PASS (Twitter Verified)** |
| **6. Graduate Badge** | Embedded FlyRank Verified Graduate Badge in footer linking to `https://internship.flyrank.ai` | ✅ **PASS (Footer Live)** |

---

## 3. FlyRank Graduate Badge Verification

The footer of `https://abdulsamiuthwal-portfolio.vercel.app/` now features the official FlyRank Graduate Badge:

```html
<!-- FlyRank Graduate Verification Badge -->
<div class="flyrank-badge-wrapper">
    <a href="https://internship.flyrank.ai" target="_blank" rel="noopener" class="flyrank-badge" title="Verify FlyRank Graduate Credential">
        <span class="badge-icon">⚡</span>
        <div class="badge-text">
            <span class="badge-title">FlyRank Verified Graduate</span>
            <span class="badge-subtitle">General AI Fluency & ML Track • 2026</span>
        </div>
        <span class="badge-check">✓</span>
    </a>
</div>
```

---

## 4. Evaluation Criteria Pass/Revise Self-Check

- [x] **Live custom domain / clean fallback over HTTPS:** `https://abdulsamiuthwal-portfolio.vercel.app/`
- [x] **Analytics installed and working:** Vercel Web Analytics tracking script active in `<head>`
- [x] **Share preview, favicon, and titles correct:** OpenGraph cards, Twitter preview, SVG favicon, and page title verified
- [x] **Graduate badge installed in footer:** Badge linking to `https://internship.flyrank.ai` visible in footer
