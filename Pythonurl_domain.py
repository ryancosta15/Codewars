def domain_name(url):
    if "www" in url:
        first = url.find(".",)
    elif "http:" in url:
        first = 6
    elif "https" in url:
        first = 7
    else:
        first = -1
    last = url.find(".", first+1)
    return url[first+1:last]
