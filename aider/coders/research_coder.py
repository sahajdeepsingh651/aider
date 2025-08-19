from .base_coder import Coder
from .research_prompts import ResearchPrompts


class ResearchCoder(Coder):
    """Ask research questions about any topics."""

    edit_format = "research"
    gpt_prompts = ResearchPrompts()
