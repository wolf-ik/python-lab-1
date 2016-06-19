import re


def email_validation(email):
    r = re.compile(r"^[-a-z0-9!#$%&'*+/=?^_`{|}~]+"
                   r"(\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)*"
                   r"@([a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*"
                   r"(aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|[a-z][a-z])$", re.IGNORECASE)

    if r.match(email):
        return True
    else:
        return False


def float_parse(number_str):
    r = re.compile(ur"(-?\d+(.|,)\d+(\*?10\^-?\d+|[Ee]-?\d+)?)$")

    num = r.search(number_str)
    if num:
        return num.group()
    else:
        return False


def url_parse(url):
    r = re.compile(r'(?:(?P<protocol>https?|ftp)://)?'
                   r'(?:(?P<login>\S+?)(?::(?P<password>\S*))?@)?'
                   r'(?P<host>(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9]+-?)*[a-z0-9]+)(?:\.(?:[a-z0-9]+-?)*[a-z0-9]+)*(?:\.(?:[a-z]{2,})))'
                   r'(?::(?P<port>\d{2,5}))?'
                   r'(?:/(?P<path>[^\s]*?))?'
                   r'(?:\?(?P<query>\S+?))?'
                   r'(?:#(?P<fragment>\S+?))?$', re.MULTILINE)

    url = r.finditer(url)
    for item in url:
        return item.groups()


def regex_handler(string, type='email'):
    regex_mapping = {
        'email': email_validation,
        'float': float_parse,
        'url': url_parse,
    }
    regex_func = regex_mapping.get(type)
    if regex_func is None:
        return 'Please, enter valid type.'
    else:
        return regex_func(string)
