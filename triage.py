import re


_QUESTION_CUE = re.compile(
    r"^\s*(?:how|what|when|where|why|who|which|is|are|am|do|does|did|"
    r"can|could|would|should|will)\b|\?",
    re.IGNORECASE,
)
_BUG_CUE = re.compile(
    r"\b(?:bug|crash(?:es|ed|ing)?|error|fail(?:s|ed|ure)?|broken|"
    r"regression|defect)\b|\bnot working\b|\bdoesn['’]t work\b",
    re.IGNORECASE,
)


def classify(title: str) -> str:
    """Return 'bug', 'feature' or 'question' for an issue title."""
    if _QUESTION_CUE.search(title):
        return "question"
    if _BUG_CUE.search(title):
        return "bug"
    return "feature"