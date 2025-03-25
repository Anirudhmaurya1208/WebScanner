

# import requests
# import socket
# import whois
# import ssl
# import datetime
# import OpenSSL
# from django.shortcuts import render
# from django.http import JsonResponse

# # Google Safe Browsing API Key (Replace with your actual key)
# GOOGLE_API_KEY = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"

# def get_ip_address(url):
#     """Get the IP address of the URL's domain"""
#     try:
#         domain = url.replace("http://", "").replace("https://", "").split("/")[0]
#         return socket.gethostbyname(domain)
#     except Exception:
#         return "Not Found"

# def check_ssl_status(url):
#     """Improved SSL verification with issuer details"""
#     try:
#         domain = url.replace("http://", "").replace("https://", "").split("/")[0]
#         context = ssl.create_default_context()
#         with socket.create_connection((domain, 443)) as sock:
#             with context.wrap_socket(sock, server_hostname=domain) as ssock:
#                 cert = ssock.getpeercert()
#                 x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert)
#                 issuer = x509.get_issuer().CN  # Certificate Authority (CA)
#                 expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")
#                 return {
#                     "status": "Valid" if expiry_date > datetime.datetime.utcnow() else "Expired",
#                     "issuer": issuer
#                 }
#     except Exception:
#         return {"status": "No SSL", "issuer": "Unknown"}

# def get_domain_info(url):
#     """Fetch WHOIS data for the domain"""
#     try:
#         domain = url.replace("http://", "").replace("https://", "").split("/")[0]
#         whois_info = whois.whois(domain)
#         return {
#             "Registrar": whois_info.registrar or "Unknown",
#             "Country": whois_info.country or "Unknown",
#             "Creation Date": whois_info.creation_date or "Unknown"
#         }
#     except Exception:
#         return {"Registrar": "Unknown", "Country": "Unknown", "Creation Date": "Unknown"}

# def check_google_safe_browsing(url):
#     """Check Google Safe Browsing API for phishing/malware detection"""
#     payload = {
#         "client": {"clientId": "cyber-url-scanner", "clientVersion": "1.0"},
#         "threatInfo": {
#             "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
#             "platformTypes": ["ANY_PLATFORM"],
#             "threatEntryTypes": ["URL"],
#             "threatEntries": [{"url": url}]
#         }
#     }
#     response = requests.post(
#         f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}",
#         json=payload
#     )
#     data = response.json()
#     return "Safe" if not data.get("matches") else "Dangerous"

# def calculate_risk_score(domain_info, ssl_status, blacklist_status):
#     """Calculate a risk score for the URL"""
#     score = 0

#     # Domain age check (New domains = High risk)
#     try:
#         creation_date = domain_info.get("Creation Date", "Unknown")
#         if creation_date != "Unknown":
#             age_days = (datetime.datetime.utcnow() - creation_date[0]).days
#             if age_days < 180:
#                 score += 40  # High risk for newly registered domains
#             elif age_days < 365:
#                 score += 20
#     except:
#         pass

#     # SSL check (No SSL / Expired = Higher risk)
#     if ssl_status["status"] == "No SSL":
#         score += 30
#     elif ssl_status["status"] == "Expired":
#         score += 20

#     # Blacklist check (Google Safe Browsing API)
#     if blacklist_status == "Dangerous":
#         score += 50  # Very high risk if blacklisted

#     # Final risk classification
#     if score >= 70:
#         return "🔴 High Risk (Unsafe)"
#     elif score >= 40:
#         return "🟠 Medium Risk (Use Caution)"
#     else:
#         return "🟢 Low Risk (Safe)"

# def scan_url(request):
#     """Scan the URL and display results on the same page"""
#     if request.method == "POST":
#         url = request.POST.get("url")

#         # Check if URL is blacklisted
#         blacklist_status = check_google_safe_browsing(url)

#         # Get additional details
#         ip_address = get_ip_address(url)
#         ssl_status = check_ssl_status(url)
#         domain_info = get_domain_info(url)

#         # Calculate risk score
#         risk_status = calculate_risk_score(domain_info, ssl_status, blacklist_status)

#         result = {
#             "url": url,
#             "status": risk_status,
#             "details": "This URL is flagged as unsafe by Google Safe Browsing API." if blacklist_status == "Dangerous" else "No known threats detected.",
#             "ip": ip_address,
#             "ssl_status": ssl_status,
#             "domain_info": domain_info
#         }

#         return render(request, "scanner/index.html", {"result": result})

#     return render(request, "scanner/index.html")


from django.shortcuts import render
from django.http import JsonResponse
import requests
import socket
import whois
import ssl
import datetime

def get_ip_address(url):
    """Get the IP address of the URL's domain"""
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        return socket.gethostbyname(domain)
    except Exception:
        return "Not Found"

def check_ssl_status(url):
    """Check if the SSL certificate is valid"""
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")
                return "Valid" if expiry_date > datetime.datetime.utcnow() else "Expired"
    except Exception:
        return "No SSL"

def get_domain_info(url):
    """Fetch WHOIS data for the domain"""
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        whois_info = whois.whois(domain)
        return {
            "Registrar": whois_info.registrar or "Unknown",
            "Country": whois_info.country or "Unknown",
            "Creation_Date": whois_info.creation_date or "Unknown"
        }
    except Exception:
        return {"Registrar": "Unknown", "Country": "Unknown", "Creation_Date": "Unknown"}

def scan_url(request):
    if request.method == "POST":
        url = request.POST.get("url")

        # Fake threat intelligence system (replace with real API)
        response = {"status": "Suspicious", "details": "This URL has been reported for phishing activity."}

        ip_address = get_ip_address(url)
        ssl_status = check_ssl_status(url)
        domain_info = get_domain_info(url)

        result = {
            "url": url,
            "status": response["status"],
            "details": response["details"],
            "ip": ip_address,
            "ssl_status": ssl_status,
            "domain_info": domain_info
        }

        return render(request, "scanner/index.html", {"result": result})  # Pass result to template

    return render(request, "scanner/index.html")


# from django.shortcuts import render
# from django.http import JsonResponse

# def scan_url(request):
#     """Simulated URL Scan with Static Data"""
#     if request.method == "POST":
#         url = request.POST.get("url")

#         # Sample scan result (Static Data for Now)
#         sample_result = {
#             "url": url,
#             "status": "Suspicious",  # You can change this to "Safe" or "Malicious"
#             "details": "This URL has been reported for phishing activity.",
#             "ip": "142.250.183.78",
#             "ssl_status": "Valid (Issuer: Let's Encrypt)",  # Static SSL data
#             "domain_info": {
#                 "Registrar": "MarkMonitor, Inc.",
#                 "Country": "US",
#                 "Creation Date": "2005-02-15 05:13:12",
#             },
#         }

#         return render(request, "scanner/index.html", {"result": sample_result})
    
#     return render(request, "scanner/index.html")
