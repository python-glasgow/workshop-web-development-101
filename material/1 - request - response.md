# Request, Response

In these examples we will be going over a simple HTTP/1.1 get request flow.

Here's an example of a simple get request:

```http request
GET / HTTP/1.1
Host: www.google.com
User-Agent: IntelliJ HTTP Client/PyCharm 2024.3.3
Accept-Encoding: br, deflate, gzip, x-gzip
Accept: */*
```

Here's the response from that:

```http request
HTTP/1.1 200 OK
Date: Day, DD MMM YYYY HH:MM:SS GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-REtD9UuEzryo0Ep75Cd7Og' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Content-Encoding: gzip
Server: gws
Content-Length: 7126
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: *****; expires=Day, DD-MMM-YYY HH:MM:SS GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax

<!doctype html>
<html itemscope="" itemtype="http://schema.org/WebPage" lang="en-GB">
...
</html>
```

All HTTP frameworks are built around parsing and working with this method 
of communication. It can look rather complex at first but when you realise 
that the communication between the browser and the server is based on 
headers and a content body it becomes easier to reason about.

Here's an example of what a JSON request and response looks like:

Request:

```http request
GET /fact?max_length=140 HTTP/1.1
Host: catfact.ninja
```

Response:

```http request
HTTP/1.1 200 OK
Date: Day, DD MMM YYYY HH:MM:SS GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
Cache-Control: no-cache, private
x-ratelimit-limit: 100
x-ratelimit-remaining: 82
access-control-allow-origin: *
Set-Cookie: XSRF-TOKEN=*****; expires=Day, DD-MMM-YYY HH:MM:SS GMT; Max-Age=7200; path=/; secure; samesite=lax
Set-Cookie: catfacts_session=*****; expires=Day, DD-MMM-YYY HH:MM:SS GMT; Max-Age=7200; path=/; secure; httponly; samesite=lax
Set-Cookie: *****; expires=Day, DD-MMM-YYY HH:MM:SS GMT; Max-Age=7200; path=/;secure; httponly; samesite=lax
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
cf-cache-status: DYNAMIC
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v4?s=*****"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 91dcba0e198c93ff-LHR
Content-Encoding: br
alt-svc: h3=":443"; ma=86400
server-timing: cfL4;desc="?proto=TCP&rtt=12943&min_rtt=10930&rtt_var=6011&sent=5&recv=7&lost=0&retrans=0&sent_bytes=3100&recv_bytes=709&delivery_rate=239341&cwnd=226&unsent_bytes=0&cid=cd90eba9eef11b6f&ts=174&x=0"

{
  "fact": "On average, cats spend 2\/3 of every day sleeping. That means a nine-year-old cat has been awake for only three years of its life.",
  "length": 129
}
```

As you can see, there's a lot more headers in this response. Don't worry 
about headers for now, the web framework will take care of generating these.

_If you feel adventurous, a detail explanation of HTTP can be found here:
[https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)_
