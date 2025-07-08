📜 protocol/spec.md – Initial Draft

# llm-md Protocol Specification (v0.1)

## Overview

The `llm-md` protocol defines a simple convention for exposing clean, structured, Markdown-based versions of web content — optimized for direct consumption by Large Language Models (LLMs), agents, and AI crawlers.

It provides a lightweight, predictable layer that enables faster ingestion, better structure, and more semantic clarity compared to traditional HTML scraping or DOM parsing.

---

## 🔗 URL Structure

Every `.llm.md` file is an **alias** of a human-facing content page.

### Convention 1: Extension-based

Given a canonical URL:

https://example.com/page

The LLM-readable version should be served at:

https://example.com/page.llm.md

### Convention 2: Directory-based

Optional alternate path:

https://example.com/.llm/page.md

---

## 📄 File Format

### Required: YAML Frontmatter

The top of every `.llm.md` file must include metadata:

```yaml
---
title: "Title of the Page"
source_url: "https://example.com/page"
last_updated: "2025-07-06"
tags: ["tag1", "tag2"]
lang: "en"
format_version: "0.1"
---

Required: Markdown Body

Structured using standard Markdown with headings (#), lists, code blocks, etc.

# Introduction

This document explains...

## Key Points

- Structured
- Clean
- Easy to parse

## Code Example

```python
print("Hello, LLMs!")

---

## 🤖 Crawler Behavior

- Always check for `.llm.md` version first (extension or `.llm/` path).
- If `.llm.md` is not found, fallback to traditional HTML processing.
- Extract YAML frontmatter separately from Markdown body.
- Prefer `.llm.md` as authoritative when available.

---

## 🧩 Use Cases

- LLM-enhanced search engines
- Chatbots retrieving up-to-date structured content
- Developer documentation crawlers
- News summarizers or feed generators
- Plugins and agents reading the "clean web"

---

## 🛠 Tooling Plan (Future)

- `llm-md-crawler`: CLI for fetching + parsing `.llm.md`
- `llm-md-validator`: Linter for format + schema
- `llm-md-browser`: Dev tool to preview `.llm.md` if available
- `llm-md-converter`: HTML → Markdown extractor for auto-generating content

---

## 📌 Notes

- `.llm.md` files should be accessible over HTTPS without auth
- Can be stored alongside original HTML content (static or dynamic)
- Can be generated at build time for static sites, or served dynamically

---

## 🌱 Future Ideas

- Embed references / citations in standardized format
- Optional JSON version (`.llm.json`) for API use
- Register `.well-known/llm-md.json` endpoint to define rules

---
