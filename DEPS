vars = {
"googlecode_url": "http://%s.googlecode.com/svn"
}

deps = {
"src/tools/gyp": "https://chromium.googlesource.com/external/gyp",
}

hooks = [
{
"name": "gyp",
"pattern": ".",
"action": ["python", "src/tools/gyp/gyp_main.py", "New64/scripts/New64.gyp"],
}
]