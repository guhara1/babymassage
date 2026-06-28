from . import (main, safe_booking, report, use_cases, policy,
               seoul, gyeonggi, incheon, stations)

PAGES = (
    [main.PAGE]
    + safe_booking.PAGES
    + report.PAGES
    + use_cases.PAGES
    + policy.PAGES
    + seoul.PAGES
    + gyeonggi.PAGES
    + incheon.PAGES
    + stations.PAGES
)
