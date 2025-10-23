
# from openai import AzureOpenAI
# from .config import settings

# client = AzureOpenAI(
#     azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
#     api_key=settings.AZURE_OPENAI_API_KEY,
#     api_version=settings.AZURE_OPENAI_API_VERSION,
# )

# def build_prompt(topic: str, keywords: str, tone: str, audience: str, word_count: int) -> list[dict]:
#     system = (
#         "You are an expert blog writer and SEO strategist. Write clear, factual, well-structured articles with headings, subheadings, bullets, and concise paragraphs. Include a compelling title, an introduction, a body with 3-5 sections, and a conclusion with a call-to-action. Provide an SEO meta title and meta description at the end. Avoid hallucinations and cite general concepts without fabricating sources."
#     )
#     user = f'''Generate a blog post with the following settings:

# - Topic: {topic}
# - Target audience: {audience}
# - Tone: {tone}
# - Keywords: {keywords}
# - Target length: ~{word_count} words (±10%)

# Requirements:
# 1) Use markdown with H1 for the title, H2/H3 section headings.
# 2) Make it skimmable with bullets and short paragraphs.
# 3) Optimize for the provided keywords naturally (no keyword stuffing).
# 4) End with: 
#    - **SEO Meta Title:** ...
#    - **SEO Meta Description (150-160 chars):** ...
# 5) If information is uncertain or speculative, say so.
# '''
#     return [
#         {"role": "system", "content": system},
#         {"role": "user", "content": user},
#     ]


# def generate_blog(topic: str, keywords: str, tone: str, audience: str, word_count: int) -> str:
#     messages = build_prompt(topic, keywords, tone, audience, word_count)
#     resp = client.chat.completions.create(
#         model=settings.AZURE_OPENAI_DEPLOYMENT,
#         messages=messages,
#         temperature=0.7,
#         max_tokens=min(4096, int(word_count * 3)),
#     )
#     content = resp.choices[0].message.content or ''
#     return content


8# app/services/azure_openai.py
from openai import AzureOpenAI
from ..config import settings

client = AzureOpenAI(
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
)

def build_prompt(topic: str, keywords: str, tone: str, audience: str, word_count: int) -> list[dict]:
    system = (
        "You are an expert blog writer and SEO strategist. Write clear, factual, well-structured articles with headings, subheadings, bullets, and concise paragraphs. Include a compelling title, an introduction, a body with 3-5 sections, and a conclusion with a call-to-action. Provide an SEO meta title and meta description at the end. Avoid hallucinations and cite general concepts without fabricating sources."
    )
    user = f'''Generate a blog post with the following settings:

- Topic: {topic}
- Target audience: {audience}
- Tone: {tone}
- Keywords: {keywords}
- Target length: ~{word_count} words (±10%)

Requirements:
1) Use markdown with H1 for the title, H2/H3 section headings.
2) Make it skimmable with bullets and short paragraphs.
3) Optimize for the provided keywords naturally (no keyword stuffing).
4) End with: 
   - **SEO Meta Title:** ...
   - **SEO Meta Description (150-160 chars):** ...
5) If information is uncertain or speculative, say so.
'''
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]

def generate_blog(topic: str, keywords: str, tone: str, audience: str, word_count: int) -> str:
    messages = build_prompt(topic, keywords, tone, audience, word_count)
    max_out_tokens = min(2048, max(512, int(word_count * 2.5)))
    resp = client.chat.completions.create(
        model=settings.AZURE_OPENAI_DEPLOYMENT,  # deployment name
        messages=messages,
        temperature=0.7,
        max_tokens=max_out_tokens,
    )
    return (resp.choices[0].message.content or '').strip()
