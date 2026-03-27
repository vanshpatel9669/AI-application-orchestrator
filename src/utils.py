import json


def safe_load_json(text: str):
    """
    Try to parse JSON directly.
    If the model includes surrounding text, extract the JSON object.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1

        if start != -1 and end != -1 and end > start:
            candidate = text[start:end]
            return json.loads(candidate)

        raise ValueError("Could not parse JSON from model response.")


def clamp_score(value, minimum=0, maximum=100):
    try:
        value = int(value)
    except Exception:
        value = 0
    return max(minimum, min(maximum, value))