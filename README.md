# Community Inference Backend

This repository is a backend only reference implementation for a community grounded inference layer.

The goal is to provide a small, auditable server that can:

- Accept short knowledge snippets (lessons) submitted by contributors
- Retrieve a limited set of relevant snippets for a given question
- Produce an answer that is constrained to the retrieved snippets
- Return lightweight citations that point back to the snippets used
- Apply a moderation gate before ingesting content and before answering

This project is intentionally minimal. It is designed to be swapped into your own environment by replacing two parts:

- Storage: replace the in memory store with your database of choice
- Inference and moderation: replace the stub modules with your own engine or provider

## Why this exists

Many AI applications rely on large general models that can introduce hallucinations or drift from your intended knowledge. This approach uses a small, community curated library and forces answers to stay within retrieved context. The system improves as contributors add better lessons, and each answer can point to the source snippets.

## What is in the repo

- A small HTTP server with JSON endpoints
- A lesson store module (default is in memory)
- A knowledge pack builder that formats lessons into a strict context block
- An inference module (default is a stub that you replace)
- A moderation module (default is a contract stub that you replace)
- Documentation and curl examples

## Core idea

1. Ingest: contributors submit lessons that are stored as structured records.
2. Retrieve: when a user asks a question, the server selects a limited set of lessons.
3. Constrain: the inference step only sees the question and the retrieved lessons.
4. Cite: the response includes citations that map back to lesson ids and titles.
5. Gate: moderation can block unsafe or low quality submissions and requests.

This is not model training. Lessons do not update model weights. Lessons update the library that retrieval pulls from.

## API surface

The default server exposes:

- GET /health
- GET /lessons
- POST /submitLesson
- POST /moderate
- POST /inference

See API.md for request and response formats.

## Running locally

Prerequisites:

- Node.js 18 or newer

Install and run:

1. npm install
2. npm run dev

The server listens on port 8080 by default. Set PORT to change it.

## Replacing the storage layer

The store is written as a small module with list and insert functions. Replace it with a thin adapter over your database. Keep inputs clamped and validated.

## Replacing the inference layer

The inference module is a single function that receives:

- question
- lessons (retrieved snippets)

Return:

- answer (string)
- citations (array of lesson references)
- confidence (0 to 100 integer)

You can implement this with any engine. The contract stays the same.

## Replacing moderation

The moderation module is a single function that receives:

- mode (ask or teach)
- content fields

Return:

- ok (boolean)
- reason (string)
- isQuestion (boolean for ask mode)

You can implement this with rules, a classifier, or an external service.
