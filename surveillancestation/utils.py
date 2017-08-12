import json

def jsondump(data):
    """Return prettified JSON dump"""
    return json.dumps(data, sort_keys=True, indent=4)

def jsonprint(data):
    """Prettify JSON dump to stdout"""
    print(jsondump(data))