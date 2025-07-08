import requests
import sys
import os
import yaml
from urllib.parse import urlparse
from pathlib import Path

def get_llm_md_url(url):
    """Attempt to construct a .llm.md version of the original URL."""
    parsed = urlparse(url)
    base = parsed.scheme + "://" + parsed.netloc + parsed.path.rstrip("/")
    return base + ".llm.md"

def fetch_llm_md(url):
    try:
        print(f"🔍 Checking for LLM Markdown at:\n{url}")
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"❌ Not found ({response.status_code})")
            return None
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return front, body
    return {}, content

def save_to_file(content, url):
    domain = urlparse(url).netloc
    filename = Path(f"output/{domain}.llm.md")
    filename.parent.mkdir(exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Saved to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python llm-md-crawler.py <url>")
        return

    original_url = sys.argv[1]
    md_url = get_llm_md_url(original_url)

    content = fetch_llm_md(md_url)
    if content:
        front, body = parse_frontmatter(content)
        print("🧾 Frontmatter:")
        print(yaml.dump(front, sort_keys=False))
        print("\n📝 Content:\n")
        print(body[:500] + "..." if len(body) > 500 else body)

        save_to_file(content, original_url)
    else:
        print("⚠️ No `.llm.md` version found or could not be fetched.")

if __name__ == "__main__":
    main()
