# DoRecifeChatFlow

> Companion to [`do_recife_embedder`](https://github.com/danielfsbarreto/do_recife_embedder),
> which builds the MongoDB Atlas vector store this flow reads from.

A minimal [crewAI](https://crewai.com) Flow wrapping a single conversational RAG
agent that answers questions about the **Diário Oficial do Recife**, grounding
every answer in the embeddings produced by `do_recife_embedder`.

The agent is transparent about tool use, stays strictly on the topic of the
Diário Oficial, and always replies in the same language as the user.

## Structure

- `main.py` – `DoRecifeChatFlow`, a `Flow[Conversation]` that appends the user
  message, calls the agent, and stores the reply.
- `agents/` – `DoRecifeAgent`, a streaming LiteAgent (`agent.kickoff()`).
- `tools/` – `DoRecifeVectorSearchTool`, a pre-configured `MongoDBVectorSearchTool`.
- `types/` – `Conversation` and `Message` state models.

## Requirements

- Python >=3.10, <3.14 and [uv](https://docs.astral.sh/uv/)
- Access to the same MongoDB Atlas cluster the embedder wrote to
- A Gemini API key (agent) and an OpenAI API key (query embeddings)

## Setup

Install dependencies:

```bash
crewai install
```

Add the required variables to `.env`:

```bash
GEMINI_API_KEY=AI...
OPENAI_API_KEY=sk-...
MONGODB_CONNECTION_STRING=mongodb+srv://...
```

`GEMINI_API_KEY` runs the agent (`gemini/gemini-3.5-flash`). `OPENAI_API_KEY`
embeds the query (`text-embedding-3-large`, 3072-dim) and must match the
embedder's settings or vector search returns irrelevant results.

## Usage

```bash
crewai run
```

Change the question by editing the `user_message` input in
[`src/do_recife_chat_flow/main.py`](src/do_recife_chat_flow/main.py).
