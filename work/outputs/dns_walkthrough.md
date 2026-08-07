# PF-04: Personal Website & Non-Technical DNS Walkthrough

**Live Portfolio URL:** `https://abdulsamiuthwal-portfolio.vercel.app/`  
**GitHub Repository:** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments`  
**Author:** Abdul Sami  
**Track:** General AI Fluency | **Module:** PF-04 Infrastructure & Hosting  

---

## 1. What is DNS? (The Internet's Phonebook)
Imagine the internet is a massive international telephone system. Computers do not understand human names like `abdulsamiuthwal-portfolio.vercel.app`; they communicate using numerical IP addresses like `76.76.21.21`.

**DNS (Domain Name System)** acts as the internet's automated phonebook. When someone types your domain name into a browser, DNS translates that human-friendly name into the exact computer IP address hosting your website.

---

## 2. What is a CNAME Record? (The Alias Pointer)
A **CNAME (Canonical Name) Record** is an alias rule in DNS. Instead of pointing a domain to a static numerical IP address (which an A record does), a CNAME record points one domain name to another domain name.

- **Example:** Pointing `abdulsamiuthwal.flyrank.ai` &rarr; `abdulsamiuthwal-portfolio.vercel.app`.
- **Why it matters:** Vercel/Netlify hosting servers dynamically change IP addresses behind the scenes to handle load balancing. By using a CNAME record, you don't need to update IP addresses manually; your domain automatically follows host updates.

---

## 3. What Happens When Someone Opens Your Website? (Step-by-Step Resolution Flow)

1. **User Request:** A user types `https://abdulsamiuthwal-portfolio.vercel.app/` in Chrome.
2. **Recursive Resolver Query:** The browser asks the Internet Service Provider's (ISP) DNS Resolver: *"Where is this site hosted?"*
3. **Nameserver Lookup:** 
   - Resolver asks the **Root Nameserver** (finds `.app` TLD).
   - Resolver asks the **TLD Nameserver** (finds `vercel.app` authoritative nameserver).
   - Resolver asks Vercel's **Authoritative Nameserver**, which replies: *"Serve content from cluster IP 76.76.21.21."*
4. **Response & SSL Handshake:** The resolver returns the IP to the browser. The browser connects over HTTPS, verifies the SSL certificate padlock, and renders the portfolio.

---

## 4. Capstone Subdomain Provisioning Checklist (`yourname.flyrank.ai`)

When FlyRank Ops grants `abdulsamiuthwal.flyrank.ai` at the end of the track:

1. **Ops Creation:** FlyRank Ops creates a DNS CNAME record mapping `abdulsamiuthwal.flyrank.ai` &rarr; `abdulsamiuthwal-portfolio.vercel.app`.
2. **Host Configuration:** Add `abdulsamiuthwal.flyrank.ai` under Vercel/Netlify **Custom Domains** settings.
3. **Propagation Verification:** Wait 2–5 minutes for global DNS propagation.
4. **Padlock Check:** Confirm HTTPS SSL padlock loads automatically on `https://abdulsamiuthwal.flyrank.ai`.
