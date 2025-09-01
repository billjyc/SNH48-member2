import json
import re


def process_str_to_json(source):
    pattern = r"get_members_success\((\{[\s\S]*\})\);"
    match = re.search(pattern, source)
    if match:
        json_str = match.group(1)
        data = json.loads(json_str)
        return data
    return None