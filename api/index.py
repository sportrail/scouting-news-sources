"""
Vercel serverless entrypoint for VibeCheck.

Vercel's @vercel/python runtime invokes a BaseHTTPRequestHandler subclass
named `handler`. VibeCheckHandler already implements the full router
(do_GET / do_POST) for the dashboard, index, public cards and JSON API,
so the function is just that handler exposed under the expected name.

All request paths are rewritten to this function by vercel.json; the
original URL is preserved in self.path, which the router dispatches on.
"""

import os
import sys

# The shared modules live at the repo root, one level above /api.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scout_web import VibeCheckHandler


class handler(VibeCheckHandler):
    pass
