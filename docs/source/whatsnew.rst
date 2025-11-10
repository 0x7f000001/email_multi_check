.. _whatsnew:

What's New in email-multi-check
===============================

1.0.7 (in development)
----------------------
* Add docs

* Add Example ``test_api.py`` easy integration with FastAPI for REST API endpoints
  returning JSON responses.

1.0.6
-----
* Add Examle tools Command-line testing script ``test_dns_smtp.py``
  with customizable modes and ports.

* Minor bugs fixed

1.0.5
-----
* Web-based verification for configured domains,
  using external configuration files for URLs and request parameters.

*  Add requests file ``domain_requests`` and ``url.cfg``

1.0.4
-----
* SMTP verification using four methods MAIL FROM / RCPT TO.

* Add SMTP_SSL request.

1.0.3
-----
* SMTP verification using four methods RCPT.

* Add response code 452 (Quota expired).

1.0.1
-----
* SMTP verification using four methods EXPN.

1.0.0
-----
* Syntax validation using a RFC 5322-compliant regex.

* DNS MX record verification with IDNA support.

* SMTP verification using four methods VRFY.